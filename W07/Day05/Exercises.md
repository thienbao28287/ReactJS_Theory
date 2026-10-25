# W07 · Day05 — Bài tập: Context + reducer cho giỏ hàng

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Xây CartProvider có thao tác thêm, xóa và đổi số lượng.

## Bài 1 — Reducer add/remove (15 phút)

Chạy cartReducer ngoài UI: thêm Book hai lần phải một dòng quantity=2; xóa theo id làm mất đúng dòng.

## Bài 2 — Ghép UI (30 phút)

ProductCard dispatch add; CartPage render items, Header tính tổng quantity. Thêm action setQuantity chấp nhận số nguyên 1–99, input sai không làm state hỏng.

## Bài 3 — Tổng tiền (20 phút)

Tính tổng từ price*quantity, thêm trạng thái empty và nút xóa. Thử Book giá 80 quantity 2, Pen giá 10 quantity 1: tổng 170.

## Tự kiểm tra kết quả

- [ ] Thêm trùng id tăng quantity.
- [ ] Header và CartPage đồng bộ qua Provider.
- [ ] Giá trị quantity không hợp lệ bị từ chối.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
