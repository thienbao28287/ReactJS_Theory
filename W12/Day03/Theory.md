# W12 · Day03 — React 19 Actions và optimistic UI

## Mục tiêu và nhịp học

Thử useActionState, useFormStatus và useOptimistic trong một form client.

Thuộc tuần **React nâng cao và tổng kết**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop và React/React DOM cùng major 19 cho các API React 19: kiểm tra npm ls react react-dom, nâng cùng nhau bằng npm install react@19 react-dom@19 nếu cần. Giữ react-router-dom@6 từ W05 cho Data Router. Làm các demo nâng cao trong module riêng, không thay state manager của dự án đã hoàn thiện.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Action state

useActionState nhận hàm async (previousState, formData) và initialState, trả state/action/isPending. Dùng action cho form để có Action context; không gọi async dispatch tùy ý ngoài transition.

### 2. Form status

useFormStatus nhập từ react-dom và phải nằm trong component con của form cần đọc. Nếu gọi trong chính component tạo form, nó không theo dõi form phía dưới.

### 3. Optimistic

useOptimistic hiển thị tạm trong Action; kết quả xác nhận phải cập nhật state chuẩn. Thất bại phải hồi phục và có thông báo. Demo Promise local, không tự có Server Functions/Backend nhờ dùng Hook mới.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useActionState, useOptimistic } from 'react';
import { useFormStatus } from 'react-dom';
function SubmitButton() { const { pending } = useFormStatus(); return <button disabled={pending}>{pending ? 'Đang gửi' : 'Thêm ghi chú'}</button>; }
export default function LessonDemo() {
  const [state, action] = useActionState(async (previous, formData) => {
    const title = String(formData.get('title') ?? '').trim();
    if (!title) return { ...previous, error: 'Nhập nội dung' };
    const item = { id: crypto.randomUUID(), title };
    addOptimistic({ ...item, pending: true });
    await new Promise(resolve => setTimeout(resolve, 600));
    if (title === 'fail') return { ...previous, error: 'Gửi thất bại mô phỏng' };
    return { items: [...previous.items, item], error: '' };
  }, { items: [], error: '' });
  const [items, addOptimistic] = useOptimistic(state.items, (current, item) => [...current, item]);
  return <section><form action={action}><label>Nội dung<input name="title" /></label><SubmitButton /></form>{state.error && <p role="alert">{state.error}</p>}<ul>{items.map(item => <li key={item.id}>{item.title}{item.pending ? ' (đang gửi)' : ''}</li>)}</ul></section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Cập nhật optimistic ngoài Action/transition; nhầm useFormStatus thuộc react thay react-dom; coi client Action là Backend.

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

[Bài tiếp theo](../Day04/Theory.md).
