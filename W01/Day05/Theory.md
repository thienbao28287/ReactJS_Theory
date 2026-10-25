# W01 · Day05 — Functional Component và ghép giao diện

## Mục tiêu và lịch học

Biết tạo component, tách file, dùng named/default export và ghép thành cây giao diện. Hiểu trách nhiệm của từng component thay vì chia nhỏ theo số dòng.

120 phút: 10 phút ôn JSX, 35 phút lý thuyết, 65 phút [bài tập](./Exercises.md), 10 phút tổng kết. Dùng `W01/react-profile` xuyên suốt.

## 1. Component là gì?

Trong phạm vi bài này, component là hàm trả về JSX. Component đóng gói một phần giao diện có ý nghĩa; các tuần sau bạn sẽ thêm dữ liệu đầu vào và logic tương tác.

```jsx
function WelcomeMessage() {
  return <p>Mỗi ngày tiến bộ một chút.</p>;
}

export default function App() {
  return (
    <main>
      <h1>Học React tuần đầu</h1>
      <WelcomeMessage />
    </main>
  );
}
```

Tên component bắt đầu bằng chữ hoa. Thẻ chữ thường như `<header>` là phần tử HTML; `<Header />` là component bạn định nghĩa/import. Dùng component bằng JSX, không gọi trực tiếp `WelcomeMessage()` trong cây giao diện.

## 2. Tách file và import/export

Tạo `src/components/Header.jsx`:

```jsx
export default function Header() {
  return (
    <header className="site-header">
      <p>Nhật ký học Frontend</p>
    </header>
  );
}
```

`src/components/Footer.jsx`:

```jsx
export function Footer() {
  return <footer><small>Học đều đặn, thực hành mỗi ngày.</small></footer>;
}
```

`src/App.jsx`:

```jsx
import Header from './components/Header.jsx';
import { Footer } from './components/Footer.jsx';

export default function App() {
  return (
    <>
      <Header />
      <main><h1>Hồ sơ học tập</h1></main>
      <Footer />
    </>
  );
}
```

Default export: một giá trị mặc định mỗi module, import không có `{}`. Named export: import có `{}` và tên khớp. Nên giữ tên file/tên component nhất quán để dễ tìm, kể cả khi cú pháp cho phép đặt tên import khác.

## 3. Cây component và composition

```text
App
  Header
  main (HTML)
    Profile
    Skills
    LearningGoals
  Footer
```

Composition là ghép các phần nhỏ để tạo phần lớn hơn. Chia theo trách nhiệm: Header nhận diện trang; Profile mô tả người học; Skills hiển thị kỹ năng; LearningGoals nói mục tiêu. Không cần một component riêng cho mọi thẻ `p`.

Tách component khi phần đó có ý nghĩa riêng, được tái sử dụng, hoặc đang khiến component cha khó đọc. Giữ component liên quan trong cùng file vẫn hợp lệ; bài này tách file để luyện import/export.

## 4. Render nên giữ tính thuần

Với cùng đầu vào, phần tính giao diện nên cho kết quả nhất quán và không sửa dữ liệu bên ngoài. Không sửa DOM bằng `document.querySelector` trong thân component; không tự tăng biến toàn cục mỗi lần render.

```jsx
const course = { title: 'React cơ bản' };

function CourseLabel() {
  return <span>{course.title}</span>;
}

export default function App() {
  return <main><CourseLabel /><CourseLabel /></main>;
}
```

Hai lần dùng component tạo hai vị trí giao diện riêng. Ví dụ chỉ đọc object tĩnh, không thay đổi object trong quá trình render.

Định nghĩa component ở cấp module, không định nghĩa `Header` bên trong hàm `App`. Điều này giữ danh tính component ổn định; bạn sẽ hiểu rõ hơn khi học State.

## 5. Chưa cần đưa Props và State vào hôm nay

W01 luyện component tĩnh và composition. Sang W02, Props sẽ giúp các lần dùng component nhận nội dung khác nhau; State giúp ghi nhớ và cập nhật dữ liệu theo tương tác. Không dùng biến thường để giả lập cơ chế State.

## Lỗi thường gặp

- Import sai kiểu: `import { Header }` khi file chỉ có default export.
- Sai chữ hoa/thường trong đường dẫn; có thể chạy trên máy này nhưng lỗi ở môi trường khác.
- Quên `return` hoặc xuống dòng ngay sau `return` rồi mới mở ngoặc.
- Quên dùng `<Header />` trong App dù đã import.
- Khai báo cùng component lặp lại bên trong component cha.

## Nguồn

- PDF `ReactJS (1) (1).pdf`, trang 2–3: component và tái sử dụng.
- [GitHub Lesson-01](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory/Lesson-01), Functional Components.
- [Roadmap](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap), JSX và Components.
- [React — Your First Component](https://react.dev/learn/your-first-component), [Importing and Exporting Components](https://react.dev/learn/importing-and-exporting-components).

Tiếp theo: [Day06 — Dự án thực hành](../Day06/Theory.md).
