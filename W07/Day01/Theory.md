# W07 · Day01 — State cục bộ, nâng State và prop drilling

## Mục tiêu và nhịp học

Chọn nơi sở hữu dữ liệu trước khi đưa vào global state.

Thuộc tuần **Context và useReducer**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Không thêm thư viện. Các ví dụ Provider là module độc lập để thử; khi ghép vào ứng dụng, đặt Provider phía trên các component cần đọc Context. Đăng nhập tuần này chỉ là mô phỏng giao diện, không phải hệ thống xác thực thật.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Local trước

Input mở/đóng và bản nháp thường thuộc component đang dùng. Không đưa tất cả vào global state; dữ liệu toàn cục tạo sự phụ thuộc và phạm vi cập nhật rộng hơn.

### 2. Cha chung

Hai component đọc/sửa cùng count thì nâng count lên cha chung. Cha truyền value và callback xuống; đây vẫn là mô hình đơn giản và đúng.

### 3. Prop drilling

Khi nhiều tầng trung gian chỉ chuyển dữ liệu, Context có thể giảm dây truyền. Trước đó thử composition để không tạo Context không cần thiết.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useState } from 'react';
function CartBadge({ count }) { return <p>Giỏ có {count} món</p>; }
function AddButton({ onAdd }) { return <button onClick={onAdd}>Thêm một món</button>; }
export default function LessonDemo() {
  const [count, setCount] = useState(0);
  return <section><CartBadge count={count} /><AddButton onAdd={() => setCount(c => c + 1)} /></section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Chọn Redux/Context chỉ vì có nhiều component chứ không xem dữ liệu cần chia sẻ gì.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: Hook Trong ReactJS (2).pdf, trang 5–9; GitHub Lesson-08; roadmap useContext, useReducer, Context API Advanced.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/learn/scaling-up-with-reducer-and-context).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day02/Theory.md).
