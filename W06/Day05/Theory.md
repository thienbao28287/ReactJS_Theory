# W06 · Day05 — Zod: schema và validation

## Mục tiêu và nhịp học

Mô tả quy tắc dữ liệu bằng schema và đọc lỗi có cấu trúc.

Thuộc tuần **Styling, React Hook Form và Zod**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Trong dự án chạy npm install react-hook-form@7 zod@4 @hookform/resolvers và npm install -D tailwindcss@4 @tailwindcss/vite@4. Lưu package-lock.json. Chỉ thêm plugin Tailwind ở Day02; không cần cài lại mỗi ngày.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Schema là contract runtime

z.object định nghĩa trường, z.string/z.number định nghĩa kiểu và ràng buộc. TypeScript không tự kiểm tra JSON runtime; Zod xử lý việc đó, kể cả trong dự án JavaScript.

### 2. parse và safeParse

parse ném lỗi khi sai; safeParse trả success/data hoặc error. Không đọc result.data trước khi kiểm tra success. Zod error dùng issues cho chi tiết lỗi.

### 3. Số và xác nhận

Input HTML thường là chuỗi; chọn valueAsNumber hoặc chuyển đổi có kiểm tra. z.coerce.number có thể biến chuỗi rỗng thành 0 nên phải nghĩ kỹ. refine cho confirm password, gắn lỗi vào confirm.

## Ví dụ có thể thử

Lưu src/schemas/registerSchema.js và import từ module trong app. Module dùng package zod@4; ví dụ có console.log chỉ cho kết quả boolean, không in dữ liệu nhạy cảm.

```js
import { z } from 'zod';
export const registerSchema = z.object({
  email: z.string().trim().email('Email chưa hợp lệ'),
  password: z.string().min(8, 'Tối thiểu 8 ký tự'),
  confirm: z.string(),
}).refine(data => data.password === data.confirm, { message: 'Mật khẩu chưa khớp', path: ['confirm'] });
const result = registerSchema.safeParse({ email: 'bao@example.com', password: 'learning123', confirm: 'learning123' });
console.log(result.success);
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Dùng lỗi .errors theo ví dụ khác phiên bản khi API đang dùng .issues; coi mọi input số đã là number.

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

[Bài tiếp theo](../Day06/Theory.md).
