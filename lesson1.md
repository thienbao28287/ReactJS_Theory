# Bài 1: Nhập môn ReactJS

[Quay về roadmap](./README.md)

Bạn sẽ tạo một ứng dụng React bằng Vite, chia giao diện thành component và viết JSX để hiển thị dữ liệu. Sau phần thực hành, bạn sẽ tìm hiểu SPA và cách React cập nhật DOM để liên hệ những gì đã viết với hoạt động của trình duyệt.

### Kiến thức cần có

Bạn nên biết thẻ HTML, CSS cơ bản và JavaScript với biến, hàm, object, array. Trong bài, **component** là một phần giao diện được viết bằng hàm; **JSX** là cú pháp mô tả giao diện trong JavaScript; **render** là lúc React gọi component để tính giao diện.

### Kết quả sau bài học

- Tạo và chạy được project React bằng Vite.
- Viết component dùng lại nhiều lần và JSX có dữ liệu, điều kiện.
- Phân biệt SPA, DOM thật, DOM ảo, render và commit.

## 1. Tạo và chạy project ReactJS bằng Vite

### Bước 1 Kiểm tra công cụ

- **Node.js:** môi trường chạy JavaScript bên ngoài trình duyệt.
- **npm:** công cụ quản lý package, thường được cài cùng Node.js.

