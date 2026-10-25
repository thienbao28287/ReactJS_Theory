# W08 · Day07 — Tổng kết Redux và kiến trúc dữ liệu

## Mục tiêu và nhịp học

Hoàn thiện bản Redux, so sánh với Context và kiểm tra toàn luồng.

Thuộc tuần **Redux Toolkit và async state**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop; npm install @reduxjs/toolkit@2 react-redux@9. Chỉ giữ một nguồn dữ liệu giỏ hàng: sau khi chuyển sang Redux, gỡ việc dùng CartContext ở giao diện tương ứng. Demo tự có Provider; khi ghép app thật, dùng Provider duy nhất ở entry.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Một chủ sở hữu cho mỗi dữ liệu

Cart ở slice, input local, auth Context mô phỏng, products ở thunk slice hoặc RTK Query. Quy tắc rõ tránh các bản sao bị lệch.

### 2. Kiểm chứng thay refactor cảm tính

Dùng đúng kịch bản W07 trước/sau; những thao tác người dùng phải giữ nguyên. Redux không tự sửa dữ liệu sai hoặc làm app nhanh hơn trong mọi trường hợp.

### 3. Mốc bàn giao

README ghi store shape, actions, selectors, cách persistence và phương án server state đã chọn. Người đọc biết tìm logic ở đâu mà không lần mọi file.

## Ví dụ có thể thử

Dữ liệu ghi chú kiến trúc: có thể lưu trong review.md hoặc src/labs/ownership.js, không phải cấu hình bắt buộc của ứng dụng.

```js
export const expectedOwnership = {
  cart: 'Redux cart slice',
  searchDraft: 'local state hoặc query URL',
  auth: 'AuthContext mô phỏng',
  products: 'Chọn thunk slice hoặc RTK Query cho app chính',
};
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Đổi state manager rồi quên persistence/model validation; đưa form draft vào Redux không có lý do.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: React-redux.pdf, trang 2–11; GitHub Lesson-09; roadmap Redux Toolkit. RTK Query và typed hooks là phần mở rộng.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://redux.js.org/tutorials/quick-start).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../../W09/Day01/Theory.md).
