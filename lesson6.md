# Bài 6: Giao tiếp với backend bằng Axios

[Quay về roadmap](./README.md)

Bài này hướng dẫn gọi API với Axios Instance, interceptors và Service Layer, sau đó hiển thị sản phẩm với trạng thái tải, lỗi và cleanup.

### Kiến thức cần có và chuẩn bị

Bạn cần nắm props, state và event handler ở bài 2; kiến thức gọi API, Effect và cleanup ở [bài 4](./lesson4.md). Mở terminal tại project Vite có `package.json`. Nếu chưa cài dependencies, chạy `npm install`; Axios được cài ở phần 1.

Giữ `src/main.jsx` render `<App />`; ví dụ này không cần router. Mở DevTools để theo dõi Console và Network khi kiểm tra request.

### Kết quả sau bài học

- Tạo Axios Instance để dùng chung cấu hình.
- Dùng interceptors để xử lý request, response và lỗi.
- Tách hàm gọi API vào Service Layer.
- Hiển thị trạng thái tải, lỗi, danh sách rỗng và hủy request khi cleanup.

## 1. Giao tiếp với backend bằng Axios

Ở bài 3 và bài 4, bạn đã dùng `fetch` để lấy dữ liệu. **Axios** là thư viện HTTP hỗ trợ cấu hình chung, xử lý JSON và interceptors. `fetch` vẫn dùng được trong dự án lớn; chọn Axios khi các khả năng này giúp tổ chức code thuận tiện hơn.

Bạn sẽ tải sản phẩm từ DummyJSON, API công khai phục vụ thực hành. **Request** là yêu cầu gửi tới máy chủ; **response** là phản hồi nhận về. Bài này dùng lại Effect và cleanup ở [bài 4](./lesson4.md).

### Bước 1 Cài Axios

Mở terminal tại thư mục project có `package.json` và chạy:

```bash
npm install axios
```

Nếu server đang chạy, dùng terminal thứ hai để cài package. Tiếp tục chạy ứng dụng bằng `npm run dev` và mở địa chỉ Local.

### Bước 2 Tạo Axios Instance

**Instance** là đối tượng Axios được cấu hình riêng. Tạo thư mục `src/utils` và file `src/utils/axiosInstance.js` với toàn bộ nội dung:

```js
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "https://dummyjson.com",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

export default axiosInstance;
```

| Cấu hình | Ý nghĩa |
| --- | --- |
| `baseURL` | Địa chỉ dùng chung; gọi `/products` sẽ dùng `https://dummyjson.com/products`. |
| `timeout` | Giới hạn thời gian chờ request, tính bằng mili giây; ở đây là 5 giây. |
| `headers` | Thông tin đi kèm request; ví dụ cấu hình cho dữ liệu JSON. |

`Content-Type` mô tả dữ liệu gửi đi, không bảo đảm server trả JSON. Với phản hồi JSON thông thường, Axios cung cấp dữ liệu đã đọc trong `response.data`, nên không gọi `response.json()` như `fetch`.

### Bước 3 Thêm Interceptors

**Interceptor** là hàm xử lý trên đường đi của request hoặc response. Đăng ký trên instance nào thì áp dụng cho các request dùng instance đó.

Thay toàn bộ `src/utils/axiosInstance.js` bằng bản sau, chỉ giữ một lần tạo instance và một `export default`:

```js
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "https://dummyjson.com",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("access_token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error),
);

axiosInstance.interceptors.response.use(
  (response) => response.data,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem("access_token");
    }
    return Promise.reject(error);
  },
);

export default axiosInstance;
```

Request interceptor đọc token lúc gửi yêu cầu, thêm `Authorization` nếu có rồi trả `config` để tiếp tục. Token là thông tin xác thực do hệ thống đăng nhập cấp. Endpoint `/products` không cần token; khi thử xác thực, chỉ dùng token thử nghiệm của API đích, không gửi token dịch vụ khác tới DummyJSON.

