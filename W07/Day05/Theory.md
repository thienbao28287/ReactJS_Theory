# W07 · Day05 — Context + reducer cho giỏ hàng

## Mục tiêu và nhịp học

Xây CartProvider có thao tác thêm, xóa và đổi số lượng.

Thuộc tuần **Context và useReducer**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Không thêm thư viện. Các ví dụ Provider là module độc lập để thử; khi ghép vào ứng dụng, đặt Provider phía trên các component cần đọc Context. Đăng nhập tuần này chỉ là mô phỏng giao diện, không phải hệ thống xác thực thật.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Cart model

Mỗi dòng có id/title/price/quantity. Thêm cùng id phải tăng quantity thay vì tạo hai dòng. Không lưu total vào state nếu tính được từ items.

### 2. Provider làm cổng

Provider kết hợp reducer và Context. Component dùng useCart, không tự thao tác object store. Có thể tách state context và dispatch context để giảm phụ thuộc.

### 3. Bất biến

Reducer thường cần map/filter/spread. Không áp dụng cú pháp mutate như Redux Toolkit trước khi học Immer; useReducer không tự cung cấp draft.

## Ví dụ có thể thử

Module Provider: lưu src/context/CartContext.jsx, import CartProvider vào entry và useCart vào các consumer. Chỉ có named exports; không dùng default import.

```jsx
import { createContext, useContext, useReducer } from 'react';
const CartContext = createContext(undefined);
export function cartReducer(items, action) {
  if (action.type === 'add') {
    const product = action.product;
    const exists = items.some(item => item.id === product.id);
    return exists ? items.map(item => item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item) : [...items, { ...product, quantity: 1 }];
  }
  if (action.type === 'remove') return items.filter(item => item.id !== action.id);
  return items;
}
export function CartProvider({ children }) {
  const [items, dispatch] = useReducer(cartReducer, []);
  return <CartContext.Provider value={{ items, dispatch }}>{children}</CartContext.Provider>;
}
export function useCart() {
  const cart = useContext(CartContext);
  if (!cart) throw new Error('Thiếu CartProvider');
  return cart;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Mỗi route bọc CartProvider riêng khiến mỗi trang có một giỏ; lưu total riêng rồi bị lệch.

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

[Bài tiếp theo](../Day06/Theory.md).
