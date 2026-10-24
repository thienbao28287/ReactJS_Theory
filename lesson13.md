# Bài 13: Gọi API với Redux và làm quen RTK Query

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn quản lý một request dùng chung bằng `createAsyncThunk`, theo dõi trạng thái tải và thử lại khi lỗi. Sau đó, bạn sẽ thực hiện cùng nhu cầu bằng RTK Query để so sánh phần code phải tự quản lý.

### Kiến thức cần có và chuẩn bị

Hoàn thành [bài 12](./lesson12.md) để có Redux Toolkit v2, React Redux v9 và Provider trong `main.jsx`. Bài này thay store và App của ví dụ giỏ hàng bằng ví dụ danh sách API. Giữ file giỏ hàng để tham khảo; các file đó chưa được gắn vào store mới.

Hai phương án thunk và RTK Query thay thế nhau. Kiểm tra phương án thứ nhất trước khi đổi sang phương án thứ hai. API công khai dùng dữ liệu sản phẩm thử nghiệm với giá USD, khác giá VND của catalog mẫu bài 12.

### Kết quả sau bài học

- Phân biệt state giao diện và dữ liệu do server quản lý.
- Xử lý vòng đời `pending`, `fulfilled`, `rejected`.
- Giữ reducer thuần và thực hiện request trong thunk.
- Dùng RTK Query để lấy dữ liệu, chia sẻ cache và chủ động refetch.
- Hiểu mục đích typed hooks khi dự án dùng TypeScript.

## 1. Khi nào đưa request vào Redux?

Nếu dữ liệu chỉ phục vụ một component, Effect hoặc custom Hook ở bài 8 có thể đủ. Khi nhiều màn hình cần cùng dữ liệu và trạng thái tải, có thể tổ chức request ở lớp dùng chung.

| Loại dữ liệu | Ví dụ | Cách quản lý có thể dùng |
| --- | --- | --- |
| State UI cục bộ | Ô tìm kiếm, mở menu | `useState`. |
| State dùng chung phía client | Giỏ hàng trong phiên | Redux slice hoặc Context phù hợp. |
| Dữ liệu server | Danh sách sản phẩm từ API | RTK Query; hoặc thunk khi cần tự tổ chức luồng. |

Thunk là hàm có thể thực hiện công việc rồi dispatch action. `createAsyncThunk` tạo các action vòng đời cho Promise; nó không tự tạo reducer và không cung cấp sẵn cache như RTK Query.

## 2. Tạo request bằng createAsyncThunk

### Bước 1 Viết productsSlice

Tạo `src/features/products/productsSlice.js`:

```js
import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

export const fetchProducts = createAsyncThunk(
  "products/fetchProducts",
  async (_, { signal, rejectWithValue }) => {
    try {
      const response = await fetch("https://dummyjson.com/products?limit=8", { signal });
      if (!response.ok) return rejectWithValue(`Máy chủ trả HTTP ${response.status}.`);
      const data = await response.json();
      if (!Array.isArray(data.products)) {
        return rejectWithValue("Dữ liệu sản phẩm không hợp lệ.");
      }
      return data.products;
    } catch (error) {
      if (signal.aborted) throw error;
      return rejectWithValue("Không tải được sản phẩm. Kiểm tra mạng và thử lại.");
    }
  },
  {
    condition: (_, { getState }) => getState().products.status !== "loading",
  },
);

const productsSlice = createSlice({
  name: "products",
  initialState: { items: [], status: "idle", error: "", currentRequestId: null },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchProducts.pending, (state, action) => {
        state.status = "loading";
        state.error = "";
        state.currentRequestId = action.meta.requestId;
      })
      .addCase(fetchProducts.fulfilled, (state, action) => {
        if (state.currentRequestId !== action.meta.requestId) return;
        state.items = action.payload;
        state.status = "succeeded";
        state.currentRequestId = null;
      })
      .addCase(fetchProducts.rejected, (state, action) => {
        if (state.currentRequestId !== action.meta.requestId) return;
        state.status = action.meta.aborted ? "idle" : "failed";
        state.error = action.meta.aborted ? "" : (action.payload || "Request thất bại.");
        state.currentRequestId = null;
      });
  },
});

export default productsSlice.reducer;
```

`rejectWithValue` đưa thông báo đã chuẩn bị vào `action.payload`. `extraReducers` lắng nghe action do thunk tạo. Request ID giúp đối chiếu đúng lượt đang theo dõi; `condition` chặn gửi thêm khi store đã loading.

`signal` cho phép thunk truyền yêu cầu hủy xuống fetch. Không đặt request trong reducer; reducer chỉ cập nhật trạng thái theo action.

