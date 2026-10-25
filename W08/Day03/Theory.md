# W08 · Day03 — useSelector, useDispatch và chuyển giỏ hàng

## Mục tiêu và nhịp học

Chuyển UI từ CartContext sang Redux mà giữ nguyên hành vi.

Thuộc tuần **Redux Toolkit và async state**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop; npm install @reduxjs/toolkit@2 react-redux@9. Chỉ giữ một nguồn dữ liệu giỏ hàng: sau khi chuyển sang Redux, gỡ việc dùng CartContext ở giao diện tương ứng. Demo tự có Provider; khi ghép app thật, dùng Provider duy nhất ở entry.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Chọn đúng phần state

useSelector đăng ký phần dữ liệu cần. Trả object/array mới mỗi lần có thể gây render không cần thiết; trước tiên chọn items hoặc primitive rõ ràng.

### 2. Dispatch action creator

dispatch(addItem(product)) gửi action đã có payload. Không dispatch(addItem) trừ khi đó thực sự là thunk; action creator thường cần được gọi.

### 3. Chuyển từng ranh giới

Giữ API UI dễ đọc, chuyển Header/ProductCard/CartPage sang cùng store rồi bỏ CartProvider. Persistence chuyển sau; hôm nay so sánh hành vi trước/sau.

## Ví dụ có thể thử

Lưu src/features/cart/cartSlice.js. Tại store cấu hình reducer: { cart: cartReducer }; các component import named actions/selectors và dùng React Redux hooks.

```js
import { createSlice } from '@reduxjs/toolkit';
const cartSlice = createSlice({
  name: 'cart', initialState: { items: [] },
  reducers: {
    addItem(state, { payload }) {
      const item = state.items.find(x => x.id === payload.id);
      if (item) item.quantity += 1;
      else state.items.push({ ...payload, quantity: 1 });
    },
    removeItem(state, { payload: id }) { state.items = state.items.filter(item => item.id !== id); },
    clearCart(state) { state.items = []; },
  },
});
export const { addItem, removeItem, clearCart } = cartSlice.actions;
export default cartSlice.reducer;
export const selectCartItems = state => state.cart.items;
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Chuyển một nửa UI rồi cố sync Context với Redux bằng effect.

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

[Bài tiếp theo](../Day04/Theory.md).
