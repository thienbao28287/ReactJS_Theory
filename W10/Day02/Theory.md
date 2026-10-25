# W10 · Day02 — Vitest và test reducer/selector

## Mục tiêu và nhịp học

Thiết lập runner Vite và kiểm tra giỏ bằng hàm thuần.

Thuộc tuần **Kiểm thử hành vi**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Day01 có bài Jest độc lập; từ Day02 dùng Vitest cho dự án Vite, không trộn hai runner trong cùng file test. Cài bằng npm install -D vitest jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom @testing-library/user-event. Đối chiếu yêu cầu Node/Vite của Vitest đang cài, lưu lockfile. Đây là tuần thực hành test, không chỉ đọc cú pháp.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Cấu hình tối thiểu

Vitest dùng cấu hình Vite cho transform. Với test hàm thuần không cần DOM; component test mới cần jsdom. Import test/expect từ vitest để tránh globals mơ hồ.

### 2. Store mới cho từng test

Không chia singleton store đã mutate giữa các ca. Test reducer bằng state đầu vào/action hoặc factory store, và kiểm tra input cũ không bị thay đổi.

### 3. Nghiệp vụ giỏ

Các ca add mới/trùng, quantity hợp lệ/sai, remove, tổng rỗng và tổng theo quantity bảo vệ hành vi W07/W08. Đừng chỉ test action creator trả object.

## Ví dụ có thể thử

Lưu src/features/cart/cartSlice.test.js; paths trong ví dụ giả định file test nằm cạnh cartSlice.js và actions giữ tên W08. Nếu tên khác, sửa import cho khớp code thực tế.

```js
import { describe, it, expect } from 'vitest';
import reducer, { addItem, removeItem } from './cartSlice.js';
describe('cart reducer', () => {
  it('gộp cùng id thành một dòng', () => {
    const product = { id: 1, title: 'Book', price: 80 };
    const first = reducer(undefined, addItem(product));
    const second = reducer(first, addItem(product));
    expect(second.items).toHaveLength(1);
    expect(second.items[0].quantity).toBe(2);
    expect(first.items[0].quantity).toBe(1);
  });
  it('xóa id không tồn tại giữ nội dung', () => {
    const initial = { items: [] };
    expect(reducer(initial, removeItem(99)).items).toEqual([]);
  });
});
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Dùng state/store chung cho mọi test; expected được tính lại bằng cùng hàm đang test.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: Roadmap Jest Unit Testing, React Testing Library và Cypress. Bài test ứng dụng giỏ hàng áp dụng kiến thức Redux trong PDF/GitHub.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://vitest.dev/guide/).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day03/Theory.md).
