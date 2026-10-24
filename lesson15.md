# Bài 15: Xây dựng base project và làm việc với Gitflow

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn tạo nền cho một ứng dụng có nhiều màn hình, đặt file đúng trách nhiệm và làm một task bằng nhánh Git. Bạn sẽ ghép Router, Provider, HTTP client và trang sản phẩm vào một base có thể tiếp tục phát triển.

### Kiến thức cần có và chuẩn bị

Bạn cần hiểu Router ở bài 3, Redux ở bài 12 và biến môi trường ở bài 14. Tạo project mới để không làm mất các ví dụ trước. Các lệnh sau chạy lần lượt trong terminal:

```bash
npm create vite@latest react-shop -- --template react
cd react-shop
npm install
npm install react-router-dom@6 axios @reduxjs/toolkit@2 react-redux@9
```

Không chạy `git init` trong thư mục kho tài liệu này chỉ để làm bài. Khi thực hành Git, đứng trong project `react-shop` riêng và kiểm tra thư mục hiện tại trước mỗi thao tác.

### Kết quả sau bài học

- Tổ chức base theo phạm vi dùng chung và theo feature.
- Ghép các Provider tại một vị trí rõ ràng, dùng đúng một router.
- Tạo trang danh sách và trang chi tiết kết nối service.
- Làm task bằng branch, commit, push, Pull Request và xử lý conflict.

## 1. Phân chia trách nhiệm trước khi tạo folder

Không cần tạo hàng chục thư mục rỗng cho một app nhỏ. Bắt đầu từ file thực sự sử dụng, rồi thêm khi có nhu cầu.

| Nơi đặt | Trách nhiệm |
| --- | --- |
| `app/` | Store và các Provider toàn ứng dụng. |
| `assets/` | Ảnh, icon, font được import và xử lý bởi bundler. |
| `components/ui/` | Button/Input dùng lại, nhận dữ liệu qua props. |
| `components/layout/` | Khung Header/Footer/Outlet. |
| `features/` | Component, slice, selector gắn với một nghiệp vụ. |
| `hooks/` | Hook dùng chung, không lắp ráp giao diện. |
| `pages/` | Màn hình theo URL, ghép component và đọc tham số. |
| `routes/` | Khai báo route. |
| `services/` | HTTP client, endpoint và hàm gọi API. |
| `constants/`, `utils/`, `styles/` | Hằng số, hàm thuần và style chung khi cần. |

File trong `public/` được truy cập theo URL tĩnh; file trong `src/assets/` thường được import để Vite xử lý. Không đặt logic API vào assets. Page lắp ráp màn hình; không đưa mọi hàm của ứng dụng vào App.jsx.

## 2. Tạo base có thể chạy

### Bước 1 Tạo cấu hình môi trường

Tạo `.env` và `.env.example` tại root project, cùng nội dung mẫu công khai:

```dotenv
VITE_API_BASE_URL=https://dummyjson.com
```

Thêm `.env` và `.env.*` vào `.gitignore`, rồi thêm `!.env.example` để giữ file mẫu. Giữ các dòng bỏ qua `node_modules` và `dist` của template. Biến môi trường frontend không dùng để giữ secret.

### Bước 2 Tạo HTTP client và service

Tạo `src/services/apiClient.js`:

```js
import axios from "axios";

const baseURL = import.meta.env.VITE_API_BASE_URL;
if (!baseURL) throw new Error("Thiếu VITE_API_BASE_URL.");

export const apiClient = axios.create({ baseURL, timeout: 8000 });
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => Promise.reject(error),
);
```

Tạo `src/services/productService.js`:

```js
import { apiClient } from "./apiClient";

export const productService = {
  async getPage({ signal } = {}) {
    const data = await apiClient.get("/products", { params: { limit: 8 }, signal });
    if (!Array.isArray(data.products)) throw new Error("Danh sách không hợp lệ.");
    return data.products;
  },
  async getById(id, { signal } = {}) {
    const data = await apiClient.get(`/products/${encodeURIComponent(id)}`, { signal });
    if (typeof data.id !== "number" || typeof data.title !== "string") {
      throw new Error("Sản phẩm không hợp lệ.");
    }
    return data;
  },
};
```

