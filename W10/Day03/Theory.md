# W10 · Day03 — React Testing Library: render và query

## Mục tiêu và nhịp học

Kiểm thử component qua role/label và chuẩn bị môi trường DOM.

Thuộc tuần **Kiểm thử hành vi**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Day01 có bài Jest độc lập; từ Day02 dùng Vitest cho dự án Vite, không trộn hai runner trong cùng file test. Cài bằng npm install -D vitest jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom @testing-library/user-event. Đối chiếu yêu cầu Node/Vite của Vitest đang cài, lưu lockfile. Đây là tuần thực hành test, không chỉ đọc cú pháp.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Query như người dùng

Ưu tiên getByRole/getByLabelText thay className hoặc DOM structure nội bộ. getBy cho phần tử phải có; queryBy cho điều không tồn tại; findBy chờ phần tử xuất hiện.

### 2. jsdom và matchers

Directive environment jsdom trong test cho DOM. Import @testing-library/jest-dom/vitest để có toBeInTheDocument; cleanup tránh DOM test trước còn lại.

### 3. Không test implementation

Kiểm tra text và hành động quan sát được, không đòi component dùng useState hay đúng số render. Refactor nội bộ không nên làm test hành vi gãy.

## Ví dụ có thể thử

File test độc lập src/labs/Greeting.test.jsx. Directive môi trường ở dòng đầu file; đây không phải component App và không được import test vào bundle UI.

```jsx
// @vitest-environment jsdom
import { afterEach, expect, it } from 'vitest';
import { render, screen, cleanup } from '@testing-library/react';
import '@testing-library/jest-dom/vitest';
afterEach(cleanup);
function Greeting({ name }) { return <section><h1>Xin chào {name}</h1><a href="/products">Xem sản phẩm</a></section>; }
it('hiển thị tên và link sản phẩm', () => {
  render(<Greeting name="Bao" />);
  expect(screen.getByRole('heading', { name: 'Xin chào Bao' })).toBeInTheDocument();
  expect(screen.getByRole('link', { name: 'Xem sản phẩm' })).toHaveAttribute('href', '/products');
});
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Test chỉ component giả rồi coi app đã được kiểm tra; dùng findBy khi không cần async hoặc getBy cho phần tử vắng.

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

[Bài tiếp theo](../Day04/Theory.md).
