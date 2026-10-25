# W02 · Day07 — Tổng kết Props–State và Todo

## Mục tiêu và nhịp học

Tự xây lại luồng Todo và giải thích vị trí State, callback và dữ liệu suy ra.

Thuộc tuần **Props, State và tương tác**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng tiếp W01/react-profile. Chạy npm run dev trong dự án đó. Ví dụ React độc lập có thể đặt ở src/LessonDemo.jsx rồi import vào App để thử; giữ lại trang hồ sơ cũ. Không cần thư viện mới.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Nâng state đúng chỗ

Khi nhiều component cần đọc/sửa cùng dữ liệu, đặt state tại cha chung gần nhất. Input chỉnh sửa cục bộ có thể nằm ở item; danh sách chuẩn do cha quản lý.

### 2. Tách theo trách nhiệm

TodoForm nhận onAdd; TodoList nhận items và callback; TodoItem hiển thị một item. Chưa cần Context/Redux vì cây dữ liệu nhỏ và luồng Props vẫn rõ.

### 3. Tiêu chí hoàn thành

Một luồng tốt có đầu vào hợp lệ, cập nhật đúng item, trạng thái rỗng và hành vi hủy. Có thể tự viết lại bằng hiểu biết thay vì nhớ nguyên code mẫu.

## Ví dụ có thể thử

Module thuần: lưu src/lib/todoSelectors.js; có named export, import từ component cần dùng. Chưa phải component JSX.

```js
export function getVisibleTodos(todos, filter) {
  if (filter === 'active') return todos.filter(todo => !todo.done);
  if (filter === 'completed') return todos.filter(todo => todo.done);
  return todos;
}
export function countActive(todos) {
  return todos.filter(todo => !todo.done).length;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Đưa mọi state lên App hoặc thêm global store khi chưa có nhu cầu; chỉ kiểm tra giao diện có dữ liệu.

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

[Bài tiếp theo](../../W03/Day01/Theory.md).
