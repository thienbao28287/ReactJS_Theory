# Bài 11: Chia sẻ state bằng Context và useReducer

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn chia sẻ trạng thái đăng nhập mô phỏng giữa các component mà không truyền props qua từng lớp. Bạn sẽ tạo Context, dùng reducer xử lý đăng nhập/đăng xuất và đọc dữ liệu bằng một custom Hook.

### Kiến thức cần có và chuẩn bị

Bạn cần biết props ở bài 2, `useReducer` ở bài 4 và custom Hooks ở bài 8. Mở project Vite, chạy `npm run dev`. Không cần cài package mới. Giữ `src/main.jsx` render `<App />`; ví dụ chính chưa dùng router.

### Kết quả sau bài học

- Nhận biết prop drilling và khi nào Context có ích.
- Dùng `createContext`, Provider và `useContext`.
- Kết hợp Context với reducer mà không sửa state cũ.
- Phân biệt trạng thái UI đăng nhập với xác thực và phân quyền tại backend.

## 1. Khi nào cần Context?

Giả sử App giữ `user`, Header cần tên người dùng và Profile cũng cần người dùng đó. Nếu các component trung gian không dùng dữ liệu nhưng phải nhận và truyền tiếp props, ta có **prop drilling**.

Truyền props vẫn rõ ràng và phù hợp khi dữ liệu chỉ đi qua một vài lớp. Có thể đưa state lên component cha chung hoặc dùng `children` trước khi thêm Context. Context hữu ích cho dữ liệu nhiều nhánh cùng cần như theme hoặc phiên đăng nhập.

| Thành phần | Trách nhiệm |
| --- | --- |
| Context | Kênh truyền giá trị qua cây component. |
| Provider | Cấp giá trị cho các component con nằm bên trong. |
| `useContext` | Đọc giá trị từ Provider gần nhất tương ứng. |
| Reducer | Nhận state/action và trả state mới. |

Context truyền dữ liệu; state vẫn do `useState` hoặc `useReducer` quản lý. Khi giá trị Provider đổi, các component đọc Context đó có thể render lại.

## 2. Tạo reducer và AuthProvider

### Bước 1 Chuẩn bị file

```text
src/
├── context/
│   ├── AuthContext.js
│   ├── AuthProvider.jsx
│   └── authReducer.js
├── hooks/
│   └── useAuth.js
└── App.jsx
```

Các file tách riêng giúp Provider chỉ export component và Hook ở module riêng. Không cần đổi `main.jsx`.

### Bước 2 Viết reducer thuần

Tạo `src/context/authReducer.js`:

```js
export const initialAuthState = { user: null };

export function authReducer(state, action) {
  switch (action.type) {
    case "auth/login":
      return { ...state, user: action.payload };
    case "auth/logout":
      return { ...state, user: null };
    default:
      throw new Error(`Action chưa được hỗ trợ: ${action.type}`);
  }
}
```

Reducer không gọi API, tạo timer hoặc ghi localStorage. Dữ liệu người dùng được chuẩn bị ở nơi xử lý sự kiện và truyền bằng `payload`. State mới là object mới; không gán `state.user = ...` trong reducer React thông thường.

### Bước 3 Tạo Context và Provider

Tạo `src/context/AuthContext.js`:

```js
import { createContext } from "react";

export const AuthContext = createContext(null);
```

Tạo `src/context/AuthProvider.jsx`:

```jsx
import { useReducer } from "react";
import { AuthContext } from "./AuthContext";
import { authReducer, initialAuthState } from "./authReducer";

export default function AuthProvider({ children }) {
  const [state, dispatch] = useReducer(authReducer, initialAuthState);
  return (
    <AuthContext.Provider value={{ state, dispatch }}>
      {children}
    </AuthContext.Provider>
  );
}
```

`null` là giá trị mặc định để nhận biết thiếu Provider. Mỗi AuthProvider là một vùng state độc lập. Đặt hai Provider quanh hai nhánh khác nhau sẽ không tạo một phiên chung.

### Bước 4 Tạo Hook đọc Context

Tạo `src/hooks/useAuth.js`:

```js
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === null) {
    throw new Error("useAuth cần được gọi bên trong AuthProvider.");
  }
  return context;
}
```

Kiểm tra này giúp lỗi cấu hình xuất hiện rõ ràng thay vì lỗi đọc thuộc tính của null. Đây là custom Hook gọi Context, không tự tạo bản sao state như `useToggle` ở bài 8.

## 3. Dùng cùng dữ liệu ở nhiều nhánh

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import AuthProvider from "./context/AuthProvider";
import { useAuth } from "./hooks/useAuth";

