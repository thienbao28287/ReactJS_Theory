# W06 · Day06 — Kết hợp RHF và Zod cho checkout

## Mục tiêu và nhịp học

Tạo form có schema thống nhất, lỗi trường và lỗi gửi.

Thuộc tuần **Styling, React Hook Form và Zod**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Trong dự án chạy npm install react-hook-form@7 zod@4 @hookform/resolvers và npm install -D tailwindcss@4 @tailwindcss/vite@4. Lưu package-lock.json. Chỉ thêm plugin Tailwind ở Day02; không cần cài lại mỗi ngày.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Resolver nối hai thư viện

zodResolver chuyển lỗi schema thành formState.errors. Không lặp cùng một quy tắc ở nhiều chỗ dễ lệch; HTML attributes vẫn hữu ích cho trải nghiệm nhập.

### 2. Luồng submit

RHF thu dữ liệu → resolver kiểm tra → onValid xử lý → thông báo kết quả. Mọi yêu cầu mạng phải catch và hiển thị lỗi, giữ dữ liệu để người dùng sửa/thử lại.

### 3. Kết quả mô phỏng

Chưa có Backend đơn hàng nên chỉ mô phỏng gửi. Không thông báo đã thanh toán thật, không thu thẻ ngân hàng. Giữ nhãn Checkout mô phỏng trong dự án học.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
const schema = z.object({ name: z.string().trim().min(1, 'Nhập tên') });
export default function LessonDemo() {
  const { register, handleSubmit, formState: { errors, isSubmitting }, setError } = useForm({ resolver: zodResolver(schema), defaultValues: { name: '' } });
  async function submit() {
    try { await new Promise(resolve => setTimeout(resolve, 500)); throw new Error('Dịch vụ mô phỏng đang lỗi'); }
    catch (e) { setError('root', { message: e.message }); }
  }
  return <form noValidate onSubmit={handleSubmit(submit)}><label>Tên<input {...register('name')} /></label>{errors.name && <p role="alert">{errors.name.message}</p>}{errors.root && <p role="alert">{errors.root.message}</p>}<button disabled={isSubmitting}>Gửi mô phỏng</button></form>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Trộn lỗi root với lỗi field; hiển thị thành công trước khi Promise gửi hoàn tất.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: GitHub Lesson-03 và Lesson-06; roadmap Forms/Styling. PDF Props & State là nền tảng cho input; React Hook Form và Zod là phần mở rộng từ GitHub.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react-hook-form.com/get-started).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day07/Theory.md).
