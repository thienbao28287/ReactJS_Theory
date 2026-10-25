# W09 · Day05 — useCallback và callback Props

## Mục tiêu và nhịp học

Ổn định tham chiếu hàm khi child memo cần, không tạo stale closure.

Thuộc tuần **Re-render và tối ưu hiệu năng**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Giữ StrictMode, đo cùng môi trường và cùng dữ liệu. Các demo minh họa memo thủ công; nếu dự án đã bật React Compiler, ghi điều đó vì compiler có thể tự tối ưu. Không bật/tắt compiler giữa hai phép so sánh.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Ghi nhớ tham chiếu

useCallback giữ tham chiếu hàm giữa các render nếu dependencies không đổi. Nó không tự ngăn tạo toàn bộ cú pháp hàm hoặc tự memo child.

### 2. Kết hợp đúng

Child memo nhận callback ổn định có cơ hội bỏ qua render do cha. Nếu các Props khác luôn mới, ổn định riêng callback chưa đủ.

### 3. Updater giảm phụ thuộc

Khi chỉ dùng State trước để cập nhật, setter updater tránh đọc snapshot. Vẫn khai báo mọi giá trị ngoài còn đọc; không dùng [] cho mọi callback.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { memo, useCallback, useState } from 'react';
const AddButton = memo(function AddButton({ onAdd }) { console.log('AddButton render'); return <button onClick={onAdd}>Thêm</button>; });
export default function LessonDemo() {
  const [count, setCount] = useState(0);
  const [query, setQuery] = useState('');
  const add = useCallback(() => setCount(c => c + 1), []);
  return <section><input aria-label="Tìm" value={query} onChange={e => setQuery(e.target.value)} /><AddButton onAdd={add} /><p>{count}</p></section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Bọc mọi event bằng useCallback dù không truyền đi; nhầm cache hàm với cache kết quả gọi hàm.

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

[Bài tiếp theo](../Day06/Theory.md).