### Bước 3 Tạo store và Provider

Để base đã có một feature state đơn giản, tạo `src/features/cart/cartSlice.js`:

```js
import { createSlice } from "@reduxjs/toolkit";

const cartSlice = createSlice({
  name: "cart",
  initialState: { items: [] },
  reducers: {
    addItem(state, action) {
      const product = action.payload;
      const item = state.items.find((row) => row.id === product.id);
      if (item) item.quantity += 1;
      else state.items.push({
        id: product.id, title: product.title, price: product.price, quantity: 1,
      });
    },
    clearCart(state) { state.items = []; },
  },
});

export const { addItem, clearCart } = cartSlice.actions;
export const selectCartCount = (state) =>
  state.cart.items.reduce((sum, item) => sum + item.quantity, 0);
export default cartSlice.reducer;
```

Đây là slice tối thiểu cho base mới; các action tăng/giảm/xóa riêng ở bài 12 là bài tập ghép tiếp. Không lấy catalog giá VND ở bài 12 ghép với sản phẩm API giá USD vào cùng giỏ nếu chưa có quy tắc tiền tệ.

Tạo `src/app/store.js`:

```js
import { configureStore } from "@reduxjs/toolkit";
import cartReducer from "../features/cart/cartSlice";

export const store = configureStore({ reducer: { cart: cartReducer } });
```

Tạo `src/app/AppProviders.jsx`:

```jsx
import { Provider } from "react-redux";
import { BrowserRouter } from "react-router-dom";
import { store } from "./store";

export default function AppProviders({ children }) {
  return (
    <Provider store={store}>
      <BrowserRouter>{children}</BrowserRouter>
    </Provider>
  );
}
```

### Bước 4 Tạo layout

Tạo `src/components/layout/MainLayout.jsx`:

```jsx
import { Link, Outlet } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { clearCart, selectCartCount } from "../../features/cart/cartSlice";

export default function MainLayout() {
  const count = useSelector(selectCartCount);
  const dispatch = useDispatch();
  return (
    <>
      <header>
        <nav><Link to="/">Trang chủ</Link>{" | "}<Link to="/products">Sản phẩm</Link></nav>
        <p>Giỏ hàng: {count} sản phẩm</p>
        <button disabled={count === 0} onClick={() => dispatch(clearCart())}>Xóa giỏ</button>
      </header>
      <main><Outlet /></main>
      <footer>React Shop thực hành</footer>
    </>
  );
}
```

### Bước 5 Tạo trang danh sách và chi tiết

Tạo `src/pages/ProductsPage.jsx`:

```jsx
import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import { productService } from "../services/productService";
import { addItem } from "../features/cart/cartSlice";

export default function ProductsPage() {
  const [view, setView] = useState({ products: [], loading: true, error: "" });
  const dispatch = useDispatch();
  useEffect(() => {
    const controller = new AbortController();
    let active = true;
    productService.getPage({ signal: controller.signal })
      .then((products) => {
        if (active) setView({ products, loading: false, error: "" });
      })
      .catch((error) => {
        if (!active || axios.isCancel(error)) return;
        setView({ products: [], loading: false, error: "Không tải được sản phẩm." });
      });
    return () => { active = false; controller.abort(); };
  }, []);

  if (view.loading) return <p role="status">Đang tải...</p>;
  if (view.error) return <p role="alert">{view.error}</p>;
  return (
    <section>
      <h1>Sản phẩm</h1>
      {view.products.length === 0 ? <p>Chưa có sản phẩm.</p> : (
        <ul>{view.products.map((product) => (
          <li key={product.id}>
            <Link to={`/products/${product.id}`}>{product.title}</Link>
            <span> - {product.price} USD </span>
            <button onClick={() => dispatch(addItem(product))}>Thêm {product.title}</button>
          </li>
        ))}</ul>
      )}
    </section>
  );
}
```

