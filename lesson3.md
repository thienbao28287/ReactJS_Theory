# Bài 3: React Router trong ReactJS

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn xây dựng ứng dụng có nhiều màn hình bằng React Router. Bạn sẽ bắt đầu với hai trang đơn giản, tìm hiểu các kiểu route, rồi thực hành ứng dụng có đăng nhập mô phỏng. Phần tiếp theo chuyển sang Data Router để tải dữ liệu và hiển thị trạng thái tải hoặc lỗi.

### Kiến thức cần có và chuẩn bị

Bạn cần biết component, JSX, props và state trong hai bài đầu. Mở project Vite và xác định `src/App.jsx` là file dùng cho các ví dụ. **Route** là quy tắc ghép một đường dẫn với giao diện; **router** quản lý các quy tắc này và việc điều hướng.

Giữ `src/main.jsx` render `<App />`. Mọi router trong bài được khai báo trong `App.jsx`, vì vậy không bọc thêm router ở `main.jsx`. Khi thử URL, giữ nguyên phần địa chỉ Local mà Vite in ra, chỉ thay đường dẫn phía sau; ví dụ từ trang chủ sang `/user/12`.

### Kết quả sau bài học

- Cài và thiết lập React Router v6, điều hướng bằng liên kết hoặc code.
- Đọc tham số đường dẫn, query và hiển thị route con.
- Chuyển hướng người chưa đăng nhập và xử lý đường dẫn chưa khai báo.
- Dùng Data Router để tải dữ liệu trước khi hiển thị trang đích.

## 1. React Router DOM là gì?

**React Router DOM** giúp xử lý routing trong ứng dụng React chạy trên trình duyệt. Routing là việc xác định giao diện cần hiển thị dựa trên URL.

Ví dụ:

| URL                        | Giao diện                             |
| -------------------------- | ------------------------------------- |
| `/`                        | Trang chủ.                            |
| `/about`                   | Giới thiệu.                           |
| `/user/12`                 | Thông tin người dùng có ID là `12`.   |
| `/dashboard/profile`       | Hồ sơ bên trong dashboard.            |
| `/products?category=phone` | Danh sách sản phẩm lọc theo danh mục. |

Khi điều hướng nội bộ bằng React Router, ứng dụng có thể thay đổi URL và nội dung hiển thị mà không tải lại toàn bộ tài liệu HTML. Đây là cách triển khai SPA đã giới thiệu trong bài 1.

## 2. Cài đặt và thiết lập router

### Bước 1 Cài thư viện

Mở terminal trong thư mục project React và chạy:

```bash
npm install react-router-dom@6
npm run dev
```

Bài học dùng **React Router v6**; Data Router có từ v6.4. Lệnh trên cài phiên bản thuộc nhánh v6 để thống nhất các ví dụ. Không dùng cú pháp v5 như `Switch` hoặc `component={Home}` cho các ví dụ dưới đây.

### Bước 2 Tạo hai trang và khai báo route

Thay toàn bộ nội dung `src/App.jsx` bằng:

```jsx
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";

function Home() {
  return <h1>Trang chủ</h1>;
}

function About() {
  return <h1>Giới thiệu</h1>;
}

export default function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Trang chủ</Link>
        {" | "}
        <Link to="/about">Giới thiệu</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}
```

| Thành phần      | Vai trò                                                                |
| --------------- | ---------------------------------------------------------------------- |
| `BrowserRouter` | Cung cấp ngữ cảnh routing, đồng bộ điều hướng với lịch sử trình duyệt. |
| `Routes`        | Chọn nhánh route phù hợp với URL hiện tại.                             |
| `Route`         | Khai báo đường dẫn và giao diện tương ứng.                             |
| `path`          | Mẫu đường dẫn cần khớp.                                                |
| `element`       | Phần tử React hiển thị khi route khớp.                                 |

