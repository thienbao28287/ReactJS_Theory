# W09 · Day06 — Tối ưu catalog bằng một thay đổi đo được

## Mục tiêu và nhịp học

Thực hiện quy trình baseline–giả thuyết–thay đổi–đối chiếu.

Thuộc tuần **Re-render và tối ưu hiệu năng**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Giữ StrictMode, đo cùng môi trường và cùng dữ liệu. Các demo minh họa memo thủ công; nếu dự án đã bật React Compiler, ghi điều đó vì compiler có thể tự tối ưu. Không bật/tắt compiler giữa hai phép so sánh.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Phạm vi nhỏ

Chọn một thao tác như gõ tìm kiếm hoặc cập nhật giỏ. Chỉ đổi một nhóm nguyên nhân để biết kết quả đến từ đâu.

### 2. Đúng trước nhanh

So cùng kết quả lọc, count, total và các tương tác sau tối ưu. Không được làm UI chậm cập nhật hoặc hiển thị dữ liệu cũ chỉ để ít render.

### 3. Báo cáo trung thực

Ghi số đo, môi trường, giới hạn. Nếu không có cải thiện rõ, bỏ tối ưu không cần hoặc ghi kết luận chưa đủ bằng chứng.

## Ví dụ có thể thử

Module tính toán thuần có named export: src/lib/measurements.js. Không coi hàm tổng hợp này là benchmark tự động của trình duyệt.

```js
export function summarizeMeasurements(values) {
  if (!values.length || values.some(value => !Number.isFinite(value))) throw new Error('Cần số đo hợp lệ');
  const sorted = [...values].sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  const median = sorted.length % 2 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2;
  return { min: sorted[0], max: sorted[sorted.length - 1], median };
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Thêm một lượt nhiều Hook rồi không biết cái nào có ích; sửa dữ liệu để benchmark dễ hơn.

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

[Bài tiếp theo](../Day07/Theory.md).
