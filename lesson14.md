# Bài 14: Làm việc với backend, API contract và biến môi trường

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn đọc mô tả API trước khi viết giao diện, thử request độc lập bằng Postman và đưa địa chỉ server vào biến môi trường. Bạn sẽ xây dựng màn hình sản phẩm có phân trang để đối chiếu dữ liệu trên Network với dữ liệu component nhận được.

### Kiến thức cần có và chuẩn bị

Bạn cần hiểu request/response, Axios và Service Layer ở bài 6; state và Effect ở bài 4. Dùng project Vite JavaScript, chạy `npm install axios` nếu chưa cài. Giữ `src/main.jsx` render `<App />`; Provider của bài 13 có thể giữ vì ví dụ này không đọc Redux.

Cài Postman hoặc dùng phiên bản web với agent phù hợp để gửi request. Các bước mô tả trường request thay vì phụ thuộc vào vị trí nút trong từng phiên bản Postman.

### Kết quả sau bài học

- Đọc method, path, tham số, body, phản hồi và mã lỗi của endpoint.
- Tái hiện request bằng Postman và mô tả lỗi bằng dữ kiện.
- Dùng `.env`, `.env.example` và `import.meta.env` trong Vite.
- Truyền limit/skip vào service, kiểm tra dữ liệu và hủy request cũ.

## 1. API contract là gì?

**API contract** là thỏa thuận giữa bên gọi và bên cung cấp API: gửi gì, nhận gì và lỗi được biểu diễn ra sao. OpenAPI là định dạng mô tả API; Swagger UI là một công cụ hiển thị và thử API từ mô tả đó.

Ví dụ hợp đồng đọc sản phẩm dùng trong bài:

| Mục | Giá trị cần biết |
| --- | --- |
| Method và path | `GET /products`. |
| Query | `limit` là kích thước trang, `skip` là số dòng bỏ qua. |
| Body | Không gửi body cho request này. |
| Thành công | Object có `products`, `total`, `skip`, `limit`. |
| Giá | Giá sản phẩm của ví dụ hiển thị theo USD. |
| Xác thực | Endpoint công khai, không yêu cầu token. |

Khi nhận task có API khác, cần hỏi thêm: trường nào có thể null, ID là số hay chuỗi, phân trang theo offset hay cursor, lỗi validation có tên trường hay không và ai được phép gọi. Không tự đoán cấu trúc từ tên endpoint.

## 2. Thử API trong Postman

### Bước 1 Tạo request

Tạo collection `React Practice` để gom request và environment `Local Practice` có biến `base_url` bằng `https://dummyjson.com`. Biến này không chứa dấu `/` cuối.

Tạo request GET với URL:

```text
{{base_url}}/products?limit=5&skip=0
```

Chọn đúng environment, gửi request rồi đọc status, headers và JSON response. Kiểm tra `products` có năm phần tử và `total` mô tả tổng kết quả của API, không phải số dòng của trang hiện tại. Đổi `skip=5` để đọc trang tiếp theo.

### Bước 2 Thêm kiểm tra response

Trong phần script chạy sau response của Postman, thêm:

```js
pm.test("HTTP thành công", () => {
  pm.response.to.have.status(200);
});

pm.test("Có danh sách và tổng số", () => {
  const data = pm.response.json();
  pm.expect(data.products).to.be.an("array");
  pm.expect(data.products.length).to.be.at.most(5);
  pm.expect(data.total).to.be.a("number");
});
```

Đây là script của Postman, không chạy trong App.jsx. Kiểm tra shape giúp phát hiện sai hợp đồng; nó không chứng minh mọi trường sản phẩm đều đúng. Thử endpoint không tồn tại như `/products/0`, quan sát status và body lỗi rồi khôi phục URL ban đầu.

### Bước 3 Phân biệt môi trường gọi

Postman thành công nhưng trình duyệt lỗi chưa chứng minh React viết sai. Trình duyệt còn áp dụng CORS và chặn mixed content khi trang HTTPS gọi API HTTP. Cần xem Console/Network; CORS thường cần chỉnh ở backend hoặc reverse proxy có thẩm quyền. Thêm header `Access-Control-Allow-Origin` vào request hoặc dùng `no-cors` không biến response bị chặn thành JSON đọc được.

## 3. Đưa cấu hình vào biến môi trường

### Bước 1 Tạo các file tại root project

Tạo `.env`:

```dotenv
VITE_API_BASE_URL=https://dummyjson.com
```

Tạo `.env.example`:

```dotenv
VITE_API_BASE_URL=https://dummyjson.com
```

Giá trị mẫu này là URL công khai. Thêm các dòng sau vào `.gitignore` nếu chưa có, giữ những dòng khác của project:

```gitignore
.env
.env.*
!.env.example
node_modules/
dist/
```

File đã được Git theo dõi không tự biến mất khỏi lịch sử chỉ vì thêm vào `.gitignore`. Kiểm tra `git status` và `git ls-files .env` trước khi commit; nếu từng lộ secret thật, cần thu hồi secret theo hệ thống sở hữu nó.

Biến có tiền tố `VITE_` được đưa vào frontend và đọc được từ mã đã build. Chỉ dùng chúng cho cấu hình công khai; `.env` không phải kho cất mật khẩu backend. Các giá trị tùy chỉnh thường là chuỗi; đổi `.env` rồi khởi động lại dev server. Khi deploy, cần cấu hình môi trường trước bước build và build lại khi thay đổi.

### Bước 2 Tạo HTTP client và service

Tạo `src/services/apiClient.js`:

```js
import axios from "axios";

const baseURL = import.meta.env.VITE_API_BASE_URL;
if (!baseURL) throw new Error("Thiếu VITE_API_BASE_URL. Kiểm tra .env và khởi động lại Vite.");

export const apiClient = axios.create({ baseURL, timeout: 8000 });
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => Promise.reject(error),
);
```

Thay toàn bộ `src/services/productService.js` bằng:

```js
import { apiClient } from "./apiClient";

export const productService = {
  async getPage({ limit = 5, skip = 0, signal } = {}) {
    const data = await apiClient.get("/products", {
      params: { limit, skip }, signal,
    });
    if (!Array.isArray(data.products) || !Number.isInteger(data.total) || data.total < 0) {
      throw new Error("Dữ liệu phân trang không hợp lệ.");
    }
    return data;
  },
};
```

Service này thay interface của service bài 6 trong ví dụ hiện tại. Không chạy lại App cũ dùng `getAllProducts` với service mới nếu chưa khôi phục hoặc bổ sung hàm đó. Axios tự mã hóa object `params`; component không cần ghép query thủ công.

## 4. Tạo màn hình phân trang

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import axios from "axios";
import { useEffect, useState } from "react";
import { productService } from "./services/productService";

const PAGE_SIZE = 5;

export default function App() {
  const [page, setPage] = useState(0);
  const [view, setView] = useState({
    page: -1, products: [], total: 0, loading: true, error: "",
  });

  useEffect(() => {
    const controller = new AbortController();
    let active = true;
    productService.getPage({ limit: PAGE_SIZE, skip: page * PAGE_SIZE, signal: controller.signal })
      .then((data) => {
        if (active) setView({ page, products: data.products, total: data.total, loading: false, error: "" });
      })
      .catch((error) => {
        if (!active || axios.isCancel(error)) return;
        const status = error.response?.status;
        const message = status ? `Không tải được trang (HTTP ${status}).` : "Không tải được trang. Kiểm tra mạng hoặc dữ liệu API.";
        setView({ page, products: [], total: 0, loading: false, error: message });
      });
    return () => { active = false; controller.abort(); };
  }, [page]);

  const loading = view.page !== page || view.loading;
  return (
    <main>
      <h1>Sản phẩm - trang {page + 1}</h1>
      {loading ? <p role="status">Đang tải...</p> : view.error ? (
        <p role="alert">{view.error}</p>
      ) : (
        <>
          <p>Tổng: {view.total} sản phẩm</p>
          {view.products.length === 0 ? <p>Trang này chưa có sản phẩm.</p> : (
            <ul>{view.products.map((p) => <li key={p.id}>{p.title} - {p.price} USD</li>)}</ul>
          )}
        </>
      )}
      <button disabled={page === 0 || loading} onClick={() => setPage((p) => p - 1)}>Trang trước</button>
      <button disabled={loading || Boolean(view.error) || (page + 1) * PAGE_SIZE >= view.total}
        onClick={() => setPage((p) => p + 1)}>Trang sau</button>
    </main>
  );
}
```

Trang hiển thị từ 1, nhưng biến `page` bắt đầu từ 0 để tính `skip = page * PAGE_SIZE`. Lúc chuyển trang, không hiển thị dữ liệu cũ dưới số trang mới. Khi lỗi, có thể quay lại trang trước; tải lại trình duyệt để thử lại trang đầu. Nút retry ngay tại trang hiện tại là bài tập mở rộng.

## 5. Kiểm tra và báo lỗi có dữ kiện

1. Khởi động lại Vite sau khi thêm `.env`; kiểm tra trang đầu có tối đa năm dòng.
2. Sang trang hai, mở Network: query có `limit=5&skip=5`, URL dùng base từ môi trường.
3. So sánh response trong Postman, Network và dữ liệu component hiển thị.
4. Bật Offline rồi chuyển trang: có thông báo, không có lỗi hủy request hiển thị nhầm.
5. Xóa tạm biến môi trường, khởi động lại: module báo thiếu cấu hình; khôi phục sau khi thử.

Khi cần báo lỗi cho BE, chuẩn bị mô tả: môi trường, method/URL, thời điểm, tham số mẫu, status, response, kết quả mong đợi và cách tái hiện. Ví dụ: “GET /products?limit=5&skip=5 trả 200 nhưng thiếu products; UI mong đợi mảng products theo contract.” Che token và thông tin cá nhân trước khi chia sẻ log.

## 6. Ôn tập và bài tập thêm

1. OpenAPI và Swagger UI có vai trò khác nhau thế nào?
2. Vì sao biến `VITE_` không thể giữ secret?
3. Vì sao `total` khác số phần tử của trang hiện tại?
4. Thêm nút Thử lại dùng state đếm, đưa state đó vào dependencies của Effect.
5. Đưa số trang lên query URL bằng kiến thức bài 3 để refresh vẫn giữ đúng trang; kiểm tra số âm, chữ và giá trị quá lớn trước khi gọi API.

## Tài liệu tham khảo

- [OpenAPI: Đặc tả](https://spec.openapis.org/oas/latest.html).
- [Postman: Viết test script](https://learning.postman.com/docs/tests-and-scripts/write-scripts/test-scripts/).
- [Vite: Biến môi trường](https://vite.dev/guide/env-and-mode).
- [DummyJSON: Sản phẩm và phân trang](https://dummyjson.com/docs/products).

[Bài 13: Redux bất đồng bộ](./lesson13.md) | [Bài 15: Base project và Gitflow](./lesson15.md) | [Quay về roadmap](./README.md)