Trong bài này, router nằm trong `App.jsx`. Giữ `src/main.jsx` render `<App />` như template Vite; không bọc thêm `BrowserRouter` ở đó. Mỗi ứng dụng chỉ dùng một router gốc.

### Bước 3 Kiểm tra điều hướng

Lưu file, mở địa chỉ Local rồi nhấn Giới thiệu. URL chuyển sang `/about`, nội dung đổi thành Giới thiệu và menu vẫn hiển thị. Nhấn nút Back của trình duyệt để quay về trang chủ.

`nav` nằm ngoài `Routes` nên được giữ trên cả hai trang; phần trong `Routes` thay đổi theo URL. Các đoạn ở phần 3 đến 7 dưới đây là **minh họa từng API**, chưa phải ứng dụng độc lập. Bạn có thể đọc trước rồi chạy bản hoàn chỉnh ở phần 8 mà không phải tự ghép code.

## 3. Điều hướng bằng Link và useNavigate

### Link

`Link` tạo liên kết điều hướng nội bộ:

```jsx
<Link to="/about">Giới thiệu</Link>
```

Với menu nội bộ, ưu tiên `Link` để React Router xử lý chuyển trang. Thẻ `<a href="...">` vẫn phù hợp cho liên kết bên ngoài hoặc khi chủ động muốn điều hướng bằng tải tài liệu mới.

### useNavigate

`useNavigate` trả về hàm điều hướng bằng code, phù hợp khi chuyển trang sau một thao tác:

```jsx
import { useNavigate } from "react-router-dom";

function GoToAbout() {
  const navigate = useNavigate();

  return <button onClick={() => navigate("/about")}>Xem giới thiệu</button>;
}
```

Đặt `<GoToAbout />` bên trong cây component được router bao bọc. Không gọi `navigate('/about')` trực tiếp trong thân component khi render; ví dụ trên gọi trong sự kiện click.

`navigate('/about', { replace: true })` thay thế mục hiện tại trong lịch sử. `navigate(-1)` quay lại mục trước nếu có; với một nút có đích đến xác định, dùng đường dẫn cụ thể sẽ dễ dự đoán hơn.

## 4. Route động và useParams

**Dynamic route** chứa đoạn đường dẫn thay đổi, khai báo bằng dấu `:`:

```jsx
<Route path="/user/:id" element={<User />} />
```

Component đọc tham số bằng `useParams`:

```jsx
import { useParams } from "react-router-dom";

function User() {
  const { id } = useParams();

  return <h1>Người dùng có ID là {id}</h1>;
}
```

Với URL `/user/12`, `id` là chuỗi `'12'`. Nếu cần tính toán bằng số, hãy chuyển kiểu và kiểm tra tính hợp lệ. Route động chỉ khớp mẫu URL; nó không tự kiểm tra người dùng đó có tồn tại trong dữ liệu hay không.

## 5. Nested Routes và Outlet

**Nested routes** là các route lồng nhau. Component cha giữ phần giao diện chung, còn component con thay đổi theo URL:

```jsx
<Route path="/dashboard" element={<Dashboard />}>
  <Route index element={<DashboardHome />} />
  <Route path="profile" element={<Profile />} />
  <Route path="settings" element={<Settings />} />
</Route>
```

| Route con  | URL                   |
| ---------- | --------------------- |
| `index`    | `/dashboard`          |
| `profile`  | `/dashboard/profile`  |
| `settings` | `/dashboard/settings` |

Đường dẫn con tương đối được ghép với đường dẫn cha. Route `index` là nội dung mặc định khi URL khớp chính route cha.

Cha cần đặt **`Outlet`** ở vị trí muốn hiển thị route con:

```jsx
import { Link, Outlet } from "react-router-dom";

function Dashboard() {
  return (
    <section>
      <h1>Dashboard</h1>
      <nav>
        <Link to="profile">Hồ sơ</Link>
        {" | "}
        <Link to="settings">Cài đặt</Link>
      </nav>
      <Outlet />
    </section>
  );
}
```

