# Bài 12: Quản lý giỏ hàng bằng Redux Toolkit

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn tạo store dùng chung, tổ chức logic bằng slice và dùng Redux trong component. Bạn sẽ xây dựng giỏ hàng có thêm sản phẩm, đổi số lượng, xóa và tính tổng tiền.

### Kiến thức cần có và chuẩn bị

Bạn cần biết action, reducer và Context ở bài 11. Mở project Vite và chạy:

```bash
npm install @reduxjs/toolkit@2 react-redux@9
```

Giữ JavaScript trong phần chính. Redux Toolkit đã bao gồm công cụ Redux cần dùng; không cần cài thêm `redux` riêng cho ví dụ. Cài Redux DevTools trên trình duyệt nếu muốn theo dõi action/state.

### Kết quả sau bài học

- Giải thích store, action, reducer, dispatch và selector.
- Tạo store bằng `configureStore` và slice bằng `createSlice`.
- Kết nối React bằng Provider, `useSelector` và `useDispatch`.
- Cập nhật giỏ hàng và tính dữ liệu dẫn xuất từ state.

## 1. Redux giải quyết việc gì?

Redux quản lý state qua store trung tâm và luồng cập nhật có cấu trúc. Nó hữu ích khi nhiều màn hình cùng dùng dữ liệu, logic cập nhật nhiều và cần theo dõi lịch sử action. Không cần đưa mọi input hoặc trạng thái mở menu vào Redux.

```text
UI → dispatch(action) → reducer → store giữ state mới → selector đọc → UI cập nhật
```

Redux Core cung cấp các khái niệm nền tảng. Redux Toolkit là cách viết Redux được khuyến nghị trong tài liệu Redux, giảm phần cấu hình và tạo action/reducer thủ công.

| Thành phần | Ví dụ trong bài |
| --- | --- |
| Store | Giữ `{ cart: { items: [] } }`. |
| Action | Yêu cầu thêm sản phẩm hoặc xóa một dòng. |
| Reducer | Quyết định số lượng và các dòng sau action. |
| Dispatch | Gửi action từ nút bấm. |
| Selector | Đọc items, tính tổng số lượng và tiền. |

## 2. Tạo cartSlice

### Bước 1 Chuẩn bị cấu trúc

```text
src/
├── app/
│   └── store.js
├── features/
│   └── cart/
│       └── cartSlice.js
├── App.jsx
└── main.jsx
```

### Bước 2 Viết slice

Tạo `src/features/cart/cartSlice.js`:

```js
import { createSlice } from "@reduxjs/toolkit";

const cartSlice = createSlice({
  name: "cart",
  initialState: { items: [] },
  reducers: {
    addItem(state, action) {
      const product = action.payload;
      const existing = state.items.find((item) => item.id === product.id);
      if (existing) {
        existing.quantity += 1;
      } else {
        state.items.push({
          id: product.id, title: product.title, price: product.price, quantity: 1,
        });
      }
    },
    changeQuantity(state, action) {
      const { id, quantity } = action.payload;
      if (!Number.isInteger(quantity) || quantity < 1) return;
      const item = state.items.find((item) => item.id === id);
      if (item) item.quantity = quantity;
    },
    removeItem(state, action) {
      state.items = state.items.filter((item) => item.id !== action.payload);
    },
    clearCart(state) {
      state.items = [];
    },
  },
});

export const { addItem, changeQuantity, removeItem, clearCart } = cartSlice.actions;
export const selectCartItems = (state) => state.cart.items;
export const selectCartCount = (state) =>
  state.cart.items.reduce((sum, item) => sum + item.quantity, 0);
export const selectCartTotal = (state) =>
  state.cart.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
export default cartSlice.reducer;
```

`createSlice` dùng Immer: cú pháp sửa `state` ở đây thực chất thao tác trên draft để tạo state mới. Quy tắc này áp dụng trong reducer do Toolkit quản lý; không lấy object từ store rồi sửa trực tiếp trong component, không áp dụng cú pháp đó cho reducer React ở bài 11.

Tổng tiền và tổng số lượng được tính từ `items`, không lưu thêm bản sao để tránh phải đồng bộ nhiều nơi. Dữ liệu nhỏ chưa cần selector memoization. Reducer chỉ nhận sản phẩm hợp lệ do ứng dụng chuẩn bị; dữ liệu API cần được kiểm tra trước khi đưa vào.

## 3. Tạo store và Provider

Tạo `src/app/store.js`:

```js
import { configureStore } from "@reduxjs/toolkit";
import cartReducer from "../features/cart/cartSlice";

export const store = configureStore({
  reducer: { cart: cartReducer },
});
```

Khóa `cart` quyết định đường dẫn `state.cart` mà selector sử dụng. Tạo store ở cấp module, không tạo mới mỗi lần App render.

Thay toàn bộ `src/main.jsx` bằng:

```jsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { store } from "./app/store";
import App from "./App";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </StrictMode>,
);
```

Điểm khởi động này cố ý không import CSS của ví dụ Tailwind. Muốn giữ style, thêm lại import CSS phù hợp sau khi kiểm tra ví dụ chạy được.

