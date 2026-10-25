# W06 · Day03 — React Hook Form: register và handleSubmit

## Mục tiêu và nhịp học

Dùng RHF quản lý form và đọc dữ liệu hợp lệ khi submit.

Thuộc tuần **Styling, React Hook Form và Zod**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Trong dự án chạy npm install react-hook-form@7 zod@4 @hookform/resolvers và npm install -D tailwindcss@4 @tailwindcss/vite@4. Lưu package-lock.json. Chỉ thêm plugin Tailwind ở Day02; không cần cài lại mỗi ngày.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Đăng ký trường

register trả các liên kết name/ref/handler cho input. Không thêm value cố định hoặc ghi đè onChange mà bỏ handler của RHF.

### 2. handleSubmit

Wrapper xử lý validation rồi gọi onValid; có thể nhận onInvalid. Đây không phải onClick của nút; gắn vào form onSubmit.

### 3. defaultValues và lỗi

Khai báo defaultValues để có trạng thái ban đầu rõ. Đọc formState.errors hiển thị message; mode mặc định có thể đợi submit nên cần thử hành vi người dùng.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useForm } from 'react-hook-form';
export default function LessonDemo() {
  const { register, handleSubmit, formState: { errors } } = useForm({ defaultValues: { email: '' } });
  return <form noValidate onSubmit={handleSubmit(data => console.log({ email: data.email }))}><label htmlFor="email">Email</label><input id="email" type="email" {...register('email', { required: 'Email bắt buộc', pattern: { value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, message: 'Email chưa hợp lệ' } })} aria-invalid={Boolean(errors.email)} />{errors.email && <p role="alert">{errors.email.message}</p>}<button>Gửi</button></form>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Spread register xong ghi đè onChange/value vô tình; dùng tên trường khác giữa register và errors.

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

[Bài tiếp theo](../Day04/Theory.md).
