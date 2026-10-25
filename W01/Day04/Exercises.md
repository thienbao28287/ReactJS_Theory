# W01 · Day04 — Bài tập JSX

Thực hành 65 phút trong `W01/react-profile`. Đọc [Theory](./Theory.md). Sau mỗi bài, mở Console kiểm tra lỗi và thử tải lại trang.

## Bài 1 — Chuyển HTML sang JSX (15 phút)

Đoạn sau là HTML cần chuyển, không dán nguyên vào component:

```html
<section class="profile">
  <h1>Hồ sơ học tập</h1>
  <label for="learner-name">Tên học viên</label>
  <input id="learner-name" type="text">
  <br>
  <p>Học React mỗi ngày</p>
</section>
```

Viết component `App` trả về JSX tương ứng. Đổi thuộc tính đúng cú pháp, đóng đủ thẻ. Chưa cần xử lý input; mục tiêu là cú pháp và liên kết label/input.

Kết quả: không có lỗi JSX; bấm label sẽ focus input.

## Bài 2 — Đưa dữ liệu vào giao diện (20 phút)

Trong thân component tạo `profile` có `name`, `city`, `goal`, `hoursPerDay`. Hiển thị tên trong h1, thành phố, mục tiêu, số giờ mỗi ngày và tổng giờ mỗi tuần bằng biểu thức tính toán.

Với `hoursPerDay = 2`, giao diện hiển thị `14 giờ/tuần`. Thay `3` phải thành `21 giờ/tuần`. Không gõ cứng kết quả phép tính. Thêm link có URL lấy từ biến `docsUrl = 'https://react.dev'`.

## Bài 3 — Fragment và style (10 phút)

Để Header và Main ngang hàng trong kết quả `return`, dùng Fragment. Kiểm tra Elements để xác nhận không xuất hiện thẻ mang tên Fragment. Tạo object style cho một dòng nhấn mạnh; các phần còn lại dùng CSS file.

## Bài 4 — Sửa lỗi và giải thích (20 phút)

Đoạn sau cố ý sai. Viết lại thành một component chạy được, sau đó ghi ít nhất bốn lỗi đã sửa:

```jsx
function BrokenProfile() {
  const profile = { name: 'Bao' };
  return (
    <h1 class="title">profile.name</h1>
    <p>{profile}</p>
    <input type="text">
    <p style="color: blue">Đang học</p>
  );
}
```

Kết quả mong đợi: hiển thị `Bao`, một dòng thông tin hợp lệ, input và dòng chữ màu xanh. Gợi ý: kiểm tra phần tử bao ngoài, biểu thức, object, thuộc tính và đóng thẻ. Đây là mẫu chẩn đoán lỗi, không phải lời giải mẫu để giữ lại nguyên trạng.

## Tiêu chí hoàn thành

- [ ] Thay đổi dữ liệu JavaScript làm thay đổi nội dung sau khi lưu.
- [ ] Phân biệt được chuỗi `profile.name` và biểu thức `{profile.name}`.
- [ ] Hiểu tại sao không render trực tiếp object `profile`.
- [ ] Có semantic HTML, nhãn input và CSS được import đúng.
- [ ] Console không có lỗi/cảnh báo do các bài hôm nay.
