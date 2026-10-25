# W07 · Day02 — Context API và useContext

## Mục tiêu và nhịp học

Cung cấp dữ liệu qua Provider và phát hiện khi thiếu Provider.

Thuộc tuần **Context và useReducer**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Không thêm thư viện. Các ví dụ Provider là module độc lập để thử; khi ghép vào ứng dụng, đặt Provider phía trên các component cần đọc Context. Đăng nhập tuần này chỉ là mô phỏng giao diện, không phải hệ thống xác thực thật.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Tạo và cung cấp

createContext tạo kênh; Provider cấp value cho subtree; useContext đọc Provider gần nhất. Default value không tự thay đổi khi app thay đổi.

### 2. Consumer cập nhật

Khi Provider value đổi, consumer đọc Context đó có thể render lại. Context không tự memo hóa hoặc thay thế mọi hình thức truyền Props.

### 3. Hook truy cập an toàn

Default undefined và Hook kiểm tra thiếu Provider cho lỗi rõ. Không âm thầm dùng giá trị giả khiến UI tưởng đã có dữ liệu hợp lệ.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { createContext, useContext, useState } from 'react';
const ThemeContext = createContext(undefined);
function useTheme() {
  const value = useContext(ThemeContext);
  if (value === undefined) throw new Error('Cần ThemeProvider');
  return value;
}
function ThemeButton() {
  const { theme, toggle } = useTheme();
  return <button onClick={toggle}>Giao diện: {theme}</button>;
}
export default function LessonDemo() {
  const [theme, setTheme] = useState('light');
  return <ThemeContext.Provider value={{ theme, toggle: () => setTheme(t => t === 'light' ? 'dark' : 'light') }}><ThemeButton /></ThemeContext.Provider>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Tạo Context bên trong component; nghĩ defaultValue là state chung có thể cập nhật.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: Hook Trong ReactJS (2).pdf, trang 5–9; GitHub Lesson-08; roadmap useContext, useReducer, Context API Advanced.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/learn/scaling-up-with-reducer-and-context).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day03/Theory.md).
