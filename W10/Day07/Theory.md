# W10 · Day07 — Tổng kết test và sửa lỗi hồi quy

## Mục tiêu và nhịp học

Xây bộ kiểm thử bảo vệ các luồng quan trọng và đọc báo cáo lỗi.

Thuộc tuần **Kiểm thử hành vi**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Day01 có bài Jest độc lập; từ Day02 dùng Vitest cho dự án Vite, không trộn hai runner trong cùng file test. Cài bằng npm install -D vitest jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom @testing-library/user-event. Đối chiếu yêu cầu Node/Vite của Vitest đang cài, lưu lockfile. Đây là tuần thực hành test, không chỉ đọc cú pháp.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Chất lượng hơn số lượng

Coverage cao không bảo đảm assertion đúng; ưu tiên các quy tắc tiền/số lượng, validation, request state và một luồng E2E.

### 2. Test độc lập

Mỗi test có dữ liệu đầu vào rõ, dọn DOM/mocks/storage có chủ đích. Chạy toàn suite phát hiện phụ thuộc lẫn nhau mà chạy riêng có thể bỏ sót.

### 3. Ghi bằng chứng

Lưu lệnh, số test pass/fail và lỗi đã sửa. Phần chưa chạy được vì môi trường phải ghi chưa xác nhận, không đổi trạng thái thành pass.

## Ví dụ có thể thử

JSON là hợp đồng báo cáo, có thể lưu W10/Day07/test-plan.json; không ghi đè package.json bằng object này. Lệnh thực thi chạy trong W04/mini-shop.

```json
{
  "unitCommand": "npx vitest run",
  "e2eCommand": "npx cypress run",
  "requiredBehaviors": ["cart totals", "quantity bounds", "form validation", "request error recovery", "catalog to cart"]
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Xóa test lỗi để suite xanh; báo pass khi chưa chạy browser E2E.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: Roadmap Jest Unit Testing, React Testing Library và Cypress. Bài test ứng dụng giỏ hàng áp dụng kiến thức Redux trong PDF/GitHub.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://vitest.dev/guide/).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../../W11/Day01/Theory.md).