### Bước 2 Gắn reducer vào store

Thay toàn bộ `src/app/store.js` bằng:

```js
import { configureStore } from "@reduxjs/toolkit";
import productsReducer from "../features/products/productsSlice";

export const store = configureStore({
  reducer: { products: productsReducer },
});
```

Giữ `main.jsx` của bài 12 import `store` từ file này và bọc Provider. Nếu muốn chạy cả giỏ hàng, có thể thêm `cart: cartReducer` vào object reducer, nhưng App dưới đây chỉ đọc products.

### Bước 3 Tạo giao diện và thử lại

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchProducts } from "./features/products/productsSlice";

export default function App() {
  const { items, status, error } = useSelector((state) => state.products);
  const dispatch = useDispatch();

  useEffect(() => {
    if (status === "idle") dispatch(fetchProducts());
  }, [status, dispatch]);

  return (
    <main>
      <h1>Sản phẩm từ Redux thunk</h1>
      <button disabled={status === "loading"} onClick={() => dispatch(fetchProducts())}>
        {status === "loading" ? "Đang tải..." : "Tải lại"}
      </button>
      {status === "loading" && <p role="status">Đang tải sản phẩm...</p>}
      {status === "failed" && <p role="alert">{error}</p>}
      {status === "succeeded" && items.length === 0 && <p>Chưa có sản phẩm.</p>}
      <ul>{items.map((p) => <li key={p.id}>{p.title} - {p.price} USD</li>)}</ul>
    </main>
  );
}
```

Request trong ví dụ thuộc store dùng chung nên được phép tiếp tục khi màn hình bị gỡ; Effect không hủy request khi unmount. `condition` chặn lượt dispatch lặp lúc đang loading, kể cả lượt kiểm tra Effect của Strict Mode. Với request chỉ thuộc component và cần hủy khi rời trang, dùng cleanup như bài 6/8 hoặc thiết kế vòng đời riêng, không ghép cơ chế hủy vào đây mà bỏ qua việc reset status.

Khi tải lại, danh sách cũ vẫn hiển thị và có chỉ báo loading. Nếu lượt tải lại lỗi, dữ liệu cũ được giữ cùng thông báo để người dùng biết chưa lấy được bản mới.

### Bước 4 Kiểm tra vòng đời

1. Mở Redux DevTools: sau lúc mount có action pending rồi fulfilled.
2. Bật mạng chậm, nhấn Tải lại: nút bị khóa, danh sách trước vẫn còn.
3. Bật Offline, nhấn Tải lại: có rejected, status failed và thông báo lỗi.
4. Chuyển Online, nhấn lại: lỗi được xóa khi pending, danh sách tải thành công.
5. Xem state: chỉ có dữ liệu và chuỗi trạng thái, không lưu Promise hay Response.

Promise từ `dispatch(fetchProducts())` thường resolve thành action cuối cùng kể cả khi request bị reject. Nếu cần `try/catch` ở event handler, dùng `await dispatch(fetchProducts()).unwrap()`; không giả định `await dispatch(...)` tự ném lỗi nghiệp vụ.

## 3. Thực hiện lại bằng RTK Query

**RTK Query** cung cấp lớp lấy dữ liệu và cache đi cùng Redux Toolkit. Nó tạo Hook từ endpoint, theo dõi request và chia sẻ kết quả theo endpoint cùng tham số. Không cần cài thêm package cho phần này.

### Bước 1 Tạo API slice

Tạo `src/services/productsApi.js`:

```js
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const productsApi = createApi({
  reducerPath: "productsApi",
  baseQuery: fetchBaseQuery({ baseUrl: "https://dummyjson.com" }),
  endpoints: (builder) => ({
    getProducts: builder.query({
      query: (limit = 8) => `/products?limit=${limit}`,
    }),
  }),
});

export const { useGetProductsQuery } = productsApi;
```

`fetchBaseQuery` dùng fetch; không dùng Axios Instance của bài 6 nên không tự nhận interceptors ở đó. Nếu API cần token, cấu hình riêng tại base query theo hệ thống xác thực của dự án.

### Bước 2 Thay store

Thay toàn bộ `src/app/store.js` bằng:

```js
import { configureStore } from "@reduxjs/toolkit";
import { productsApi } from "../services/productsApi";

export const store = configureStore({
  reducer: { [productsApi.reducerPath]: productsApi.reducer },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(productsApi.middleware),
});
```

Cả reducer và middleware đều cần được đăng ký. Callback middleware giữ các middleware mặc định rồi nối API middleware; không thay bằng một mảng chỉ có API middleware.

### Bước 3 Thay App.jsx

```jsx
import { useGetProductsQuery } from "./services/productsApi";

