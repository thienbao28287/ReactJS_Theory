# W12 · Day06 — Hoàn thiện sản phẩm và bản phát hành học tập

## Mục tiêu và nhịp học

Đưa ứng dụng chính về trạng thái nhất quán và kiểm chứng toàn bộ luồng.

Thuộc tuần **React nâng cao và tổng kết**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop và React/React DOM cùng major 19 cho các API React 19: kiểm tra npm ls react react-dom, nâng cùng nhau bằng npm install react@19 react-dom@19 nếu cần. Giữ react-router-dom@6 từ W05 cho Data Router. Làm các demo nâng cao trong module riêng, không thay state manager của dự án đã hoàn thiện.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Đóng phạm vi

Chỉ giữ tính năng chính: catalog/detail/search/cart/form/auth mô phỏng. Lab Hooks/Zustand/Saga tách khỏi app chính và không tạo request nền khi không dùng.

### 2. Hồi quy có hệ thống

Chạy unit/component/E2E, build/preview, kiểm tra deep link và data env. Ghi lỗi thật và mức ảnh hưởng, sửa phần làm mất dữ liệu hoặc không chạy trước mỹ thuật.

### 3. Bàn giao trung thực

README nói rõ backend nào thật, phần nào fixture/mô phỏng và URL nào đã deploy. Không biến checkbox tài liệu thành tuyên bố test đã pass khi chưa thực hiện.

## Ví dụ có thể thử

JSON là checklist để lập release-report.md, không phải manifest triển khai. Đánh dấu trạng thái thực tế trong báo cáo sau khi chạy các lệnh.

```json
{
  "coreFlows": ["catalog", "product detail", "URL search", "cart persistence", "checkout validation", "mock auth guard"],
  "checks": ["unit/component tests", "E2E", "production build", "deep link refresh", "mobile layout"],
  "labBoundary": "Advanced demos are separate from the main application"
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Đổi kiến trúc phút cuối để dùng hết công cụ mới; tuyên bố production-ready chỉ vì build thành công.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: React Router (1).pdf, trang 9–13; roadmap React 18/19 Hooks, Zustand, Redux Saga; GitHub Lesson-10/11 để tổng kết dự án.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/reference/react).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day07/Theory.md).
