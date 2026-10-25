# W12 · Day06 — Bài tập: Hoàn thiện sản phẩm và bản phát hành học tập

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Đưa ứng dụng chính về trạng thái nhất quán và kiểm chứng toàn bộ luồng.

## Bài 1 — Sửa và dọn (30 phút)

Đọc todo/notes các tuần, sửa lỗi cốt lõi còn mở. Bỏ import lab gây side effect, file asset không dùng và log chứa dữ liệu form.

## Bài 2 — Chạy xác nhận (20 phút)

Chạy Vitest, Cypress với server, npm run build/preview và smoke test bản deploy nếu có. Lưu lệnh/kết quả; nếu chưa đủ môi trường ghi rõ phần chưa kiểm chứng.

## Bài 3 — Bàn giao (15 phút)

Cập nhật README, env mẫu, sơ đồ dữ liệu và known limitations. Nếu tự deploy bản mới, xác nhận link thật và thời điểm kiểm tra; không bắt buộc mua domain hay dịch vụ.

## Tự kiểm tra kết quả

- [ ] App chính chỉ dùng một phương án cho mỗi nguồn dữ liệu.
- [ ] Có kết quả kiểm tra thật và danh sách giới hạn.
- [ ] README khớp phiên bản cuối, không thông tin giả về triển khai.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
