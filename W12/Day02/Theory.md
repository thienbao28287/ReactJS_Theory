# W12 · Day02 — Hooks React 18: useId, transition và deferred value

## Mục tiêu và nhịp học

Phân biệt tính duy nhất id, cập nhật ưu tiên thấp và giá trị trì hoãn.

Thuộc tuần **React nâng cao và tổng kết**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop và React/React DOM cùng major 19 cho các API React 19: kiểm tra npm ls react react-dom, nâng cùng nhau bằng npm install react@19 react-dom@19 nếu cần. Giữ react-router-dom@6 từ W05 cho Data Router. Làm các demo nâng cao trong module riêng, không thay state manager của dự án đã hoàn thiện.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. useId

Sinh id liên kết label/input hỗ trợ nhiều instance và hydration. Không dùng làm key danh sách: key phải từ danh tính dữ liệu.

### 2. useTransition

Đánh dấu cập nhật có thể bị ngắt để giữ tương tác ưu tiên. Không dùng transition để điều khiển input text; giữ state input cập nhật ngay, chuyển phần kết quả nặng.

### 3. useDeferredValue và Hook ngoài phạm vi

Deferred value cho phần UI phụ chậm hơn giá trị nhập, không phải debounce có thời gian cố định và không tự giảm request mạng. useSyncExternalStore dành đăng ký external store; useInsertionEffect chủ yếu cho thư viện CSS, chỉ cần biết vai trò.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useDeferredValue, useId, useMemo, useState, memo } from 'react';
const rows = Array.from({ length: 3000 }, (_, id) => ({ id, title: `Product ${id}` }));
const Results = memo(function Results({ query }) {
  const visible = useMemo(() => rows.filter(row => row.title.toLowerCase().includes(query.toLowerCase())), [query]);
  return <ul>{visible.map(row => <li key={row.id}>{row.title}</li>)}</ul>;
});
export default function LessonDemo() {
  const id = useId();
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);
  return <section><label htmlFor={id}>Tìm</label><input id={id} value={query} onChange={e => setQuery(e.target.value)} /><div style={{ opacity: query === deferredQuery ? 1 : 0.5 }}><Results query={deferredQuery} /></div></section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Hứa useDeferredValue giảm số request; thêm Hook mới vào mọi phép tính nhỏ mà không đo.

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

[Bài tiếp theo](../Day03/Theory.md).