Trong ví dụ, các `Link` được render tại route cha `/dashboard`, nên `to="profile"` dẫn tới `/dashboard/profile`. Nếu quên `Outlet`, giao diện route con không có chỗ để hiển thị.

## 6. Protected Route

**Protected route** kiểm tra điều kiện trước khi hiển thị trang, chẳng hạn trạng thái đăng nhập:

```jsx
import { Navigate } from "react-router-dom";

function ProtectedRoute({ isAuthenticated, children }) {
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

Dùng component này trong khai báo route:

```jsx
<Route
  path="/dashboard"
  element={
    <ProtectedRoute isAuthenticated={isAuthenticated}>
      <Dashboard />
    </ProtectedRoute>
  }
/>
```

`Navigate` chuyển hướng khi được render; `useNavigate` phù hợp cho điều hướng trong hàm xử lý. Prop `replace` giúp thay mục bị chặn trong lịch sử bằng trang đăng nhập.

Đây là kiểm soát giao diện phía trình duyệt. Với ứng dụng thật, máy chủ vẫn phải xác thực và kiểm tra quyền cho các API; ẩn một trang ở frontend không bảo vệ được dữ liệu phía server.

## 7. Trang 404, query params và useLocation

### Trang không tìm thấy

Dùng `*` để xử lý các đường dẫn chưa được khai báo:

```jsx
<Route path="*" element={<NotFound />} />
```

`NotFound` là component do bạn tạo. Đây là trang 404 phía giao diện; nó không tự đặt mã HTTP 404 cho tài liệu HTML do máy chủ gửi về.

### Query params

Query params nằm sau dấu `?`, ví dụ `/products?category=phone`. Dùng `useSearchParams` để đọc và cập nhật:

```jsx
import { useSearchParams } from "react-router-dom";

function Products() {
  const [searchParams, setSearchParams] = useSearchParams();
  const category = searchParams.get("category") ?? "all";

  function changeCategory(value) {
    const nextParams = new URLSearchParams(searchParams);
    if (value === "all") {
      nextParams.delete("category");
    } else {
      nextParams.set("category", value);
    }
    setSearchParams(nextParams);
  }

  return (
    <section>
      <h1>Sản phẩm</h1>
      <label>
        Danh mục
        <select
          value={category}
          onChange={(e) => changeCategory(e.target.value)}
        >
          <option value="all">Tất cả</option>
          <option value="phone">Điện thoại</option>
          <option value="laptop">Máy tính</option>
        </select>
      </label>
      <p>Danh mục đang chọn: {category}</p>
    </section>
  );
}
```

Ví dụ này minh họa bộ chọn và URL; chưa có dữ liệu sản phẩm để lọc. Sao chép `searchParams` giúp giữ các query khác khi đổi danh mục; gọi setter mới thực hiện điều hướng tới query mới.

| Loại tham số | Ví dụ                      | Cách đọc                            |
| ------------ | -------------------------- | ----------------------------------- |
| Path param   | `/user/12`                 | `useParams()` lấy `id`.             |
| Query param  | `/products?category=phone` | `useSearchParams()` lấy `category`. |

### useLocation

`useLocation` lấy đối tượng vị trí hiện tại của router:

```jsx
import { useLocation } from "react-router-dom";

function CurrentLocation() {
  const location = useLocation();

  return (
    <p>
      Vị trí: {location.pathname}
      {location.search}
      {location.hash}
    </p>
  );
}
```

Với `/products?category=phone#list`, `pathname` là `/products`, `search` là `?category=phone`, còn `hash` là `#list`. `location` không phải toàn bộ URL bao gồm giao thức và tên miền.

## 8. Thực hành routing cơ bản

### Bước 1 Chạy ứng dụng hoàn chỉnh

Thay toàn bộ `src/App.jsx` bằng code dưới đây. Ví dụ đã có đủ import, component và cấu hình route; không cần chép thêm các đoạn ở phần trước.

