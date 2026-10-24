# Bài 1: Nhập môn ReactJS

[← Quay về roadmap](./README.md)

Bài học tổng hợp 5 chủ đề trong tài liệu ReactJS được cung cấp: Component, SPA, DOM ảo, JSX và tạo project bằng Vite. Các ví dụ được bổ sung để bạn có thể thực hành.

## 1. Component

Trong ReactJS, **Component** là một thành phần giao diện độc lập, có thể tái sử dụng. Một component có thể chứa giao diện và logic xử lý liên quan đến phần giao diện đó.

Ví dụ: một trang web có thể được chia thành `Header`, `Sidebar`, `ProductCard` và `Footer`.

### Tạo và sử dụng component

Component thường là một hàm JavaScript trả về JSX. Thay nội dung `src/App.jsx` trong project React bằng đoạn sau:

```jsx
function Welcome() {
  return <h1>Chào mừng bạn đến với ReactJS!</h1>;
}

export default function App() {
  return (
    <main>
      <Welcome />
      <Welcome />
    </main>
  );
}
```

`Welcome` được khai báo một lần và dùng hai lần bằng thẻ `<Welcome />`. Tên component phải bắt đầu bằng chữ hoa để React phân biệt với các thẻ HTML như `<main>` hoặc `<h1>`.

### Vì sao sử dụng component?

| Lợi ích | Ý nghĩa |
| --- | --- |
| Chia nhỏ giao diện | Tách trang lớn thành các phần dễ hiểu. |
| Tái sử dụng | Dùng cùng một component tại nhiều vị trí. |
| Dễ bảo trì | Sửa định nghĩa component để cập nhật các nơi sử dụng. |
| Tổ chức logic | Mỗi component phụ trách một phần giao diện và hành vi liên quan. |

## 2. SPA

**SPA (Single Page Application)** là ứng dụng web tải tài liệu HTML ban đầu, sau đó dùng JavaScript để cập nhật nội dung khi người dùng tương tác hoặc chuyển màn hình, thay vì tải lại toàn bộ tài liệu HTML cho mỗi lần điều hướng trong ứng dụng.

| Website nhiều trang truyền thống | SPA |
| --- | --- |
| Chuyển trang thường yêu cầu một tài liệu HTML mới từ máy chủ. | Điều hướng nội bộ có thể được xử lý bằng JavaScript. |
| Trình duyệt thường tải lại toàn bộ trang. | Chỉ cập nhật giao diện cần hiển thị. |

Ví dụ: từ danh sách sản phẩm sang chi tiết sản phẩm, SPA có thể thay nội dung chính mà không tải lại toàn bộ trang. Ứng dụng vẫn có thể gửi yêu cầu lấy dữ liệu hoặc tải thêm mã JavaScript.

**Lưu ý về SEO:** SPA chỉ render phía trình duyệt có thể gặp khó khăn hơn với SEO nếu công cụ tìm kiếm không xử lý được nội dung JavaScript. Không phải mọi ứng dụng React đều có SEO kém; kết quả còn phụ thuộc cách triển khai, chẳng hạn render phía máy chủ hoặc tạo HTML tĩnh. React là thư viện giao diện, không bắt buộc ứng dụng phải là SPA.

## 3. DOM ảo

**DOM (Document Object Model)** là cách trình duyệt biểu diễn cấu trúc trang bằng các đối tượng. JavaScript có thể thay đổi DOM để cập nhật giao diện.

**DOM ảo (Virtual DOM)** là cách gọi phổ biến cho biểu diễn giao diện trong bộ nhớ mà React sử dụng khi tính toán cập nhật. Có thể hình dung quá trình như sau:

```text
Cập nhật state
  → React gọi component để tính giao diện mới (render)
  → Đối chiếu kết quả với lần trước
  → Áp dụng thay đổi cần thiết lên DOM thật (commit)
  → Trình duyệt vẽ lại màn hình
```

Ví dụ thực hành trong `src/App.jsx`:

```jsx
import { useState } from 'react';

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <main>
      <h1>Bộ đếm</h1>
      <p>Số lần bấm: {count}</p>
      <button onClick={() => setCount(count + 1)}>Tăng</button>
    </main>
  );
}
```

`useState` lưu giá trị bộ đếm. Khi bấm nút, `setCount` yêu cầu cập nhật state và React tính lại giao diện. Trong ví dụ này, React cập nhật phần văn bản của bộ đếm; không cần tạo lại toàn bộ trang.

Render không đồng nghĩa với thay đổi DOM: nếu kết quả không đổi, React có thể không cần sửa DOM. DOM ảo cũng không bảo đảm mọi ứng dụng luôn nhanh hơn thao tác DOM trực tiếp.

## 4. JSX là gì?

**JSX** là phần mở rộng cú pháp của JavaScript, cho phép viết giao diện có hình thức gần giống HTML ngay trong mã JavaScript. Công cụ như Vite xử lý JSX để trình duyệt có thể chạy ứng dụng.

Bạn có thể gán JSX cho biến:

```jsx
const element = <h1>Hello World!</h1>;
```

Hoặc trả về JSX từ component như các ví dụ phía trên.

### Các quy tắc và cách dùng cơ bản

**Bọc các phần tử liền kề trong một phần tử cha hoặc Fragment.** Fragment `<>...</>` nhóm các phần tử mà không tạo thêm thẻ bao ngoài trong DOM.