function Header() {
  const { state, dispatch } = useAuth();
  return (
    <header>
      <h1>Cửa hàng thử nghiệm</h1>
      <p>{state.user ? `Xin chào ${state.user.name}` : "Chưa đăng nhập"}</p>
      {state.user && (
        <button onClick={() => dispatch({ type: "auth/logout" })}>Đăng xuất</button>
      )}
    </header>
  );
}

function Profile() {
  const { state, dispatch } = useAuth();
  if (!state.user) {
    return (
      <section>
        <h2>Tài khoản</h2>
        <p>Đăng nhập dưới đây chỉ thay đổi state trong trình duyệt.</p>
        <button onClick={() => dispatch({
          type: "auth/login", payload: { id: 1, name: "Học viên", role: "customer" },
        })}>Đăng nhập mẫu</button>
      </section>
    );
  }
  return <section><h2>Hồ sơ</h2><p>Tên: {state.user.name}</p></section>;
}

function Content() {
  return <main><Profile /></main>;
}

export default function App() {
  return (
    <AuthProvider>
      <Header />
      <Content />
    </AuthProvider>
  );
}
```

Content không đọc `user` hoặc truyền props cho Profile. Header và Profile cùng đọc Provider phía trên chúng.

```text
Nhấn Đăng nhập mẫu
  → dispatch({ type: "auth/login", payload: user })
  → reducer trả state mới
  → Provider cấp giá trị mới
  → Header và Profile hiển thị cùng người dùng
```

## 4. Liên hệ với Protected Route

Trong ứng dụng Router ở bài 3, đặt một AuthProvider bao quanh các trang cần dùng phiên. Component bảo vệ đọc `state.user` bằng `useAuth`; nếu chưa có user thì trả `<Navigate to="/login" replace />`, nếu có thì trả `<Outlet />`.

Đây là hướng ghép vào ví dụ Router, không dán riêng hai JSX trên vào App hiện tại. Cần import Navigate/Outlet từ `react-router-dom`, đặt guard trong Route cha và giữ đúng một router. AuthProvider phải ở phía trên các component gọi `useAuth`; nếu Provider dùng Hook điều hướng thì chính nó cũng phải ở trong router.

Thông tin role trong state và protected route chỉ điều khiển giao diện. Backend vẫn phải xác thực request và kiểm tra quyền. Tải lại ví dụ hiện tại sẽ đăng xuất vì chưa khôi phục phiên từ server hoặc storage.

## 5. Kiểm tra kết quả và giới hạn

1. Lúc mới mở, Header và Profile đều ở trạng thái chưa đăng nhập.
2. Nhấn Đăng nhập mẫu: cả hai cùng có tên Học viên.
3. Nhấn Đăng xuất ở Header: Profile quay lại nút đăng nhập.
4. Tải lại trang sau khi đăng nhập: state được khởi tạo lại.
5. Tạm bỏ AuthProvider khỏi App: Hook phải báo lỗi có nội dung rõ ràng; sau đó khôi phục Provider.

Object `value={{ state, dispatch }}` được tạo lại khi Provider render. Với màn hình nhỏ này chưa cần tối ưu thêm. Khi đo thấy nhiều component render không cần thiết, cân nhắc tách Context đọc state/dispatch hoặc chia Context theo phạm vi; không thêm `useMemo` chỉ để che thiết kế state quá rộng.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Hook báo thiếu Provider | Đặt Provider phía trên component đang đọc Context. |
| Hai nơi không cùng phiên | Kiểm tra có hai AuthProvider độc lập không. |
| Reducer chạy nhưng UI không đổi | Trả object mới, kiểm tra action type và payload. |
| Đăng nhập mất khi refresh | Ví dụ chỉ lưu trong bộ nhớ; chưa có cơ chế khôi phục phiên. |

## 7. Ôn tập và bài tập thêm

1. Context có tự tạo state không? Reducer làm nhiệm vụ gì?
2. Vì sao `useAuth` chia sẻ dữ liệu còn hai lần gọi `useToggle` có state riêng?
3. Thêm action đổi tên người dùng và kiểm tra Header/Profile cùng cập nhật.
4. Tạo ThemeContext riêng có sáng/tối; không gộp theme vào reducer auth.
5. Ghép AuthProvider vào protected route bài 3, kiểm tra đăng xuất rồi mở lại trang được bảo vệ.

## Tài liệu tham khảo

- [React: Truyền dữ liệu bằng Context](https://react.dev/learn/passing-data-deeply-with-context).
- [React: Kết hợp reducer và Context](https://react.dev/learn/scaling-up-with-reducer-and-context).

[Bài 10: Zod](./lesson10.md) | [Bài 12: Redux Toolkit](./lesson12.md) | [Quay về roadmap](./README.md)
