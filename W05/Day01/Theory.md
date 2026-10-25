# W05 · Day01 — Router, Routes và Route

## Mục tiêu và nhịp học

Thiết lập ứng dụng nhiều URL với một Router duy nhất.

Thuộc tuần **Điều hướng với React Router**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Trong W04/mini-shop, chạy npm install react-router-dom@6. Dùng nhánh v6 để khớp PDF, không trộn import/cấu hình framework mode của phiên bản khác. Dự án chỉ có một BrowserRouter: các demo bên dưới tự bọc Router, vì vậy main.jsx không bọc thêm. Giữ trang sản phẩm hiện có để ghép dần.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. URL là một phần trạng thái ứng dụng

Routes chọn nhánh phù hợp với URL; Route gắn path với element. BrowserRouter dùng History API, không tự cấu hình server trả index.html cho deep link.

### 2. Một Router gốc

Đặt BrowserRouter ở một vị trí bao phủ cây cần routing. Demo tự bọc; khi chuyển sang main.jsx thì bỏ lớp bọc khỏi demo, không lồng hai BrowserRouter.

### 3. Trang và component

Page ghép dữ liệu/layout theo route; component như ProductCard tái sử dụng không cần biết toàn bộ sơ đồ URL.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
export default function LessonDemo() {
  return <BrowserRouter><nav><Link to="/">Trang chủ</Link> | <Link to="/products">Sản phẩm</Link></nav><Routes><Route path="/" element={<h1>Mini Shop</h1>} /><Route path="/products" element={<h1>Sản phẩm</h1>} /></Routes></BrowserRouter>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Dùng href nội bộ cho mọi link làm tải document không cần thiết; tưởng Router tự sửa server 404.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: React Router (1).pdf, trang 2–8; GitHub Lesson-07; roadmap Routing/Navigation.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://reactrouter.com/6.30.1).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day02/Theory.md).