Response interceptor trả thẳng `response.data`. Vì vậy, **kết quả gọi instance này là dữ liệu API**, không còn là response mặc định của Axios. Với danh sách sản phẩm, dữ liệu vẫn là object có `products`, `total`, `skip`, `limit`; interceptor không bỏ các trường do backend định nghĩa.

Khi nhận `401 Unauthorized`, ví dụ xóa token rồi chuyển tiếp lỗi bằng `Promise.reject(error)` để component vẫn nhận được lỗi trong `catch`. Ứng dụng thật cần đồng bộ thêm state đăng nhập và điều hướng qua cơ chế xác thực; xóa localStorage riêng lẻ chưa thực hiện các việc đó. Không cần bật alert hoặc tự chuyển trang trong ví dụ tải sản phẩm này.

Đăng ký interceptors trong module như trên, không đặt trong thân component mỗi lần render.

## 2. Tách Service Layer và hiển thị sản phẩm

**Service Layer** là lớp các hàm chuyên giao tiếp API. Component quản lý giao diện và tương tác; service đặt tên rõ nghĩa cho request để có thể dùng lại.

Gọi API trực tiếp trong component không mặc định là sai. Khi nhiều màn hình dùng cùng endpoint hoặc logic API tăng lên, tách service giúp thay đổi cách gọi ở một nơi.

### Bước 1 Chuẩn bị cấu trúc file

Giữ instance ở phần trước và tạo thêm thư mục `services`, `components` trong `src`:

```text
src/
├── components/
│   └── ProductList.jsx
├── services/
│   └── productService.js
├── utils/
│   └── axiosInstance.js
├── App.jsx
└── main.jsx
```

### Bước 2 Viết service sản phẩm

Tạo `src/services/productService.js` với toàn bộ nội dung:

```js
import axiosInstance from "../utils/axiosInstance";

export const productService = {
  getAllProducts: ({ signal } = {}) => {
    return axiosInstance.get("/products", { signal });
  },

  getProductById: (id, { signal } = {}) => {
    return axiosInstance.get(`/products/${encodeURIComponent(id)}`, { signal });
  },
};
```

`getAllProducts` lấy một trang danh sách mặc định của API, không bảo đảm lấy toàn bộ dữ liệu. `getProductById` lấy một sản phẩm theo ID. Cả hai trả Promise để nơi gọi dùng `await` hoặc `catch`.

Tham số tùy chọn `signal` truyền yêu cầu hủy từ component xuống Axios. `{ signal } = {}` cho phép gọi hàm không truyền cấu hình khi không cần hủy.

### Bước 3 Tạo component có loading và lỗi

Tạo `src/components/ProductList.jsx` với toàn bộ nội dung:

```jsx
import axios from "axios";
import { useEffect, useState } from "react";
import { productService } from "../services/productService";

export default function ProductList() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    let active = true;

    async function loadProducts() {
      try {
        const data = await productService.getAllProducts({
          signal: controller.signal,
        });
        if (!Array.isArray(data.products)) {
          throw new Error("Dữ liệu sản phẩm không hợp lệ.");
        }
        if (active) setProducts(data.products);
      } catch (err) {
        if (!active || axios.isCancel(err)) return;
        const message = err.response?.status === 401
          ? "Phiên đăng nhập không hợp lệ. Vui lòng đăng nhập lại."
          : "Không tải được sản phẩm. Kiểm tra kết nối và tải lại trang.";
        setError(message);
      } finally {
        if (active) setLoading(false);
      }
    }

    loadProducts();
    return () => {
      active = false;
      controller.abort();
    };
  }, []);

  if (loading) return <p role="status">Đang tải sản phẩm...</p>;
  if (error) return <p role="alert">{error}</p>;
  if (products.length === 0) return <p>Chưa có sản phẩm.</p>;

  return (
    <section>
      <h2>Danh sách sản phẩm</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.title} - {product.price} USD
          </li>
        ))}
      </ul>
    </section>
  );
}
```

Component chỉ gọi hàm từ service, không cần biết địa chỉ gốc, timeout hoặc cách đính kèm token. Nó vẫn quyết định cách hiển thị đang tải, lỗi, danh sách rỗng hoặc dữ liệu thành công.

