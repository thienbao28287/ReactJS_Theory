# W07 · Day06 — Persist giỏ hàng và derived data

## Mục tiêu và nhịp học

Khôi phục giỏ an toàn và tính count/total từ một nguồn dữ liệu.

Thuộc tuần **Context và useReducer**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Không thêm thư viện. Các ví dụ Provider là module độc lập để thử; khi ghép vào ứng dụng, đặt Provider phía trên các component cần đọc Context. Đăng nhập tuần này chỉ là mô phỏng giao diện, không phải hệ thống xác thực thật.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Khởi tạo reducer

Tham số initializer của useReducer đọc storage khi tạo state. Validate từng dòng, không chỉ Array.isArray; schema sai cần fallback an toàn.

### 2. Persist có version

Dùng key riêng và lưu {version, items} để dễ thay model. Effect ghi khi items đổi; không xóa storage của các tính năng khác.

### 3. Giá ở client

Giá và tổng trong app học là hiển thị ước tính. Hệ thống bán hàng thật cần Backend xác minh giá/tồn kho, không tin tổng browser gửi lên.

## Ví dụ có thể thử

Module thuần cho browser: lưu src/lib/cartStorage.js. Khi gọi trong môi trường SSR/test không có localStorage cần môi trường hoặc dependency tương ứng.

```js
export function isCartItem(item) {
  return item !== null && typeof item === 'object' && ['string', 'number'].includes(typeof item.id) && typeof item.title === 'string' && Number.isFinite(item.price) && item.price >= 0 && Number.isInteger(item.quantity) && item.quantity >= 1 && item.quantity <= 99;
}
export function readCart() {
  try {
    const saved = JSON.parse(localStorage.getItem('mini-shop-cart-v1') ?? 'null');
    return saved?.version === 1 && Array.isArray(saved.items) && saved.items.every(isCartItem) ? saved.items : [];
  } catch { return []; }
}
export function cartTotal(items) { return items.reduce((sum, item) => sum + item.price * item.quantity, 0); }
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Tin toàn bộ JSON trong storage; ghi [] trước khi đọc dữ liệu cũ.

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

[Bài tiếp theo](../Day07/Theory.md).