```jsx
function Introduction() {
  return (
    <>
      <h1>Học ReactJS</h1>
      <p>Bắt đầu từ component và JSX.</p>
    </>
  );
}
```

**Đóng đầy đủ các thẻ**, kể cả thẻ không có nội dung:

```jsx
const input = <input type="text" placeholder="Nhập tên của bạn" />;
```

**Chèn biểu thức JavaScript bằng `{}`.** Có thể hiển thị biến, phép tính, kết quả gọi hàm và biểu thức điều kiện:

```jsx
export default function App() {
  const name = 'An';
  const price = 50000;
  const quantity = 2;
  const isLoggedIn = true;

  return (
    <section>
      <h1>Xin chào, {name.toUpperCase()}!</h1>
      <p>Tổng tiền: {price * quantity} đồng</p>
      <p>{isLoggedIn ? 'Đã đăng nhập' : 'Chưa đăng nhập'}</p>
      {isLoggedIn && <button>Đăng xuất</button>}
    </section>
  );
}
```

Không viết trực tiếp câu lệnh `if`, vòng lặp `for` hoặc khai báo `const` bên trong `{}` của JSX. Hãy xử lý trước `return`, hoặc dùng biểu thức phù hợp như toán tử ba ngôi trong ví dụ trên.

**Một số thuộc tính khác HTML.** Dùng `className` thay cho `class`, `htmlFor` thay cho `for`; nhiều thuộc tính dùng camelCase như `onClick`, `tabIndex`. Các thuộc tính `aria-*` và `data-*` vẫn giữ dấu gạch nối.

```jsx
const field = (
  <div className="form-field">
    <label htmlFor="username">Tên người dùng</label>
    <input id="username" tabIndex={0} aria-label="Tên người dùng" />
  </div>
);
```

**Spread attributes** giúp truyền các thuộc tính từ một đối tượng vào phần tử. Chỉ truyền các thuộc tính bạn thực sự muốn sử dụng:

```jsx
function SearchInput() {
  const inputProps = {
    type: 'search',
    placeholder: 'Tìm kiếm...',
    name: 'keyword',
  };

  return <input {...inputProps} />;
}
```

## 5. Tạo project ReactJS bằng Vite

### Chuẩn bị

- **Node.js:** môi trường chạy JavaScript bên ngoài trình duyệt.
- **npm:** công cụ quản lý package, thường được cài cùng Node.js.

Cài Node.js tương thích với [yêu cầu hiện tại của Vite](https://vite.dev/guide/), sau đó mở terminal và kiểm tra:

```bash
node -v
npm -v
```

Nếu terminal chưa nhận lệnh sau khi cài Node.js, hãy đóng rồi mở lại terminal.

### Tạo và chạy project

Chạy lần lượt các lệnh sau để tạo project React sử dụng JavaScript:

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

Nếu npm hỏi có cài công cụ tạo project hay không, xác nhận để tiếp tục. Khi server chạy, mở địa chỉ **Local** được in trong terminal. Dùng `Ctrl+C` để dừng server.

### Các thư mục và file chính

```text
my-react-app/
├── node_modules/
├── public/
├── src/
│   ├── App.jsx
│   └── main.jsx
├── index.html
├── package.json
├── package-lock.json
└── vite.config.js
```

Cấu trúc trên chỉ liệt kê các mục chính; template có thể có thêm file CSS, tài nguyên và cấu hình khác.

| Thư mục / File | Vai trò |
| --- | --- |
| `node_modules/` | Chứa các package được cài bằng npm; không chỉnh sửa trực tiếp. |
| `public/` | Chứa tài nguyên tĩnh được phục vụ trực tiếp. |
| `src/` | Chứa phần lớn mã nguồn giao diện và logic ứng dụng. |
| `src/App.jsx` | Component chính trong template; nơi phù hợp để thử các ví dụ của bài. |
| `src/main.jsx` | Điểm khởi động phía React, gắn component gốc vào phần tử DOM trong HTML. |
| `index.html` | Tài liệu HTML gốc chứa phần tử để React gắn giao diện vào. |
| `package.json` | Khai báo thông tin project, dependencies và các script. |
| `package-lock.json` | Ghi lại phiên bản package được npm giải quyết để hỗ trợ cài đặt nhất quán. |
| `vite.config.js` | Cấu hình Vite và plugin sử dụng trong project. |

### Thực hành

1. Tạo và chạy project theo các lệnh trên.
2. Thay toàn bộ nội dung `src/App.jsx` bằng ví dụ `Welcome` ở phần 1, rồi lưu file.
3. Kiểm tra trình duyệt hiển thị hai lời chào.
4. Thử thay bằng ví dụ bộ đếm ở phần 3; bấm **Tăng** và kiểm tra số thay đổi.
5. Thử ví dụ chèn JavaScript ở phần 4 và thay giá trị các biến để quan sát kết quả.

Các ví dụ có `export default function App()` là các phương án thay thế nhau cho `src/App.jsx`; không dán tất cả vào cùng một file.

## Tài liệu tham khảo

- Tài liệu ReactJS do người học cung cấp: nội dung nền tảng của bài 1.
- [React: Viết giao diện với JSX](https://react.dev/learn/writing-markup-with-jsx).
- [React: Render và Commit](https://react.dev/learn/render-and-commit).
- [Vite: Bắt đầu tạo project](https://vite.dev/guide/).

[← Quay về roadmap](./README.md)
