# W08 · Day01 — Redux Core và luồng một chiều

## Mục tiêu và nhịp học

Nắm Store–Action–Reducer và phân biệt Redux với React Redux.

Thuộc tuần **Redux Toolkit và async state**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop; npm install @reduxjs/toolkit@2 react-redux@9. Chỉ giữ một nguồn dữ liệu giỏ hàng: sau khi chuyển sang Redux, gỡ việc dùng CartContext ở giao diện tương ứng. Demo tự có Provider; khi ghép app thật, dùng Provider duy nhất ở entry.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Ba phần cốt lõi

Store giữ state; action mô tả sự kiện; reducer tính state mới. UI dispatch, store xử lý đồng bộ reducer, subscriber nhận thay đổi; async sẽ do middleware/thunk đảm nhiệm.

### 2. Vai trò các package

Redux Toolkit cung cấp cách cấu hình và tạo reducer/action; react-redux nối React với store qua Provider/Hooks. Redux có thể dùng ngoài React.

### 3. Không toàn cục mọi thứ

Giỏ dùng chung hợp lý cho store; bản nháp input vẫn có thể local. Dữ liệu server cần trạng thái và cache riêng; không sao chép mọi response vào nhiều slice.

## Ví dụ có thể thử

Module thí nghiệm: src/labs/reduxCore.js, import một lần để quan sát Console; không phải React component. Sau thử nghiệm bỏ import log khỏi app chính.

```js
import { configureStore } from '@reduxjs/toolkit';
function reducer(state = { count: 0 }, action) {
  if (action.type === 'counter/increment') return { count: state.count + 1 };
  return state;
}
const store = configureStore({ reducer });
const unsubscribe = store.subscribe(() => console.log(store.getState()));
store.dispatch({ type: 'counter/increment' });
unsubscribe();
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Nhầm reducer làm gọi API; giữ đồng thời Redux cart và Context cart làm hai nguồn dữ liệu.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: React-redux.pdf, trang 2–11; GitHub Lesson-09; roadmap Redux Toolkit. RTK Query và typed hooks là phần mở rộng.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://redux.js.org/tutorials/quick-start).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day02/Theory.md).
