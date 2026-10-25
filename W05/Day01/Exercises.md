# W05 · Day01 — Bài tập: Router, Routes và Route

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Thiết lập ứng dụng nhiều URL với một Router duy nhất.

## Bài 1 — Router đầu tiên (15 phút)

Chạy demo ở / và /products; quan sát URL và nội dung. Kiểm tra không có lỗi Router lồng nhau.

## Bài 2 — Ghép mini-shop (30 phút)

Tạo HomePage, ProductsPage và CartPage. Đưa ProductsPage W04 vào /products, giữ Header/Nav ngoài Routes để dùng chung.

## Bài 3 — Kiểm tra history (20 phút)

Chuyển ba trang, dùng Back/Forward; nội dung khớp URL. Thử nhập URL trực tiếp ở local dev và ghi khác biệt với host static chưa cấu hình fallback.

## Tự kiểm tra kết quả

- [ ] Ba route mở đúng nội dung.
- [ ] Có đúng một Router gốc.
- [ ] Back/Forward không lệch màn hình.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
