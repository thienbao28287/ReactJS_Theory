# W02 · Day05 — Điều kiện, lists và key

## Mục tiêu và nhịp học

Hiển thị trạng thái rỗng và danh sách có key ổn định.

Thuộc tuần **Props, State và tương tác**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng tiếp W01/react-profile. Chạy npm run dev trong dự án đó. Ví dụ React độc lập có thể đặt ở src/LessonDemo.jsx rồi import vào App để thử; giữ lại trang hồ sơ cũ. Không cần thư viện mới.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Biểu thức điều kiện

Dùng if trước return, ternary hoặc && cho phần UI tùy điều kiện. Với số lượng, viết items.length > 0 thay vì items.length && để tránh render số 0 ngoài ý muốn.

### 2. Danh sách bằng map

Mỗi phần tử trả về phải có key trong nhóm anh em. Dùng id từ dữ liệu; key không tự được chuyển thành Props, hãy truyền id riêng nếu component cần.

### 3. Giữ danh tính

Key ổn định giúp React theo dõi item qua thêm/xóa/sắp xếp. Math.random trong render tạo danh tính mới; index không phù hợp danh sách có thể đổi thứ tự.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useState } from 'react';
export default function LessonDemo() {
  const [items, setItems] = useState([{ id: 'a', title: 'JSX' }, { id: 'b', title: 'Props' }]);
  return <section>{items.length === 0 ? <p>Chưa có bài học</p> : <ul>{items.map(item => <li key={item.id}>{item.title}<button onClick={() => setItems(list => list.filter(x => x.id !== item.id))}>Xóa {item.title}</button></li>)}</ul>}</section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Đặt key bên trong TodoItem thay vì tại vị trí map; filter trực tiếp thành state làm mất item ẩn.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: ReactJS_state_props (1).pdf, trang 2–8; GitHub Lesson-02; roadmap Props/State, Event Handling, Lists và Keys.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/learn/adding-interactivity).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day06/Theory.md).