```jsx
import { useState } from "react";
import {
  BrowserRouter,
  Link,
  Navigate,
  Outlet,
  Route,
  Routes,
  useLocation,
  useNavigate,
  useParams,
  useSearchParams,
} from "react-router-dom";

function User() {
  const { id } = useParams();

  return <h1>Người dùng có ID là {id}</h1>;
}

function Dashboard() {
  return (
    <section>
      <h1>Dashboard</h1>
      <nav>
        <Link to="profile">Hồ sơ</Link>
        {" | "}
        <Link to="settings">Cài đặt</Link>
      </nav>
      <Outlet />
    </section>
  );
}

function ProtectedRoute({ isAuthenticated, children }) {
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return children;
}

function Products() {
  const [searchParams, setSearchParams] = useSearchParams();
  const category = searchParams.get("category") ?? "all";

  function changeCategory(value) {
    const nextParams = new URLSearchParams(searchParams);
    if (value === "all") {
      nextParams.delete("category");
    } else {
      nextParams.set("category", value);
    }
    setSearchParams(nextParams);
  }

  return (
    <section>
      <h1>Sản phẩm</h1>
      <label>
        Danh mục
        <select
          value={category}
          onChange={(e) => changeCategory(e.target.value)}
        >
          <option value="all">Tất cả</option>
          <option value="phone">Điện thoại</option>
          <option value="laptop">Máy tính</option>
        </select>
      </label>
      <p>Danh mục đang chọn: {category}</p>
    </section>
  );
}

function CurrentLocation() {
  const location = useLocation();

  return (
    <p>
      Vị trí: {location.pathname}
      {location.search}
      {location.hash}
    </p>
  );
}

function Home() {
  return <h1>Trang chủ</h1>;
}

function DashboardHome() {
  return <p>Tổng quan dashboard</p>;
}

function Profile() {
  return <p>Hồ sơ của bạn</p>;
}

function Settings() {
  return <p>Cài đặt tài khoản</p>;
}

function NotFound() {
  return <h1>404 Không tìm thấy trang</h1>;
}

function Login({ onLogin }) {
  const navigate = useNavigate();

  function handleLogin() {
    onLogin();
    navigate("/dashboard", { replace: true });
  }

  return <button onClick={handleLogin}>Đăng nhập thử</button>;
}

export default function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Trang chủ</Link>
        {" | "}
        <Link to="/user/12">Người dùng 12</Link>
        {" | "}
        <Link to="/products?category=phone">Sản phẩm</Link>
        {" | "}
        <Link to="/dashboard">Dashboard</Link>
      </nav>
      {isAuthenticated && (
        <button onClick={() => setIsAuthenticated(false)}>Đăng xuất</button>
      )}
      <CurrentLocation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/user/:id" element={<User />} />
        <Route path="/products" element={<Products />} />
        <Route
          path="/login"
          element={<Login onLogin={() => setIsAuthenticated(true)} />}
        />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute isAuthenticated={isAuthenticated}>
              <Dashboard />
            </ProtectedRoute>
          }
        >
          <Route index element={<DashboardHome />} />
          <Route path="profile" element={<Profile />} />
          <Route path="settings" element={<Settings />} />
        </Route>
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

Nút đăng nhập chỉ mô phỏng bằng state, không gửi thông tin đăng nhập tới server. Tải lại trang sẽ đưa trạng thái về chưa đăng nhập.

### Bước 2 Hiểu luồng đăng nhập và route con

`App` giữ state đăng nhập và truyền nó qua props cho `ProtectedRoute`. Khi state là `false`, route dashboard hiển thị `Navigate` để chuyển sang trang đăng nhập. Nhấn Đăng nhập thử cập nhật state ở cha và chuyển đến dashboard.

Khi đi tới `/dashboard/profile`, router chọn cả dashboard lẫn route con profile. `Dashboard` giữ tiêu đề và menu; `Outlet` được thay bằng nội dung của `Profile`. Đăng xuất đổi state về `false`, khiến route bảo vệ đánh giá lại điều kiện và chuyển hướng.

### Bước 3 Kiểm tra kết quả

1. Mở `/user/12`: giao diện hiển thị ID `12`.
2. Mở `/products?category=phone`, đổi danh mục và kiểm tra query thay đổi.
3. Khi chưa đăng nhập, mở `/dashboard`: ứng dụng chuyển tới `/login`.
4. Nhấn Đăng nhập thử: dashboard xuất hiện; chọn Hồ sơ và Cài đặt để xem route con.
5. Nhấn Đăng xuất khi đang ở dashboard: quay về trang đăng nhập.
6. Mở `/khong-ton-tai`: hiển thị trang 404.

## 9. Data Router với createBrowserRouter

Phần trước khai báo route bằng `BrowserRouter`, `Routes` và `Route`. **Data Router** có từ v6.4 cho phép khai báo route bằng object và gắn thêm `loader`, `errorElement` cùng các tính năng xử lý dữ liệu.

| Cách thiết lập | Thành phần chính                        | Dùng trong bài                               |
| -------------- | --------------------------------------- | -------------------------------------------- |
| Routing cơ bản | `BrowserRouter`, `Routes`, `Route`      | Điều hướng và hiển thị component.            |
| Data Router    | `createBrowserRouter`, `RouterProvider` | Điều hướng kết hợp tải dữ liệu và xử lý lỗi. |

Đây là hai cách thiết lập khác nhau, không phải cứ dùng object là đang dùng một phiên bản thư viện khác. Với ví dụ tiếp theo, **thay toàn bộ `src/App.jsx`**; không bọc `RouterProvider` trong `BrowserRouter` và không giữ router cũ ở `main.jsx`.

### Bước 1 Chuẩn bị dữ liệu cho loader

`loader` tải dữ liệu cho route trước khi giao diện đích được hiển thị với dữ liệu đó. Component đọc kết quả bằng `useLoaderData`. Khác với việc bắt đầu fetch trong `useEffect` sau khi component đã render, loader gắn việc tải dữ liệu vào quá trình điều hướng của router.

Tạo file `public/users.json` để có nguồn dữ liệu chạy tại chỗ:

```json
[
  { "id": 1, "name": "Nguyễn An" },
  { "id": 2, "name": "Trần Bình" }
]
```

### Bước 2 Chuyển sang Data Router

Thay toàn bộ nội dung `src/App.jsx` bằng ví dụ đầy đủ sau:

```jsx
import {
  createBrowserRouter,
  isRouteErrorResponse,
  Link,
  Outlet,
  RouterProvider,
  useLoaderData,
  useNavigation,
  useRouteError,
} from "react-router-dom";

