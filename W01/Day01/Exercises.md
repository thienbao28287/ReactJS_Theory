# W01 · Day01 — Bài tập JavaScript nền tảng

Đọc [Theory](./Theory.md) trước. Làm 65 phút, sau đó dành 10 phút ghi kết quả. Bài hôm nay chạy trong Console trình duyệt; lưu lời giải vào `W01/Day01/practice.js` để giữ lại, không cần cài React.

## Bài 1 — Đọc và dự đoán (10 phút)

Chưa chạy code, hãy ghi kết quả hoặc lỗi của từng đoạn, sau đó chạy riêng từng đoạn để đối chiếu.

```js
const user = { name: 'An' };
user.name = 'Bao';
console.log(user.name);
```

```js
const price = 100;
price = 120;
```

```js
const multiply = (a, b) => { a * b; };
console.log(multiply(2, 4));
```

Đáp án kiểm tra sau khi làm: lần lượt là `Bao`, lỗi gán lại biến `const`, và `undefined`. Hãy sửa đoạn thứ ba để được `8`.

## Bài 2 — Tạo hồ sơ học viên (15 phút)

Tạo object `learner` có `name`, `age`, `city`, `skills`. Dùng destructuring lấy `name`, `city`, đồng thời đặt `role` mặc định là `Student`. Viết arrow function `describeLearner(learner)` trả về câu giới thiệu bằng template literal.

Đầu vào mẫu: `{ name: 'Bao', age: 20, city: 'Ha Noi', skills: ['HTML', 'CSS'] }`.

Kết quả mong đợi: `Bao đang học Frontend tại Ha Noi.`. Đổi tên/city trong đầu vào phải đổi được kết quả mà không sửa thân hàm.

## Bài 3 — Cập nhật không sửa bản gốc (20 phút)

Tạo `updatedLearner` từ `learner`: đổi city thành `Da Nang`, thêm `JavaScript` vào skills. Giữ nguyên city và skills của `learner`. Thử thêm object `address: { district: 'Cau Giay' }`, rồi tạo bản mới có district là `Hai Chau` mà bản cũ không đổi.

Điều kiện đạt:

- `learner.city` vẫn là `Ha Noi`.
- Mảng gốc vẫn có 2 kỹ năng; mảng mới có 3.
- `learner !== updatedLearner` là `true`.
- Sau bài nâng cấp address, district của bản gốc vẫn là `Cau Giay`.

Gợi ý: bạn cần sao chép riêng cấp array/object lồng nhau khi muốn cập nhật cấp đó.

## Bài 4 — Tách module trên giấy (10 phút)

Viết hai file `helpers.js`, `main.js`: file đầu export một hàm `getInitials(fullName)` bằng named export; file sau import và gọi hàm. Chỉ yêu cầu xử lý tên có hai từ, cách nhau một dấu cách: `getInitials('Thien Bao')` trả về `TB`. Ngày mai chạy bằng Node để xác nhận.

## Bài 5 — Giải thích lại (10 phút)

Không nhìn lý thuyết, viết vào `notes.md`:

1. Khi nào dùng `let`?
2. Destructuring khác spread ở đâu?
3. Vì sao spread không đủ để sao chép sâu?
4. Named import và default import khác nhau thế nào?

## Tiêu chí hoàn thành

- [ ] Tự viết được hàm nhận tham số và trả kết quả.
- [ ] Bài 2 đổi dữ liệu đầu vào vẫn chạy đúng.
- [ ] Bài 3 giữ nguyên dữ liệu gốc ở các cấp được yêu cầu.
- [ ] Đã lưu lời giải, kết quả dự đoán và ít nhất một lỗi mình gặp.

Nếu chưa đạt bài 2–3, dùng buổi ôn Day07 để làm lại; không cần học thêm cú pháp mới hôm nay.
