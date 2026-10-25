# W06 · Day07 — Tổng kết form và giao diện

## Mục tiêu và nhịp học

Hoàn thiện form mini-shop và ma trận validation.

Thuộc tuần **Styling, React Hook Form và Zod**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Trong dự án chạy npm install react-hook-form@7 zod@4 @hookform/resolvers và npm install -D tailwindcss@4 @tailwindcss/vite@4. Lưu package-lock.json. Chỉ thêm plugin Tailwind ở Day02; không cần cài lại mỗi ngày.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Kiểm tra theo dữ liệu

Tạo bảng trường–quy tắc–input hợp lệ–input lỗi. Đây là contract có thể dùng để viết test W10, không chỉ danh sách checkbox hình thức.

### 2. Lỗi có thể hồi phục

Người dùng cần biết trường nào sai và sửa thế nào. Lỗi mạng có nút thử lại hoặc submit lại, không làm mất dữ liệu.

### 3. Style không thay ngữ nghĩa

CSS đổi hình thức, không tự tạo label, heading hay hành vi bàn phím. Kiểm tra tương phản và focus trên trang có form lẫn danh sách.

## Ví dụ có thể thử

Module dữ liệu kiểm tra: lưu src/lib/validationCases.js để tham chiếu thủ công, chưa phải test runner. Với schema password chỉ dùng dữ liệu giả khi thực hành.

```js
export const validationCases = [
  { field: 'name', input: '   ', expected: 'invalid' },
  { field: 'email', input: 'bao@example.com', expected: 'valid' },
  { field: 'quantity', input: 0, expected: 'invalid' },
  { field: 'quantity', input: 1, expected: 'valid' },
  { field: 'quantity', input: 100, expected: 'invalid' },
];
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Chỉ kiểm tra form hợp lệ; chỉnh CSS mà bỏ qua focus và lỗi.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: GitHub Lesson-03 và Lesson-06; roadmap Forms/Styling. PDF Props & State là nền tảng cho input; React Hook Form và Zod là phần mở rộng từ GitHub.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react-hook-form.com/get-started).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../../W07/Day01/Theory.md).