async function usersLoader({ request }) {
  const response = await fetch("/users.json", { signal: request.signal });

  if (!response.ok) {
    throw new Response("Không tải được danh sách người dùng.", {
      status: response.status,
    });
  }

  return response.json();
}

function Layout() {
  const navigation = useNavigation();
  const isLoading = navigation.state === "loading";

  return (
    <main>
      <nav>
        <Link to="/">Trang chủ</Link>
        {" | "}
        <Link to="/users">Người dùng</Link>
      </nav>
      {isLoading && <p role="status">Đang tải dữ liệu...</p>}
      <Outlet />
    </main>
  );
}

function Home() {
  return <h1>Thực hành Data Router</h1>;
}

function Users() {
  const users = useLoaderData();

  return (
    <section>
      <h1>Danh sách người dùng</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </section>
  );
}

function ErrorPage() {
  const error = useRouteError();
  const message = isRouteErrorResponse(error)
    ? `Lỗi ${error.status}: ${error.data}`
    : "Đã xảy ra lỗi khi tải hoặc hiển thị dữ liệu.";

  return (
    <section role="alert">
      <h1>Không thể hiển thị trang</h1>
      <p>{message}</p>
      <Link to="/">Về trang chủ</Link>
    </section>
  );
}

function NotFound() {
  return <h1>404 Không tìm thấy trang</h1>;
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <Home /> },
      {
        path: "users",
        element: <Users />,
        loader: usersLoader,
        errorElement: <ErrorPage />,
      },
      { path: "*", element: <NotFound /> },
    ],
  },
]);

