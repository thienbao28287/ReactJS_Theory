# W08 · Day04 — State structure, selectors và DevTools

## Mục tiêu và nhịp học

Tổ chức slice theo tính năng, tính dữ liệu suy ra và đọc lịch sử action.

Thuộc tuần **Redux Toolkit và async state**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop; npm install @reduxjs/toolkit@2 react-redux@9. Chỉ giữ một nguồn dữ liệu giỏ hàng: sau khi chuyển sang Redux, gỡ việc dùng CartContext ở giao diện tương ứng. Demo tự có Provider; khi ghép app thật, dùng Provider duy nhất ở entry.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Dữ liệu serializable

State/action nên chứa dữ liệu plain để debug và persist; không lưu DOM node, function hay Promise. Một Date thường chuyển ISO string nếu cần lưu.

### 2. Selectors

Hàm selectCartTotal tính từ items; selector trả primitive có so sánh dễ. Memoized selector hữu ích khi phép suy ra tạo array/object hoặc tốn công, không bắt buộc cho mọi phép cộng.

### 3. Persistence store

Khởi tạo preloadedState bằng dữ liệu validated và subscribe ghi cart. Subscription không nên lưu toàn bộ product request/error nếu không có yêu cầu persistence.

## Ví dụ có thể thử

Lưu src/features/cart/cartSelectors.js. Nếu cùng module đã export selectCartItems thì tái sử dụng/export lại rõ ràng, không khai báo trùng tên trong một file.

```js
import { createSelector } from '@reduxjs/toolkit';
export const selectCartItems = state => state.cart.items;
export const selectCartCount = createSelector([selectCartItems], items => items.reduce((sum, item) => sum + item.quantity, 0));
export const selectCartTotal = createSelector([selectCartItems], items => items.reduce((sum, item) => sum + item.price * item.quantity, 0));
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Lưu state function/DOM vào store; truyền items trực tiếp vào preloadedState khi store cần cart.items.

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

[Bài tiếp theo](../Day05/Theory.md).