Cài Node.js tương thích với [yêu cầu hiện tại của Vite](https://vite.dev/guide/), sau đó mở terminal, tức cửa sổ nhập lệnh, và kiểm tra:

```bash
node -v
npm -v
```

Nếu terminal chưa nhận lệnh sau khi cài Node.js, hãy đóng rồi mở lại terminal.

### Bước 2 Tạo project

Chạy lần lượt các lệnh sau để tạo project React sử dụng JavaScript:

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

Nếu npm hỏi có cài công cụ tạo project hay không, xác nhận để tiếp tục. Các lệnh lần lượt tạo thư mục project, chuyển vào thư mục đó, cài dependencies và khởi động server phát triển. Nếu công cụ tạo project hỏi có cài và chạy ngay không, chọn tự thực hiện các lệnh để theo đúng các bước trên; nếu nó đã chạy server, không cần chạy server thứ hai. Khi server chạy, mở địa chỉ **Local** được in trong terminal. Dùng `Ctrl+C` để dừng server.

### Bước 3 Xác định các file cần chỉnh sửa

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

| Thư mục / File      | Vai trò                                                                    |
| ------------------- | -------------------------------------------------------------------------- |
| `node_modules/`     | Chứa các package được cài bằng npm; không chỉnh sửa trực tiếp.             |
| `public/`           | Chứa tài nguyên tĩnh được phục vụ trực tiếp.                               |
| `src/`              | Chứa phần lớn mã nguồn giao diện và logic ứng dụng.                        |
| `src/App.jsx`       | Component chính trong template; nơi phù hợp để thử các ví dụ của bài.      |
| `src/main.jsx`      | Điểm khởi động phía React, gắn component gốc vào phần tử DOM trong HTML.   |
| `index.html`        | Tài liệu HTML gốc chứa phần tử để React gắn giao diện vào.                 |
| `package.json`      | Khai báo thông tin project, dependencies và các script.                    |
| `package-lock.json` | Ghi lại phiên bản package được npm giải quyết để hỗ trợ cài đặt nhất quán. |
| `vite.config.js`    | Cấu hình Vite và plugin sử dụng trong project.                             |

### Bước 4 Chuẩn bị vùng thực hành

Giữ `src/main.jsx` của template để nó gắn `<App />` vào trang. Các ví dụ tiếp theo sẽ thay toàn bộ `src/App.jsx`. Mỗi file chỉ giữ một `export default`; lưu ví dụ hiện tại và kiểm tra trước khi chuyển sang ví dụ khác.

Bạn có thể xóa nội dung CSS mẫu trong `src/App.css` và `src/index.css` nếu muốn quan sát giao diện mặc định của trình duyệt; giữ file nếu `main.jsx` đang import nó. Không cần thêm CSS để chạy các ví dụ.

## 2. Tạo giao diện bằng component

Trong ReactJS, **Component** là một thành phần giao diện độc lập, có thể tái sử dụng. Một component có thể chứa giao diện và logic xử lý liên quan đến phần giao diện đó.

Ví dụ: một trang web có thể được chia thành `Header`, `Sidebar`, `ProductCard` và `Footer`.

### Bước 1 Viết component đầu tiên

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

### Bước 2 Hiểu và kiểm tra kết quả

`App` là component gốc được `main.jsx` sử dụng. `export default` cho phép file khác import component này. `return` trả về mô tả giao diện bằng JSX; JSX sẽ được giải thích kỹ ở phần tiếp theo.

Lưu file, mở địa chỉ Local và kiểm tra hai lời chào xuất hiện. Đổi câu chào trong `Welcome` rồi lưu: cả hai vị trí dùng component đều được cập nhật. Nếu chỉ thấy chữ `Welcome` thay vì lời chào, kiểm tra bạn đã viết thẻ `<Welcome />` và tên bắt đầu bằng chữ hoa.

### Vì sao sử dụng component?

| Lợi ích            | Ý nghĩa                                                          |
| ------------------ | ---------------------------------------------------------------- |
| Chia nhỏ giao diện | Tách trang lớn thành các phần dễ hiểu.                           |
| Tái sử dụng        | Dùng cùng một component tại nhiều vị trí.                        |
| Dễ bảo trì         | Sửa định nghĩa component để cập nhật các nơi sử dụng.            |
| Tổ chức logic      | Mỗi component phụ trách một phần giao diện và hành vi liên quan. |

## 3. Viết JSX để hiển thị dữ liệu

**JSX** là phần mở rộng cú pháp của JavaScript, cho phép viết giao diện có hình thức gần giống HTML ngay trong mã JavaScript. Công cụ như Vite xử lý JSX để trình duyệt có thể chạy ứng dụng.

Các đoạn khai báo biến hoặc component đơn lẻ trong phần này là **minh họa cú pháp**, chưa tự hiển thị khi dán riêng vào file. Đặt biến trước `return` và dùng nó trong JSX, hoặc dùng component qua thẻ như `<Introduction />` trong `App`.

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

### Thực hành chèn dữ liệu vào JSX

Thay toàn bộ `src/App.jsx` bằng ví dụ hoàn chỉnh bên dưới.

**Chèn biểu thức JavaScript bằng `{}`.** Có thể hiển thị biến, phép tính, kết quả gọi hàm và biểu thức điều kiện:

```jsx
export default function App() {
  const name = "An";
  const price = 50000;
  const quantity = 2;
  const isLoggedIn = true;

  return (
    <section>
      <h1>Xin chào, {name.toUpperCase()}!</h1>
      <p>Tổng tiền: {price * quantity} đồng</p>
      <p>{isLoggedIn ? "Đã đăng nhập" : "Chưa đăng nhập"}</p>
      {isLoggedIn && <button>Đăng xuất</button>}
    </section>
  );
}
```

Lưu file và kiểm tra: lời chào hiển thị `AN`, tổng tiền bằng `100000 đồng`, trạng thái là Đã đăng nhập và có nút Đăng xuất. Đổi `isLoggedIn` thành `false`, lưu rồi kiểm tra trạng thái và nút thay đổi. Nút Đăng xuất chỉ minh họa hiển thị có điều kiện, chưa được gắn hành vi.

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
    type: "search",
    placeholder: "Tìm kiếm...",
    name: "keyword",
  };

  return <input {...inputProps} />;
}
```

## 4. Hiểu cách hoạt động của SPA

**SPA (Single Page Application)** là ứng dụng web tải tài liệu HTML ban đầu, sau đó dùng JavaScript để cập nhật nội dung khi người dùng tương tác hoặc chuyển màn hình, thay vì tải lại toàn bộ tài liệu HTML cho mỗi lần điều hướng trong ứng dụng.

| Website nhiều trang truyền thống                              | SPA                                                  |
| ------------------------------------------------------------- | ---------------------------------------------------- |
| Chuyển trang thường yêu cầu một tài liệu HTML mới từ máy chủ. | Điều hướng nội bộ có thể được xử lý bằng JavaScript. |
| Trình duyệt thường tải lại toàn bộ trang.                     | Chỉ cập nhật giao diện cần hiển thị.                 |

Ví dụ: từ danh sách sản phẩm sang chi tiết sản phẩm, SPA có thể thay nội dung chính mà không tải lại toàn bộ trang. Ứng dụng vẫn có thể gửi yêu cầu lấy dữ liệu hoặc tải thêm mã JavaScript.

**Lưu ý về SEO:** SPA chỉ render phía trình duyệt có thể gặp khó khăn hơn với SEO nếu công cụ tìm kiếm không xử lý được nội dung JavaScript. Không phải mọi ứng dụng React đều có SEO kém; kết quả còn phụ thuộc cách triển khai, chẳng hạn render phía máy chủ hoặc tạo HTML tĩnh. React là thư viện giao diện, không bắt buộc ứng dụng phải là SPA.

## 5. Quan sát React cập nhật DOM

**DOM (Document Object Model)** là cách trình duyệt biểu diễn cấu trúc trang bằng các đối tượng. JavaScript có thể thay đổi DOM để cập nhật giao diện.

**DOM ảo (Virtual DOM)** là cách gọi phổ biến cho biểu diễn giao diện trong bộ nhớ mà React sử dụng khi tính toán cập nhật. Có thể hình dung quá trình như sau:

```text
Cập nhật state
  → React gọi component để tính giao diện mới (render)
  → Đối chiếu kết quả với lần trước
  → Áp dụng thay đổi cần thiết lên DOM thật (commit)
  → Trình duyệt vẽ lại màn hình