Cleanup hủy request và cờ `active` ngăn kết quả của lần setup cũ cập nhật state. `axios.isCancel` nhận diện hủy chủ động để không coi đó là lỗi tải dữ liệu. Trong Strict Mode khi phát triển, có thể thấy request bị hủy rồi request mới chạy do chu kỳ kiểm tra setup và cleanup.

### Bước 4 Gắn component vào App

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import ProductList from "./components/ProductList";

export default function App() {
  return (
    <main>
      <h1>Cửa hàng thực hành Axios</h1>
      <ProductList />
    </main>
  );
}
```

Giữ `src/main.jsx` render `<App />`, lưu các file rồi mở ứng dụng. Ví dụ này cần đủ các file instance, service, component và App, không chỉ một file `App.jsx` như các ví dụ Hook ở [bài 5](./lesson5.md).

### Bước 5 Hiểu luồng dữ liệu

```text
ProductList mount
  → Effect gọi productService.getAllProducts
  → Service dùng axiosInstance gửi GET /products
  → Request interceptor xử lý config
  → API phản hồi
  → Response interceptor trả response.data
  → Component đọc data.products và cập nhật state
  → React hiển thị danh sách
```

Nếu request thất bại, interceptor chuyển lỗi xuống `catch`; component cập nhật thông báo thay vì để người dùng chờ mà không biết kết quả.

### Bước 6 Kiểm tra kết quả

1. Mở trang và kiểm tra có tiêu đề cửa hàng, danh sách tên và giá sản phẩm.
2. Mở DevTools, chọn Network và tải lại trang. Tìm request tới `https://dummyjson.com/products`; response cần có trường `products` là mảng.
3. Chọn chế độ mạng chậm và tải lại để quan sát trạng thái tải. Timeout là 5 giây nên mạng quá chậm có thể chuyển sang lỗi.
4. Chọn Offline trong Network và tải lại để kiểm tra thông báo lỗi. Chuyển lại Online và tải lại để khôi phục dữ liệu.
5. Tạm đổi endpoint trong `getAllProducts` thành `/products/0` để thử HTTP 404. Kiểm tra giao diện lỗi rồi khôi phục `/products`.

API danh sách công khai không yêu cầu đăng nhập; ví dụ chưa thực hiện luồng đăng nhập hoặc hết hạn phiên. Hàm `getProductById` dùng cho bài tập chi tiết bên dưới.
## 3. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Không tìm thấy package `axios` | Chạy `npm install axios` trong đúng project. |
| `data.products` là `undefined` | Kiểm tra response và interceptor; đã trả `response.data` thì không đọc thêm `data.data`. |
| Service không nhận lỗi | Giữ `Promise.reject(error)` trong nhánh lỗi interceptor. |
| Lỗi timeout hoặc mạng | Kiểm tra kết nối, request trong Network và cấu hình timeout. |
| Không import được service | Kiểm tra tên file và đường dẫn tương đối theo cấu trúc phần 2. |

## 4. Ôn tập và bài tập thêm

### Câu hỏi ôn tập

1. Axios Instance giúp tránh lặp cấu hình như thế nào?
2. Khi interceptor trả `response.data`, nơi gọi service nhận kết quả dạng nào?
3. Vì sao cần chuyển tiếp lỗi và truyền `signal` xuống service?

### Bài tập mở rộng

1. Tạo component chi tiết dùng `getProductById(1, { signal })`, hiển thị tên, giá và mô tả. Thêm trạng thái tải, lỗi và cleanup tương tự danh sách.

## Tài liệu tham khảo

- [Axios: Tạo instance](https://axios-http.com/docs/instance).
- [Axios: Interceptors](https://axios-http.com/docs/interceptors).
- [Axios: Hủy request](https://axios-http.com/docs/cancellation).
- [DummyJSON: API sản phẩm](https://dummyjson.com/docs/products).

[Bài 5: Ghi nhớ và tham chiếu](./lesson5.md) | [Bài 7: Styling](./lesson7.md) | [Quay về roadmap](./README.md)
