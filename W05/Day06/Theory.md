# W05 · Day06 — Protected route và 404

## Mục tiêu và nhịp học

Bảo vệ luồng UI mô phỏng mà không nhầm với phân quyền Backend.

Thuộc tuần **Điều hướng với React Router**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Trong W04/mini-shop, chạy npm install react-router-dom@6. Dùng nhánh v6 để khớp PDF, không trộn import/cấu hình framework mode của phiên bản khác. Dự án chỉ có một BrowserRouter: các demo bên dưới tự bọc Router, vì vậy main.jsx không bọc thêm. Giữ trang sản phẩm hiện có để ghép dần.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Guard giao diện

Navigate chuyển người chưa đăng nhập tới login; Outlet render nhánh được phép. Backend vẫn phải kiểm tra quyền thật ở từng request.

### 2. Giữ đích quay lại

useLocation có thể lưu đích nội bộ vào location state. Chỉ cho quay lại đường dẫn nội bộ hợp lệ khi áp dụng login; không chuyển tới URL tùy ý từ query chưa kiểm tra.

### 3. 404 và trạng thái auth

Route * xử lý URL không khớp. Khi auth cần tải ban đầu, phân biệt chưa biết với chưa đăng nhập để tránh redirect chớp; tuần này auth là state mô phỏng đồng bộ.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useState } from 'react';
import { BrowserRouter, Routes, Route, Navigate, Outlet, Link } from 'react-router-dom';
function Guard({ signedIn }) { return signedIn ? <Outlet /> : <Navigate to="/login" replace />; }
export default function LessonDemo() {
  const [signedIn, setSignedIn] = useState(false);
  return <BrowserRouter><Link to="/account">Tài khoản</Link><Routes><Route path="/login" element={<button onClick={() => setSignedIn(true)}>Đăng nhập mô phỏng</button>} /><Route element={<Guard signedIn={signedIn} />}><Route path="/account" element={<h1>Tài khoản</h1>} /></Route><Route path="*" element={<h1>404 — Không có trang này</h1>} /></Routes></BrowserRouter>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Cho rằng ẩn menu là bảo mật API; demo đăng nhập tự chuyển ngay mà không giải thích state.

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

[Bài tiếp theo](../Day07/Theory.md).