```

### Bước 1 Tạo một giao diện có tương tác

State là dữ liệu React ghi nhớ để cập nhật giao diện. Ví dụ dưới đây giới thiệu trước một bộ đếm nhỏ; cách dùng state sẽ được giải thích đầy đủ trong bài 2. Thay toàn bộ `src/App.jsx` bằng:

```jsx
import { useState } from "react";

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

### Bước 2 Theo dõi luồng cập nhật

`useState` lưu giá trị bộ đếm. `onClick` nhận hàm được gọi khi người dùng bấm nút; hàm này gọi `setCount` để yêu cầu tăng số đếm. React tính lại giao diện với state mới. Trong ví dụ này, React cập nhật phần văn bản của bộ đếm; không cần tạo lại toàn bộ trang.

Render không đồng nghĩa với thay đổi DOM: nếu kết quả không đổi, React có thể không cần sửa DOM. DOM ảo cũng không bảo đảm mọi ứng dụng luôn nhanh hơn thao tác DOM trực tiếp.

### Bước 3 Kiểm tra trên trình duyệt

Nhấn Tăng ba lần: số lần bấm cần chuyển từ `0` thành `3`. Trong ví dụ này, nút chỉ cập nhật state, không gửi form hoặc yêu cầu điều hướng nên trang không tải lại. Bạn có thể mở tab Elements trong DevTools để xem phần văn bản của bộ đếm thay đổi.

## 6. Lỗi thường gặp

| Hiện tượng                            | Cách kiểm tra                                                                                 |
| ------------------------------------- | --------------------------------------------------------------------------------------------- |
| Terminal không nhận `node` hoặc `npm` | Cài Node.js đáp ứng yêu cầu Vite, rồi mở lại terminal.                                        |
| Không tìm thấy `package.json`         | Chuyển terminal vào thư mục `my-react-app` trước khi chạy lệnh npm.                           |
| Trang trắng sau khi sửa JSX           | Xem thông báo lỗi trong terminal và Console; kiểm tra thẻ đóng, phần tử gốc và tên component. |
| Báo trùng khai báo `App` hoặc export  | Thay nội dung file bằng một ví dụ hoàn chỉnh, không nối các ví dụ.                            |
| Giao diện khác màu hoặc bố cục mẫu    | Kiểm tra CSS template; code trong bài chỉ yêu cầu nội dung và tương tác đúng.                 |

## 7. Ôn tập và bài tập thêm

### Câu hỏi ôn tập

1. Component giúp tái sử dụng giao diện như thế nào?
2. Vì sao tên component bắt đầu bằng chữ hoa?
3. JSX dùng dấu `{}` để làm gì?
4. Render khác commit ở điểm nào?
5. React có bắt buộc mọi ứng dụng phải là SPA không?

### Bài tập mở rộng

1. Tạo component `Footer` trong `src/App.jsx` và đặt `<Footer />` sau hai lời chào.
2. Thay giá và số lượng trong ví dụ JSX rồi kiểm tra tổng tiền.
3. Tạo object thuộc tính cho ô tìm kiếm, truyền bằng spread và dùng `<SearchInput />` trong `App` để xem kết quả.

## Tài liệu tham khảo

- [React: Viết giao diện với JSX](https://react.dev/learn/writing-markup-with-jsx).
- [React: Render và Commit](https://react.dev/learn/render-and-commit).
- [Vite: Bắt đầu tạo project](https://vite.dev/guide/).

[Bài 2: Props và State](./lesson2.md) | [Quay về roadmap](./README.md)
