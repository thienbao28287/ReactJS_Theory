# W12 · Day07 — Tự đánh giá 12 tuần và hướng phát triển

## Mục tiêu và nhịp học

Tự trình bày dự án, nhận diện lỗ hổng và chọn bước học tiếp theo.

Thuộc tuần **React nâng cao và tổng kết**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop và React/React DOM cùng major 19 cho các API React 19: kiểm tra npm ls react react-dom, nâng cùng nhau bằng npm install react@19 react-dom@19 nếu cần. Giữ react-router-dom@6 từ W05 cho Data Router. Làm các demo nâng cao trong module riêng, không thay state manager của dự án đã hoàn thiện.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Giải thích bằng luồng thật

Từ click thêm giỏ tới action/reducer/store/selector/UI, từ URL tới route/data và từ form tới validation/submit. Trình bày trên code của bạn thay vì học thuộc định nghĩa.

### 2. Đánh giá có minh chứng

Mỗi kỹ năng gắn với file, test hoặc thao tác demo. Chưa làm được API auth/backend thật thì ghi đúng, không đồng nhất mô phỏng với kinh nghiệm production.

### 3. Chọn nhánh tiếp

Nếu nền tảng tốt có thể học TypeScript sâu, server-state, accessibility hoặc framework SSR theo mục tiêu. Nếu Props/State/effect còn yếu, củng cố chúng trước khi thêm framework.

## Ví dụ có thể thử

Module dữ liệu này gợi ý loại bằng chứng cần tìm trong code của bạn; final-review.md phải trỏ tới file/kết quả thật, không chép object như một báo cáo hoàn thành.

```js
export const skillEvidence = [
  { skill: 'State ownership', evidence: 'Sơ đồ và code local/Context/Redux của dự án' },
  { skill: 'API resilience', evidence: 'Loading/error/retry/cancel và test liên quan' },
  { skill: 'User flows', evidence: 'URL, cart, form và E2E chạy thực tế' },
  { skill: 'Delivery', evidence: 'README, build logs và deploy nếu đã thực hiện' },
];
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Tự chấm theo số thư viện đã cài; bỏ qua nền tảng để học thêm framework.

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

[Ôn lại từ W01](../../W01/Day01/Theory.md).
