# W03 · Day06 — Tìm kiếm API và hủy request

## Mục tiêu và nhịp học

Ngăn response cũ ghi đè kết quả tìm kiếm mới.

Thuộc tuần **useEffect và API**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Từ gốc ReactJS, chạy npm create vite@latest W03/api-lab -- --template react, sau đó cd W03/api-lab, npm install và npm run dev. Dùng dự án này cả tuần; không tạo lại mỗi ngày. Ví dụ dùng /products.json: tạo public/products.json chứa [{"id":1,"title":"Book","price":80},{"id":2,"title":"Pen","price":10}]. Đây là fixture cục bộ để học độc lập với mạng.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Race condition

Hai request không bảo đảm hoàn tất theo thứ tự gửi. Nếu query B mới hơn A nhưng A về sau, UI có thể hiển thị dữ liệu cũ nếu không cleanup.

### 2. AbortController

Tạo controller trong effect, truyền signal cho fetch; cleanup gọi abort. Bỏ qua AbortError nhưng vẫn hiển thị lỗi thật. Ngoài hủy mạng, dùng cờ ignore khi cần bỏ qua công việc đã bắt đầu.

### 3. URL và dữ liệu ngoài

Mã hóa query bằng encodeURIComponent hoặc URLSearchParams. API công khai có thể rate limit; fixture giúp kiểm tra UI nhưng không chứng minh tích hợp thật đã hoạt động.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useEffect, useState } from 'react';
export default function LessonDemo() {
  const [name, setName] = useState('octocat');
  const [user, setUser] = useState(null);
  const [error, setError] = useState('');
  useEffect(() => {
    const controller = new AbortController();
    setUser(null); setError('');
    if (!name.trim()) return () => controller.abort();
    async function load() {
      try {
        const r = await fetch(`https://api.github.com/users/${encodeURIComponent(name.trim())}`, { signal: controller.signal });
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        const data = await r.json();
        if (!controller.signal.aborted) setUser(data);
      } catch (e) { if (!controller.signal.aborted) setError(e.message); }
    }
    load();
    return () => controller.abort();
  }, [name]);
  return <section><label>GitHub username<input value={name} onChange={e => setName(e.target.value)} /></label>{error && <p role="alert">{error}</p>}{user && <p>{user.login}</p>}</section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Dùng chung controller cho mọi lần effect; quên kiểm tra trạng thái aborted trước khi setState.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: Hook Trong ReactJS (2).pdf, trang 2–4; GitHub Lesson-03; roadmap Component Lifecycle và useEffect.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/learn/synchronizing-with-effects).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day07/Theory.md).