Tạo `src/pages/ProductDetailPage.jsx`:

```jsx
import axios from "axios";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { productService } from "../services/productService";

export default function ProductDetailPage() {
  const { id } = useParams();
  const [view, setView] = useState({ id: null, product: null, error: "" });

  useEffect(() => {
    const controller = new AbortController();
    let active = true;
    async function load() {
      try {
        if (!/^\d+$/.test(id)) throw new Error("ID không hợp lệ.");
        const product = await productService.getById(id, { signal: controller.signal });
        if (active) setView({ id, product, error: "" });
      } catch (error) {
        if (!active || axios.isCancel(error)) return;
        const message = error.response?.status === 404 ? "Không tìm thấy sản phẩm." : "Không tải được sản phẩm. Kiểm tra ID hoặc kết nối.";
        setView({ id, product: null, error: message });
      }
    }
    load();
    return () => { active = false; controller.abort(); };
  }, [id]);

  if (view.id !== id) return <p role="status">Đang tải chi tiết...</p>;
  if (view.error) return <p role="alert">{view.error} <Link to="/products">Về danh sách</Link></p>;
  return (
    <article>
      <h1>{view.product.title}</h1>
      <p>{view.product.description}</p>
      <p>{view.product.price} USD</p>
      <Link to="/products">Về danh sách</Link>
    </article>
  );
}
```

`id` từ URL là chuỗi. Kiểm tra đầu vào trước khi gọi service và hủy request trước khi đổi ID. Lưu ID cùng kết quả giúp không gắn nội dung cũ dưới URL mới.

### Bước 6 Khai báo route và điểm khởi động

Tạo `src/routes/AppRoutes.jsx`:

```jsx
import { Link, Route, Routes } from "react-router-dom";
import MainLayout from "../components/layout/MainLayout";
import ProductsPage from "../pages/ProductsPage";
import ProductDetailPage from "../pages/ProductDetailPage";

export default function AppRoutes() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route index element={<><h1>React Shop</h1><Link to="/products">Xem sản phẩm</Link></>} />
        <Route path="products" element={<ProductsPage />} />
        <Route path="products/:id" element={<ProductDetailPage />} />
        <Route path="*" element={<h1>Không tìm thấy trang</h1>} />
      </Route>
    </Routes>
  );
}
```

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import AppRoutes from "./routes/AppRoutes";

export default function App() {
  return <AppRoutes />;
}
```

Thay toàn bộ `src/main.jsx` bằng:

```jsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import AppProviders from "./app/AppProviders";