export default function App() {
  return (
    <RouterProvider
      router={router}
      fallbackElement={<p role="status">Đang khởi tạo trang...</p>}
    />
  );
}
```

### Bước 3 Theo dõi luồng tải dữ liệu

Từ trang chủ, nhấn Người dùng. Router xác định route `/users` và gọi `usersLoader`; hàm này fetch JSON rồi trả về dữ liệu đã đọc. Khi loader thành công, `Users` lấy dữ liệu bằng `useLoaderData` và dùng `map` tạo danh sách. Trong lúc chờ, layout vẫn có thể hiện thông báo tải.

Router được tạo bên ngoài component để không tạo lại mỗi lần `App` render. `/users.json` được phục vụ từ `public/users.json` trong project Vite chạy ở đường dẫn gốc. Có thể thay URL này bằng API thật khi đã có backend.

`request.signal` cho phép yêu cầu fetch bị hủy khi router hủy việc tải tương ứng. Loader đang giả định phản hồi JSON là mảng các object có `id` và `name`; với API thực tế, cần kiểm tra cấu trúc dữ liệu theo hợp đồng API.

## 10. Loading state và xử lý lỗi

### useNavigation

Trong Data Router, `useNavigation` theo dõi tiến trình điều hướng:

| Trạng thái   | Ý nghĩa                                                                  |
| ------------ | ------------------------------------------------------------------------ |
| `idle`       | Không có điều hướng đang chờ.                                            |
| `loading`    | Router đang tải dữ liệu cho điều hướng.                                  |
| `submitting` | Đang gửi dữ liệu qua cơ chế action của router; ví dụ hiện tại chưa dùng. |

Ở ví dụ trên, khi đi từ trang chủ sang `/users`, `Layout` hiển thị thông báo tải trong lúc chờ loader. Lần tải đầu khi mở trực tiếp `/users` dùng `fallbackElement` của `RouterProvider` trong cấu hình v6 này.

**Phân biệt:** `useNavigate` trả về hàm để chuyển trang; `useNavigation` trả về trạng thái tiến trình của Data Router. Không đặt `useNavigation` trong ví dụ chỉ dùng `BrowserRouter` ở phần trước.

### errorElement và useRouteError

`errorElement` khai báo giao diện thay thế khi route gặp lỗi trong loader, action hoặc quá trình render. `useRouteError` đọc lỗi tại giao diện đó. Nếu route không có `errorElement`, lỗi được chuyển lên boundary gần nhất của route cha.

`fetch` không tự ném lỗi chỉ vì phản hồi HTTP là 404 hoặc 500. Vì vậy, loader kiểm tra `response.ok` và chủ động ném `Response`. Lỗi mạng hoặc JSON không hợp lệ cũng có thể làm loader thất bại; nhánh thông báo chung trong `ErrorPage` xử lý các trường hợp này.

Trang `path="*"` xử lý URL chưa khớp route; `errorElement` xử lý lỗi xảy ra ở route. Hai phần này có mục đích khác nhau.

### Kiểm tra ví dụ Data Router

1. Từ `/`, nhấn Người dùng: kiểm tra danh sách có hai tên trong `users.json`.
2. Mở DevTools, chọn chế độ mạng chậm trong Network rồi chuyển lại từ `/` sang `/users` để quan sát trạng thái tải.
3. Để thử lỗi một cách chắc chắn, tạm thay phần thân `usersLoader` bằng `throw new Response('Lỗi thử nghiệm', { status: 500 });`, lưu file rồi điều hướng lại tới `/users`.
4. Kiểm tra giao diện lỗi vẫn nằm trong layout và có liên kết về trang chủ. Sau đó khôi phục loader ban đầu.
5. Mở URL chưa khai báo để kiểm tra trang 404.

## 11. Lỗi thường gặp và triển khai

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Hook điều hướng báo không ở trong router | Đặt component gọi Hook bên dưới router; xem lại các ví dụ hoàn chỉnh. |
| Báo router lồng trong router | Giữ một router gốc; kiểm tra cả `main.jsx` và `App.jsx`. |
| Chỉ hiện dashboard, không có trang con | Giữ `<Outlet />` trong component cha. |
| `useNavigation` không hoạt động | Dùng với Data Router ở phần 9, không dùng với ví dụ chỉ có `BrowserRouter`. |
| Fetch trả HTML hoặc lỗi JSON | Kiểm tra `public/users.json` và thử mở `/users.json` trên cùng địa chỉ Local. |
| Tải lại trang con gặp 404 trên hosting | Cấu hình fallback của máy chủ như hướng dẫn bên dưới. |


- Các Hook và component điều hướng phải nằm trong cây được router phù hợp bao bọc.
- Các đoạn code minh họa ở phần 3 đến 7 được tập hợp trong ví dụ hoàn chỉnh ở phần 8; ví dụ đầy đủ ở phần 9 thay thế ví dụ trước, không dán nối các `App` vào cùng một file.
- Khi dùng `BrowserRouter` hoặc `createBrowserRouter` trên hosting tĩnh, cấu hình máy chủ trả về `index.html` cho đường dẫn giao diện như `/dashboard/profile`. Nếu không, mở trực tiếp hoặc tải lại đường dẫn đó có thể gặp 404 từ server trước khi React chạy. Các file tĩnh và API cần được phục vụ đúng thay vì chuyển tất cả về HTML.
- Nếu triển khai ứng dụng dưới đường dẫn con, cần cấu hình đường dẫn gốc của Vite và `basename` của router phù hợp; các ví dụ trong bài chạy ở đường dẫn gốc.

## 12. Ôn tập và bài tập thêm

### Câu hỏi ôn tập

1. `BrowserRouter`, `Routes` và `Route` có vai trò gì?
2. Khi nào dùng `Link`, khi nào dùng `useNavigate`?
3. `useParams` khác `useSearchParams` như thế nào?
4. Vì sao route cha cần `Outlet`?
5. Protected route phía frontend có thay thế kiểm tra quyền tại server không?
6. `loader` trả dữ liệu cho component bằng cách nào?
7. `useNavigate` khác `useNavigation` ở điểm nào?
8. Vì sao loader cần kiểm tra `response.ok`?

### Bài tập mở rộng

1. Tách các trang trong phần thực hành thành file riêng trong `src/pages/`.
2. Thêm route `/user/:id` vào ví dụ Data Router; đọc `params.id` trong loader và tìm người dùng trong dữ liệu JSON.
3. Nếu không tìm thấy người dùng, ném `Response` có status `404` và hiển thị bằng `errorElement`.
4. Dùng `NavLink` để làm nổi bật mục menu đang được chọn.
5. Mở rộng bộ chọn danh mục thành danh sách sản phẩm được lọc dựa trên query params.

## Tài liệu tham khảo

- [React Router v6: Tổng quan tính năng](https://reactrouter.com/6.30.1/start/overview).
- [React Router v6: Loader](https://reactrouter.com/6.30.1/route/loader).
- [React Router v6: useNavigation](https://reactrouter.com/6.30.1/hooks/use-navigation).
- [React Router v6: Xử lý lỗi với errorElement](https://reactrouter.com/6.30.1/route/error-element).
- [React Router v6: useSearchParams](https://reactrouter.com/6.30.1/hooks/use-search-params).

[Bài 2: Props và State trong ReactJS](./lesson2.md) | [Bài 4: useEffect và useReducer →](./lesson4.md) | [Quay về roadmap](./README.md)
