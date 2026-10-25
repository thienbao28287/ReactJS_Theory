# W02 · Day06 — Controlled input và Todo CRUD

## Mục tiêu và nhịp học

Tạo Todo bằng form, quản lý input bằng State và cập nhật danh sách.

Thuộc tuần **Props, State và tương tác**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng tiếp W01/react-profile. Chạy npm run dev trong dự án đó. Ví dụ React độc lập có thể đặt ở src/LessonDemo.jsx rồi import vào App để thử; giữ lại trang hồ sơ cũ. Không cần thư viện mới.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Một nguồn sự thật

Input có value/onChange lấy giá trị từ State. Với checkbox, dùng checked và event.target.checked. Khởi tạo chuỗi rỗng thay undefined để không chuyển uncontrolled sang controlled.

### 2. Submit và kiểm tra đầu vào

Form onSubmit hỗ trợ cả Enter lẫn button. preventDefault tránh reload; trim trước khi thêm để không tạo Todo rỗng. Tạo id một lần lúc thêm, không tạo trong render.

### 3. Derived data

Số Todo còn lại và danh sách lọc có thể tính từ todos/filter, không cần state riêng đồng bộ bằng effect. Chỉ giữ state cho dữ liệu gốc hoặc ý định người dùng.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useState } from 'react';
export default function LessonDemo() {
  const [title, setTitle] = useState('');
  const [todos, setTodos] = useState([]);
  function addTodo(event) {
    event.preventDefault();
    const value = title.trim();
    if (!value) return;
    setTodos(list => [...list, { id: crypto.randomUUID(), title: value, done: false }]);
    setTitle('');
  }
  return <section><form onSubmit={addTodo}><label htmlFor="todo-title">Việc cần làm</label><input id="todo-title" value={title} onChange={e => setTitle(e.target.value)} /><button>Thêm</button></form><ul>{todos.map(todo => <li key={todo.id}>{todo.title}</li>)}</ul></section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Dùng onClick thay onSubmit khiến Enter không hoạt động; đặt state số đếm riêng rồi quên cập nhật.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: ReactJS_state_props (1).pdf, trang 2–8; GitHub Lesson-02; roadmap Props/State, Event Handling, Lists và Keys.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/learn/adding-interactivity).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day07/Theory.md).
