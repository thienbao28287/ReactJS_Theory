# W07 · Day07 — Tổng kết kiến trúc Context và reducer

## Mục tiêu và nhịp học

Tự giải thích và kiểm tra giỏ hàng dùng chung nhiều route.

Thuộc tuần **Context và useReducer**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Không thêm thư viện. Các ví dụ Provider là module độc lập để thử; khi ghép vào ứng dụng, đặt Provider phía trên các component cần đọc Context. Đăng nhập tuần này chỉ là mô phỏng giao diện, không phải hệ thống xác thực thật.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Một nguồn dữ liệu

ProductCard, Header và CartPage phải đọc/cập nhật cùng CartProvider. Nếu số badge khác CartPage, tìm state trùng trước khi thêm effect đồng bộ.

### 2. Tách logic để kiểm tra

Reducer có thể gọi như hàm bình thường. Bảng action→state mong đợi là nền tảng cho test W10 và so sánh Redux W08.

### 3. Giới hạn và bước tiếp

Context + reducer đủ cho app nhỏ. Redux thêm công cụ, quy ước và middleware; không chuyển chỉ vì Context bị xem là cũ.

## Ví dụ có thể thử

Module dữ liệu kịch bản: lưu trong notes hoặc src/lib/cartScenario.js. expectedCount là tổng quantity, không phải số dòng khác id.

```js
export const cartScenario = [
  { action: { type: 'add', product: { id: 1, title: 'Book', price: 80 } }, expectedCount: 1 },
  { action: { type: 'add', product: { id: 1, title: 'Book', price: 80 } }, expectedCount: 2 },
  { action: { type: 'remove', id: 1 }, expectedCount: 0 },
];
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Chuyển Redux mà không lưu mốc Context để đối chiếu; kiểm tra chỉ một component.

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

[Bài tiếp theo](../../W08/Day01/Theory.md).
