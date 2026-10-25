# W10 · Day04 — userEvent và giỏ hàng tích hợp

## Mục tiêu và nhịp học

Kiểm tra tương tác qua UI với store độc lập mỗi test.

Thuộc tuần **Kiểm thử hành vi**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Day01 có bài Jest độc lập; từ Day02 dùng Vitest cho dự án Vite, không trộn hai runner trong cùng file test. Cài bằng npm install -D vitest jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom @testing-library/user-event. Đối chiếu yêu cầu Node/Vite của Vitest đang cài, lưu lockfile. Đây là tuần thực hành test, không chỉ đọc cú pháp.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Tương tác bất đồng bộ

userEvent.setup tạo user; await click/type để React hoàn thành cập nhật. Không thay mọi tương tác bằng gọi handler trực tiếp.

### 2. Provider test

Render component thật dưới store factory và MemoryRouter nếu cần. Preloaded cart rõ cho từng test; tránh dùng store singleton của entry.

### 3. Assertion theo luồng

Kiểm tra thêm, gộp id, đổi quantity và xóa qua nội dung người dùng nhìn thấy. Không chỉ kiểm tra dispatch được gọi nếu UI tổng tiền có thể sai.

## Ví dụ có thể thử

Demo test src/labs/Counter.test.jsx; bài 2–3 viết file test riêng import UI thật. Demo Counter chỉ giúp học userEvent, không thay bài kiểm thử giỏ.

```jsx
// @vitest-environment jsdom
import { useState } from 'react';
import { afterEach, expect, it } from 'vitest';
import { render, screen, cleanup } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom/vitest';
afterEach(cleanup);
function Counter() { const [n, setN] = useState(0); return <button onClick={() => setN(v => v + 1)}>Số lượng {n}</button>; }
it('tăng qua hành động người dùng', async () => {
  const user = userEvent.setup(); render(<Counter />);
  await user.click(screen.getByRole('button', { name: 'Số lượng 0' }));
  expect(screen.getByRole('button', { name: 'Số lượng 1' })).toBeInTheDocument();
});
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Dùng setTimeout 1 giây cho mọi assertion; mock useSelector/useDispatch hết làm mất kiểm tra tích hợp.

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

[Bài tiếp theo](../Day05/Theory.md).