createRoot(document.getElementById("root")).render(
  <StrictMode><AppProviders><App /></AppProviders></StrictMode>,
);
```

Không import CSS demo của template trong điểm khởi động này. Bạn có thể thêm file style riêng dựa trên bài 7 sau khi luồng chạy đúng. Khởi động `npm run dev`, kiểm tra trang chủ, danh sách, thêm vào giỏ và chi tiết. Tải trang `/products/1` trực tiếp trong dev server; kiểm tra một URL không tồn tại.

## 3. Làm một task bằng Gitflow

### Bước 1 Khởi tạo kho của project riêng

Nếu project `react-shop` chưa có repository, chạy trong chính thư mục đó:

```bash
git init -b main
git status
git add .
git diff --cached
git commit -m "chore: initialize react shop"
git switch -c develop
git switch -c feature/project-base
```

Kiểm tra diff staged không có `.env`, `node_modules` hoặc `dist` trước khi commit. Nếu đã có repository/branch, dùng trạng thái hiện tại và bỏ lệnh tạo trùng. Máy cần cấu hình tên/email Git của chính người học để commit.

### Bước 2 Hiểu các nhánh

| Nhánh | Mục đích trong quy trình mẫu |
| --- | --- |
| `main` | Bản ổn định có thể triển khai. |
| `develop` | Tích hợp tính năng trước khi phát hành. |
| `feature/...` | Một tính năng, thường tách từ develop. |
| `fix/...` | Sửa lỗi thông thường. |
| `hotfix/...` | Sửa gấp từ main, sau đó đồng bộ về develop. |

Đây là quy trình tham khảo; nhóm nhỏ có thể dùng mô hình đơn giản hơn. Thống nhất nhánh đích trước khi mở PR.

### Bước 3 Commit, push và mở PR

Thực hiện một thay đổi mới, ví dụ thêm trạng thái hết hàng trên feature branch, rồi chạy:

```bash
git status
git diff
git add .
git diff --cached
git commit -m "feat: show product stock status"
```

Tạo repository riêng trên GitHub và kết nối remote bằng URL thật của bạn. Kiểm tra `git remote -v` trước khi thêm; không ghi đè remote hiện có. Sau khi đã có remote `origin`, đẩy các nhánh cần dùng:

```bash
git push -u origin main
git push -u origin develop
git push -u origin feature/project-base
```

Mở PR từ `feature/project-base` vào `develop`. Mô tả thay đổi, ảnh UI khi cần, các bước kiểm tra và giới hạn còn lại. Review diff, sửa phản hồi, chạy kiểm tra rồi mới merge. Trước task tiếp theo, về develop và cập nhật code mới trước khi tạo branch.

## 4. Xử lý conflict

Khi feature branch cần nhận thay đổi mới từ develop:

```bash
git switch feature/project-base
git fetch origin
git merge origin/develop
```

Nếu có conflict, mở file được báo và tìm marker `<<<<<<<`, `=======`, `>>>>>>>`. Đọc cả hai thay đổi, chọn hoặc ghép nội dung đúng, xóa marker rồi kiểm tra ứng dụng. Không chọn toàn bộ một bên chỉ để hết thông báo.

Sau khi giải quyết:

```bash
git status
git add .
git diff --cached
git commit -m "fix: resolve project base merge conflict"
```

Nếu chưa hiểu conflict và muốn hủy lượt merge đang diễn ra, có thể dùng `git merge --abort`; đọc `git status` trước để xác định đúng trạng thái. Không dùng reset hard để xử lý theo thói quen.

## 5. Kiểm tra và tài liệu hóa

1. Chạy `npm run build` để phát hiện lỗi import và build.
2. Chạy `npm run lint` nếu script có trong template; sửa lỗi trước khi gửi review.
3. Dùng Network Offline để thử lỗi ở danh sách và chi tiết; trở lại Online rồi tải trang.
4. Kiểm tra giỏ tăng ở Header khi thêm từ danh sách, chuyển trang vẫn giữ trong phiên hiện tại.
5. Viết README cho `react-shop`: cách cài/chạy/build, biến môi trường, cấu trúc folder, API dùng và giới hạn giỏ trong bộ nhớ.
6. Dùng `git status` và `git diff --cached` để biết chính xác file sẽ được commit.

## 6. Ôn tập và bài tập thêm

1. Vì sao MainLayout cần Outlet và App không bọc thêm BrowserRouter?
2. Component dùng chung khác component chỉ thuộc một feature ở đâu?
3. Thêm trang giỏ và các action tăng/giảm/xóa từ bài 12; định dạng toàn bộ giá API bằng USD.
4. Mở PR cho một thay đổi nhỏ, nhờ người cùng học review và sửa theo phản hồi.
5. Mô phỏng conflict bằng hai nhánh sửa cùng dòng tiêu đề; giải quyết trên repository thực hành riêng.

## Tài liệu tham khảo

- [Vite: Khởi tạo project](https://vite.dev/guide/).
- [Git: Branching và merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
- [GitHub: Tạo Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

[Bài 14: Làm việc với backend](./lesson14.md) | [Bài 16: Build và triển khai](./lesson16.md) | [Quay về roadmap](./README.md)
