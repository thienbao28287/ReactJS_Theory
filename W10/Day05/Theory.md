# W10 · Day05 — Test validation và loading/error

## Mục tiêu và nhịp học

Kiểm tra form và request với Promise/mạng được điều khiển.

Thuộc tuần **Kiểm thử hành vi**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Day01 có bài Jest độc lập; từ Day02 dùng Vitest cho dự án Vite, không trộn hai runner trong cùng file test. Cài bằng npm install -D vitest jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom @testing-library/user-event. Đối chiếu yêu cầu Node/Vite của Vitest đang cài, lưu lockfile. Đây là tuần thực hành test, không chỉ đọc cú pháp.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Form

Input sai phải hiển thị lỗi và không gọi submit service. Input đúng gọi đúng payload; không so mật khẩu thật hay dữ liệu cá nhân trong snapshot.

### 2. Async assertions

findBy cho nội dung xuất hiện, waitFor cho assertion sẽ đúng sau cập nhật. await trước khi assert; không dùng waitFor để thực hiện click lặp.

### 3. Mock tại ranh giới

Mock service hoặc HTTP, giữ React UI và validation thật. Reset mock giữa tests. Thành công/rỗng/lỗi nên được điều khiển, không dựa API công khai luôn sẵn sàng.

## Ví dụ có thể thử

Lưu Loader.test.jsx trong src/labs; sau đó viết tests cho module thật. Với vi.mock service, đặt mock đúng đường dẫn import và đọc tài liệu hoisting của Vitest nếu gặp lỗi biến chưa khởi tạo.

```jsx
// @vitest-environment jsdom
import { useEffect, useState } from 'react';
import { afterEach, expect, it, vi } from 'vitest';
import { render, screen, cleanup } from '@testing-library/react';
import '@testing-library/jest-dom/vitest';
afterEach(cleanup);
function Loader({ load }) {
  const [status, setStatus] = useState('Đang tải');
  useEffect(() => { let active = true; load().then(() => { if (active) setStatus('Hoàn tất'); }, () => { if (active) setStatus('Có lỗi'); }); return () => { active = false; }; }, [load]);
  return <p role="status">{status}</p>;
}
it('hiển thị lỗi khi service reject', async () => {
  const load = vi.fn().mockRejectedValue(new Error('offline'));
  render(<Loader load={load} />);
  expect(await screen.findByText('Có lỗi')).toBeInTheDocument();
});
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Mock luôn validation thành công; assertion chạy trước Promise settle; waitFor callback gây side effect.

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

[Bài tiếp theo](../Day06/Theory.md).