## 4. Kết nối component

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import { useDispatch, useSelector } from "react-redux";
import {
  addItem, changeQuantity, removeItem, clearCart,
  selectCartItems, selectCartCount, selectCartTotal,
} from "./features/cart/cartSlice";

const products = [
  { id: 1, title: "Tai nghe", price: 350000 },
  { id: 2, title: "Bàn phím", price: 700000 },
];
const money = (value) => new Intl.NumberFormat("vi-VN", {
  style: "currency", currency: "VND",
}).format(value);

function Catalog() {
  const dispatch = useDispatch();
  return (
    <section>
      <h2>Sản phẩm</h2>
      <ul>{products.map((p) => (
        <li key={p.id}>
          {p.title} - {money(p.price)}
          <button onClick={() => dispatch(addItem(p))}>Thêm {p.title}</button>
        </li>
      ))}</ul>
    </section>
  );
}

function Cart() {
  const items = useSelector(selectCartItems);
  const total = useSelector(selectCartTotal);
  const dispatch = useDispatch();
  if (items.length === 0) return <p>Giỏ hàng đang trống.</p>;
  return (
    <section>
      <h2>Giỏ hàng</h2>
      <ul>{items.map((item) => (
        <li key={item.id}>
          <span>{item.title}: {item.quantity} × {money(item.price)}</span>
          <button disabled={item.quantity <= 1} onClick={() => dispatch(changeQuantity({
            id: item.id, quantity: item.quantity - 1,
          }))}>Giảm {item.title}</button>
          <button onClick={() => dispatch(changeQuantity({
            id: item.id, quantity: item.quantity + 1,
          }))}>Tăng {item.title}</button>
          <button onClick={() => dispatch(removeItem(item.id))}>Xóa {item.title}</button>
        </li>
      ))}</ul>
      <p>Tổng tiền: {money(total)}</p>
      <button onClick={() => dispatch(clearCart())}>Xóa toàn bộ giỏ</button>
    </section>
  );
}

export default function App() {
  const count = useSelector(selectCartCount);
  return <main><h1>Cửa hàng - {count} sản phẩm trong giỏ</h1><Catalog /><Cart /></main>;
}
```

`useSelector` đăng ký đọc store; khi kết quả selector thay đổi theo phép so sánh mặc định, component cần cập nhật. `useDispatch` lấy hàm gửi action. Phải gọi `dispatch(addItem(p))`, không chỉ gọi `addItem(p)` vì action creator mới chỉ tạo object action.

## 5. Kiểm tra kết quả

1. Thêm Tai nghe hai lần: có một dòng số lượng 2, tổng 700.000 đồng.
2. Thêm Bàn phím: tổng số lượng là 3, tổng tiền 1.400.000 đồng.
3. Giảm Tai nghe về 1: nút giảm bị khóa, số lượng không về 0.
4. Xóa từng dòng và xóa toàn bộ: tổng và trạng thái rỗng cùng cập nhật.
5. Mở Redux DevTools, quan sát action `cart/addItem` và state trước/sau.
6. Tải lại trang: giỏ rỗng vì chưa có persistence. Đây chưa phải giỏ đồng bộ với tài khoản hay tồn kho backend.

Không lưu Promise, DOM element hoặc function vào store. Với thời gian, thường lưu chuỗi ISO hoặc timestamp thay vì Date object. Các giá trị đơn giản giúp debug và kiểm tra state dễ hơn.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Không tìm thấy React Redux context | Bọc App bằng Provider đúng store. |
| `state.cart` undefined | Kiểm tra khóa reducer trong configureStore. |
| Action xuất hiện nhưng UI không đúng | Kiểm tra payload và selector; quan sát state trong DevTools. |
| Selector bị gọi nhiều hoặc cảnh báo | Không tạo object/mảng mới vô điều kiện khi chỉ cần đọc tham chiếu hiện có. |
| Giỏ mất sau refresh | Store trong bộ nhớ không tự lưu lâu dài. |

## 7. Ôn tập và bài tập thêm

1. Vì sao reducer slice được viết như sửa trực tiếp còn reducer React thông thường phải trả state mới?
2. Vì sao tổng tiền nên tính từ items?
3. Thêm giới hạn số lượng tối đa 10 ở reducer và phản ánh bằng trạng thái nút.
4. Tách Catalog và Cart thành hai component riêng, giữ các import và Provider.
5. Tạo favoritesSlice với danh sách ID yêu thích; không sao chép toàn bộ catalog vào từng danh sách.

## Tài liệu tham khảo

- [Redux: Quick Start](https://redux.js.org/tutorials/quick-start).
- [Redux Toolkit: createSlice](https://redux-toolkit.js.org/api/createSlice).
- [Redux Toolkit: Reducers và Immer](https://redux-toolkit.js.org/usage/immer-reducers).
- [React Redux: Hooks](https://react-redux.js.org/api/hooks).

[Bài 11: Context và reducer](./lesson11.md) | [Bài 13: Redux bất đồng bộ](./lesson13.md) | [Quay về roadmap](./README.md)
