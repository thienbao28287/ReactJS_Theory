# W09 · Day07 — Tổng kết performance và rà soát effects

## Mục tiêu và nhịp học

Giữ code dễ hiểu, loại bỏ cache/effect dư thừa và ghi quyết định.

Thuộc tuần **Re-render và tối ưu hiệu năng**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Giữ StrictMode, đo cùng môi trường và cùng dữ liệu. Các demo minh họa memo thủ công; nếu dự án đã bật React Compiler, ghi điều đó vì compiler có thể tự tối ưu. Không bật/tắt compiler giữa hai phép so sánh.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Rà soát effect

Tổng/filtered list thường tính trong render. Request/listener/storage cần đồng bộ ngoài. Mỗi effect nên có mục đích và cleanup khi có tài nguyên.

### 2. Rà soát memo

Mỗi memo/useMemo/useCallback cần giải thích input, lợi ích và dependency. Không giữ cache đã chứng minh không cần chỉ vì đã viết.

### 3. Dự án bàn giao

Viết báo cáo ngắn có vấn đề, thay đổi, kiểm tra và giới hạn. Thời gian người dùng cảm nhận và tính đúng quan trọng hơn bảng đếm log.

## Ví dụ có thể thử

Object này là danh sách yêu cầu báo cáo, không phải dữ liệu mẫu để giả kết quả. Điền số đo thật vào báo cáo Markdown khi làm bài.

```js
export const performanceReview = {
  interaction: 'Lọc danh sách sản phẩm theo từ khóa',
  evidenceRequired: ['dataset', 'environment', 'before', 'after', 'correctnessChecks'],
  decisionOptions: ['Giữ tối ưu có bằng chứng', 'Bỏ tối ưu không có lợi', 'Cần đo thêm'],
};
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Coi mọi effect là xấu hoặc mọi memo là tốt; tắt lint/StrictMode như một tối ưu.

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

[Bài tiếp theo](../../W10/Day01/Theory.md).
