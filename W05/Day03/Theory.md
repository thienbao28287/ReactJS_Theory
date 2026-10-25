# W05 · Day03 — Dynamic routes và useParams

## Mục tiêu và nhịp học

Tạo trang chi tiết sản phẩm từ tham số URL.

Thuộc tuần **Điều hướng với React Router**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Trong W04/mini-shop, chạy npm install react-router-dom@6. Dùng nhánh v6 để khớp PDF, không trộn import/cấu hình framework mode của phiên bản khác. Dự án chỉ có một BrowserRouter: các demo bên dưới tự bọc Router, vì vậy main.jsx không bọc thêm. Giữ trang sản phẩm hiện có để ghép dần.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Param là chuỗi

path /products/:id ánh xạ id vào useParams. Không so sánh string id với number bằng === mà quên chuyển đổi hoặc chuẩn hóa.

### 2. Thay id phải thay dữ liệu

Khi chuyển giữa hai URL dùng cùng component, component có thể không unmount. Effect/service phải phụ thuộc id; cleanup request cũ.

### 3. Không tồn tại khác loading

Trạng thái đang tìm/tải khác với không có sản phẩm. Kiểm tra id sai định dạng, không có bản ghi và lỗi request bằng UI phù hợp.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { BrowserRouter, Routes, Route, Link, useParams } from 'react-router-dom';
const products = [{ id: 1, title: 'Book' }, { id: 2, title: 'Pen' }];
function Detail() {
  const { id } = useParams();
  const product = products.find(p => String(p.id) === id);
  return product ? <h1>{product.title}</h1> : <h1>Không tìm thấy sản phẩm</h1>;
}
export default function LessonDemo() {
  return <BrowserRouter><nav><Link to="/products/1">Book</Link> | <Link to="/products/2">Pen</Link></nav><Routes><Route path="/products/:id" element={<Detail />} /><Route path="*" element={<p>Chọn sản phẩm</p>} /></Routes></BrowserRouter>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Effect có [] dù đọc id; dùng location state làm nguồn duy nhất khiến refresh mất sản phẩm.

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

[Bài tiếp theo](../Day04/Theory.md).
