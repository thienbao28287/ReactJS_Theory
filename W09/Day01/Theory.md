# W09 · Day01 — Nguồn gốc re-render

## Mục tiêu và nhịp học

Phân biệt gọi component, cập nhật DOM và vấn đề hiệu năng thực tế.

Thuộc tuần **Re-render và tối ưu hiệu năng**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Giữ StrictMode, đo cùng môi trường và cùng dữ liệu. Các demo minh họa memo thủ công; nếu dự án đã bật React Compiler, ghi điều đó vì compiler có thể tự tối ưu. Không bật/tắt compiler giữa hai phép so sánh.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Vì sao render

State cục bộ đổi, cha render, Context đọc thay đổi hoặc subscription store cập nhật đều có thể dẫn tới render. Props giống không mặc định ngăn component thường render khi cha render.

### 2. Render không bằng DOM mới

React có thể tính lại JSX nhưng giữ DOM nếu kết quả phù hợp. Không tối ưu chỉ vì thấy console.log hai lần trong StrictMode.

### 3. Đo trước

Chọn thao tác chậm và dữ liệu cố định, ghi môi trường, đo vài lần rồi xem xu hướng. Số lần render là tín hiệu, không thay thời gian phản hồi người dùng.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useState } from 'react';
function Child() { console.log('Child render'); return <p>Nội dung tĩnh</p>; }
export default function LessonDemo() {
  const [count, setCount] = useState(0);
  return <section><button onClick={() => setCount(c => c + 1)}>{count}</button><Child /></section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Tối ưu số log thay vì thao tác chậm; dùng dữ liệu khác nhau cho trước/sau.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: Hook Trong ReactJS (2).pdf, trang 10–14; GitHub Lesson-05; roadmap Performance Optimization.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/reference/react/memo).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day02/Theory.md).
