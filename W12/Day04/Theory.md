# W12 · Day04 — Zustand: store nhỏ và selectors

## Mục tiêu và nhịp học

Thử state manager khác trong lab và so sánh với Redux/Context.

Thuộc tuần **React nâng cao và tổng kết**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop và React/React DOM cùng major 19 cho các API React 19: kiểm tra npm ls react react-dom, nâng cùng nhau bằng npm install react@19 react-dom@19 nếu cần. Giữ react-router-dom@6 từ W05 cho Data Router. Làm các demo nâng cao trong module riêng, không thay state manager của dự án đã hoàn thiện.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Store tối giản

create tạo Hook chứa state/actions. set cập nhật bằng object hoặc hàm; merge nông nên object lồng nhau vẫn cần sao chép đúng cấp.

### 2. Selector nhỏ

Đọc primitive hoặc slice cần thiết thay vì cả store. Trong Zustand v5, selector tạo object mới liên tục cần chiến lược equality/useShallow phù hợp; bài này dùng selector primitive.

### 3. So sánh theo nhu cầu

Zustand gọn, Redux Toolkit có quy ước và hệ công cụ riêng; Context cấp dữ liệu trong cây React. Không chọn theo bảng dung lượng package thiếu bối cảnh và không đổi app chính chỉ để thử.

## Ví dụ có thể thử

Demo component độc lập; cài zustand@5 trước. Đối chiếu API chính thức tại https://github.com/pmndrs/zustand. Giữ lab tách khỏi Redux cart hiện có.

```jsx
import { create } from 'zustand';
const useCounterStore = create(set => ({ count: 0, add: () => set(state => ({ count: state.count + 1 })), reset: () => set({ count: 0 }) }));
function Badge() { const count = useCounterStore(state => state.count); return <p>Số lượng: {count}</p>; }
export default function LessonDemo() {
  const add = useCounterStore(state => state.add);
  const reset = useCounterStore(state => state.reset);
  return <section><Badge /><button onClick={add}>Thêm</button><button onClick={reset}>Reset</button></section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Store object lồng nhau bị ghi đè do nhầm merge sâu; đọc toàn store ở mọi component.

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

[Bài tiếp theo](../Day05/Theory.md).
