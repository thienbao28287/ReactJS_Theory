# W01 · Day02 — Bài tập array, async và Vite

Thời lượng thực hành: 65 phút. Đọc [Theory](./Theory.md) để biết thư mục chạy lệnh. Lưu bài JS vào `W01/Day02/practice.mjs`, chạy từ gốc bằng `node W01/Day02/practice.mjs` sau khi cài Node.

## Bài 1 — Biến đổi sản phẩm (20 phút)

Dùng dữ liệu sau:

```js
const products = [
  { id: 1, name: 'Book', price: 80000, inStock: true },
  { id: 2, name: 'Pen', price: 10000, inStock: false },
  { id: 3, name: 'Bag', price: 200000, inStock: true },
];
```

Viết các hàm:

1. `getProductNames(items)` → `['Book', 'Pen', 'Bag']`.
2. `getAvailableProducts(items)` → sản phẩm id 1 và 3.
3. `findProductById(items, id)` → object phù hợp; id 99 trả `undefined`.
4. `applyDiscount(items, percent)` → array mới, mỗi giá giảm phần trăm tương ứng. Với `10`, giá lần lượt là `72000`, `9000`, `180000`.

Thử với array rỗng; các hàm trả array phải trả `[]`. Bài giảm giá giả định `percent` trong 0–100. Kiểm tra giá gốc vẫn là `80000`, `10000`, `200000`.

## Bài 2 — Chờ kết quả và bắt lỗi (10 phút)

Chạy ví dụ `loadCourse` trong Theory. Gọi `showCourse(false)`, sau đó thử `showCourse(true)`; xác nhận cả nhánh thành công và lỗi. Thử bỏ `await` trước `loadCourse` rồi ghi lại sự khác nhau; khôi phục code sau khi thử.

Kết quả cần hiểu: lời gọi thành công in tên khóa học sau khoảng chờ; lời gọi thất bại in thông báo lỗi, không để Promise rejection bị bỏ quên.

## Bài 3 — Chạy React đầu tiên (25 phút)

1. Kiểm tra `node -v`, `npm -v`.
2. Tạo `W01/react-profile` theo Theory; nếu đã có thì dùng lại, không ghi đè dự án.
3. Cài package, chạy dev server, mở URL terminal đưa ra.
4. Trong `src/App.jsx`, thay component mặc định bằng:

```jsx
export default function App() {
  return <h1>Xin chào, tôi đang học React!</h1>;
}
```

5. Đổi nội dung và lưu; xác nhận trình duyệt cập nhật.
6. Dừng server rồi chạy lại để biết cách tiếp tục vào ngày mai.

## Bài 4 — Chạy module Day01 (10 phút)

Thực hiện hướng dẫn `.mjs` trong Theory, chạy hàm `getInitials('Thien Bao')`. Kết quả phải là `TB`. Viết vào `notes.md`: Node, npm, Vite, React khác nhau ở đâu; ghi lại phiên bản công cụ đang dùng.

## Tiêu chí hoàn thành

- [ ] Bốn hàm array đúng dữ liệu mẫu và trường hợp rỗng.
- [ ] Hiểu vì sao phải kiểm tra kết quả `find` trước khi đọc thuộc tính.
- [ ] Đã chạy cả nhánh thành công và thất bại của tác vụ async.
- [ ] Dự án `W01/react-profile` chạy được, sửa tiêu đề thấy kết quả.
- [ ] Biết dừng và khởi động lại dev server.

Nếu cài công cụ mất quá nhiều thời gian, ưu tiên dự án chạy được; ghi bài async chưa xong để bù Day07.
