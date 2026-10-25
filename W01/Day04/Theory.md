# W01 · Day04 — Viết giao diện bằng JSX

## Mục tiêu và thời lượng

Chuyển được HTML cơ bản sang JSX, đưa dữ liệu JavaScript lên giao diện, hiểu Fragment và các lỗi cú pháp thường gặp.

120 phút: 10 phút ôn cấu trúc, 35 phút đọc/chạy ví dụ, 65 phút [bài tập](./Exercises.md), 10 phút tổng kết. Chỉnh `src/App.jsx` trong `W01/react-profile`.

## 1. JSX là cú pháp mở rộng của JavaScript

JSX cho phép mô tả giao diện với cú pháp gần HTML trong mã JavaScript. Công cụ như Vite xử lý JSX để trình duyệt chạy được. JSX không phải chuỗi HTML, cũng không phải template được chạy trực tiếp bằng `node App.jsx`.

```jsx
export default function App() {
  const learnerName = 'Bao';
  const studiedHours = 2;
  return (
    <main className="profile">
      <h1>Xin chào {learnerName}</h1>
      <p>Tuần này dự kiến học {studiedHours * 7} giờ.</p>
    </main>
  );
}
```

Trong `{}`, JavaScript được đánh giá thành giá trị để React hiển thị. Chuỗi không dùng `{}` được hiểu là nội dung chữ bình thường.

## 2. Các quy tắc quan trọng

| HTML quen thuộc | JSX |
| --- | --- |
| `class="profile"` | `className="profile"` |
| `<label for="name">` | `<label htmlFor="name">` |
| `<img src="/avatar.png">` | `<img src="/avatar.png" alt="Ảnh đại diện" />` |
| Thuộc tính như `tabindex` | `tabIndex` |

`aria-*` và `data-*` vẫn giữ dấu gạch ngang, ví dụ `aria-label`. Không đổi mọi thuộc tính một cách máy móc sang camelCase.

Các thẻ phải đóng. Kết quả trả về cần một giá trị JSX; để nhóm nhiều phần tử ngang hàng, bọc bằng một thẻ hoặc Fragment:

```jsx
export default function App() {
  return (
    <>
      <header><h1>Nhật ký React</h1></header>
      <main><p>Ngày thứ tư</p></main>
    </>
  );
}
```

Fragment `<>...</>` nhóm phần tử mà không tạo thêm DOM wrapper. Khi thực sự cần một khối layout hay ngữ nghĩa như `main`, hãy dùng thẻ thích hợp.

## 3. Expression và statement

Trong `{}`, dùng biểu thức như biến, lời gọi hàm, phép tính hoặc toán tử ba ngôi. Không viết trực tiếp câu lệnh `if` hay `for` ở đó.

```jsx
export default function App() {
  const isLearning = true;
  const status = isLearning ? 'Đang học React' : 'Đang nghỉ';
  return <p>{status}</p>;
}
```

Bạn có thể đặt `if` trước `return` trong thân hàm. W02 sẽ học hiển thị điều kiện và danh sách sâu hơn; W01 chỉ cần đọc được biểu thức đơn giản.

## 4. Thuộc tính động, style và comment

```jsx
export default function App() {
  const website = 'https://react.dev';
  const headingStyle = { color: '#1d4ed8', fontSize: '2rem' };
  return (
    <main>
      {/* Nội dung dành cho người mới học */}
      <h1 style={headingStyle}>Học React</h1>
      <a href={website}>Tài liệu React</a>
    </main>
  );
}
```

`style` nhận object, không nhận chuỗi CSS. Cặp ngoặc kép trong `style={{ color: 'blue' }}` là một cặp để vào JavaScript và một cặp tạo object. Dùng CSS file cho phần lớn styling để dễ quản lý.

React hiển thị chuỗi như văn bản; đừng dùng API chèn HTML thô cho bài này. Object thuần như `{ name: 'Bao' }` không phải nội dung hiển thị hợp lệ: chọn thuộc tính như `profile.name`.

## 5. Chất lượng HTML vẫn quan trọng

Dùng `header`, `main`, `section`, `footer` đúng mục đích; tiêu đề có thứ bậc; link dùng để điều hướng; button dùng cho hành động. Ảnh nội dung cần `alt` mô tả. Việc code chạy được không thay thế cấu trúc HTML dễ đọc và sử dụng.

## Nguồn

- PDF `ReactJS (1) (1).pdf`, trang 5–6: JSX, Fragment, thuộc tính, biểu thức.
- [GitHub Lesson-01](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory/Lesson-01) và [roadmap](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap), mục JSX/Components.
- Đối chiếu quy tắc: [React — Writing Markup with JSX](https://react.dev/learn/writing-markup-with-jsx), [JavaScript in JSX](https://react.dev/learn/javascript-in-jsx-with-curly-braces).

Tiếp theo: [Day05 — Component](../Day05/Theory.md).