function ProductCount() {
  const { data } = useGetProductsQuery(8);
  return <p>Số dòng đang xem: {data?.products?.length ?? 0}</p>;
}

export default function App() {
  const { data, isLoading, isFetching, isError, refetch } = useGetProductsQuery(8);
  return (
    <main>
      <h1>Sản phẩm từ RTK Query</h1>
      <button disabled={isFetching} onClick={() => refetch()}>Tải lại</button>
      {isLoading && <p role="status">Đang tải lần đầu...</p>}
      {!isLoading && isFetching && <p role="status">Đang cập nhật dữ liệu...</p>}
      {isError && <p role="alert">Không tải được sản phẩm. Hãy thử lại.</p>}
      {!isLoading && !isError && data && !Array.isArray(data.products) && (
        <p role="alert">Dữ liệu sản phẩm không hợp lệ.</p>
      )}
      {Array.isArray(data?.products) && (
        data.products.length === 0 ? <p>Chưa có sản phẩm.</p> :
        <ul>{data.products.map((p) => <li key={p.id}>{p.title} - {p.price} USD</li>)}</ul>
      )}
      <ProductCount />
    </main>
  );
}
```

Hai component cùng gọi endpoint với tham số `8` đăng ký cùng cache entry, không cần tự chép dữ liệu vào một productsSlice khác. `isLoading` dành cho lần tải đầu chưa có dữ liệu; `isFetching` phản ánh request đang chạy kể cả khi đã có bản trước.

Mở Network và kiểm tra hai nơi nhận cùng kết quả. Nhấn Tải lại để thấy refetch chủ động. Cache có vòng đời và cấu hình riêng; không phải dữ liệu vĩnh viễn và không tự biết mọi thay đổi bên ngoài server. Mutation và tag invalidation là hướng mở rộng sau ví dụ đọc dữ liệu này.

## 4. Làm quen typed hooks cho TypeScript

Phần chính dùng JavaScript. Những đoạn `.ts` bên dưới chỉ áp dụng khi bạn đã tạo project React TypeScript và store/slice có kiểu phù hợp; không dán cú pháp type vào file `.js`.

Trong module store TypeScript, sau khi tạo `store`, khai báo:

```ts
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

Tạo `src/app/hooks.ts` trong project TypeScript:

```ts
import { useDispatch, useSelector } from "react-redux";
import type { AppDispatch, RootState } from "./store";

export const useAppDispatch = useDispatch.withTypes<AppDispatch>();
export const useAppSelector = useSelector.withTypes<RootState>();
```

`RootState` lấy kiểu từ store, `AppDispatch` bao gồm khả năng dispatch thunk. Dùng hai Hook này trong component `.tsx` giúp trình soạn thảo kiểm tra đường dẫn state và payload; chúng không tạo thêm store hoặc thay đổi cách Redux chạy. API `withTypes` cần React Redux hỗ trợ API này, ví dụ nhánh 9 từ 9.1 trở lên.

## 5. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Không thấy dữ liệu sau fulfilled | Khóa reducer và selector cần khớp; kiểm tra shape API. |
| Rejected không vào catch ở component | Dùng `.unwrap()` nếu muốn xử lý theo Promise ném lỗi. |
| RTK Query cảnh báo middleware | Đăng ký cả API reducer và API middleware. |
| Tạo hai nguồn dữ liệu cùng endpoint | Chọn cache RTK Query hoặc luồng thunk cho nhu cầu đó, tránh chép lặp vô cớ. |
| TypeScript báo lỗi trong file JS | Phần typed hooks chỉ dành cho project TS. |

## 6. Ôn tập và bài tập thêm

1. `createAsyncThunk` tự tạo những action nào và còn cần tự viết phần gì?
2. Vì sao request dùng chung có thể có vòng đời khác request thuộc component?
3. Thêm endpoint chi tiết sản phẩm vào RTK Query và đọc ID từ route bài 3.
4. Truyền limit khác nhau và quan sát các cache entry trong DevTools.
5. So sánh số phần state, action và Effect phải tự quản lý giữa hai cách, không chỉ so sánh số dòng code.

## Tài liệu tham khảo

- [Redux Toolkit: createAsyncThunk](https://redux-toolkit.js.org/api/createAsyncThunk).
- [Redux Toolkit: RTK Query](https://redux-toolkit.js.org/rtk-query/overview).
- [React Redux: TypeScript và typed hooks](https://react-redux.js.org/using-react-redux/usage-with-typescript).

[Bài 12: Redux Toolkit](./lesson12.md) | [Bài 14: Làm việc với backend](./lesson14.md) | [Quay về roadmap](./README.md)
