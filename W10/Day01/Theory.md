# W10 · Day01 — Testing pyramid và Jest cơ bản

## Mục tiêu và nhịp học

Phân biệt test cấp hàm, component và E2E; chạy bài Jest độc lập.

Thuộc tuần **Kiểm thử hành vi**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Day01 có bài Jest độc lập; từ Day02 dùng Vitest cho dự án Vite, không trộn hai runner trong cùng file test. Cài bằng npm install -D vitest jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom @testing-library/user-event. Đối chiếu yêu cầu Node/Vite của Vitest đang cài, lưu lockfile. Đây là tuần thực hành test, không chỉ đọc cú pháp.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Mỗi tầng một mục tiêu

Unit kiểm tra quy tắc tính toán; component kiểm tra hành vi UI; E2E kiểm tra luồng trên browser. Không dùng E2E cho mọi nhánh reducer nếu unit test rõ hơn.

### 2. Arrange–Act–Assert

Chuẩn bị input, thực hiện hành động, so kết quả có ý nghĩa. Test phải có thể thất bại khi hành vi sai; test chỉ xác nhận function tồn tại không bảo vệ nghiệp vụ.

### 3. Jest và Vitest

Roadmap giới thiệu Jest; học cú pháp bằng lab Node CommonJS riêng. Dự án Vite dùng Vitest từ Day02 để giảm cấu hình chuyển đổi JSX; không gọi jest.fn trong file Vitest.

## Ví dụ có thể thử

Lưu W10/jest-lab/total.test.cjs theo hướng dẫn bài 1. Đây là lab CommonJS độc lập; không import file này vào ứng dụng React.

```js
const { test, expect } = require('@jest/globals');
function total(items) { return items.reduce((sum, item) => sum + item.price * item.quantity, 0); }
test('giỏ rỗng có tổng bằng 0', () => { expect(total([])).toBe(0); });
test('tổng tính cả số lượng', () => {
  expect(total([{ price: 80, quantity: 2 }, { price: 10, quantity: 1 }])).toBe(170);
});
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Test chép lại cùng logic trong expected thay vì kết quả độc lập; trộn config Jest vào Vite.

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

[Bài tiếp theo](../Day02/Theory.md).
