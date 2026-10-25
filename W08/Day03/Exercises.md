# W08 · Day03 — Bài tập: useSelector, useDispatch và chuyển giỏ hàng

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Chuyển UI từ CartContext sang Redux mà giữ nguyên hành vi.

## Bài 1 — Hoàn thiện slice (15 phút)

Thêm setQuantity với payload {id, quantity}, kiểm tra số nguyên 1–99. Giữ same-id không tạo dòng trùng.

## Bài 2 — Chuyển UI (30 phút)

Header dùng selector count, ProductCard dispatch addItem, CartPage dùng items/remove/setQuantity. Gỡ CartProvider và import useCart khỏi các component đã chuyển.

## Bài 3 — So sánh (20 phút)

Chạy lại chuỗi Book×2, Pen×1 tổng 170 từ W07. Bấm action trong DevTools để đọc state, xác nhận không có state cart thứ hai.

## Tự kiểm tra kết quả

- [ ] Hành vi giỏ không đổi sau chuyển.
- [ ] Không còn consumer dùng CartContext cũ.
- [ ] Quantity sai không được nhận.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
