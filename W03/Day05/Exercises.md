# W03 · Day05 — Bài tập: Loading, error, empty và retry

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Thiết kế bốn trạng thái request và cơ chế thử lại không tạo vòng lặp.

## Bài 1 — Bốn trạng thái (15 phút)

Dùng Network throttling, fixture [], dữ liệu hợp lệ và đường dẫn lỗi để chụp/ghi từng trạng thái UI.

## Bài 2 — Retry (30 phút)

Áp dụng retry vào ProductList Day04. Lỗi xong sửa fixture rồi click thử lại; error cũ mất và danh sách mới hiện. Nút không gửi request lặp khi đang loading.

## Bài 3 — Thiết kế thông báo (20 phút)

Viết thông báo phân biệt không có sản phẩm với không tải được sản phẩm. Kiểm tra trạng thái loading/error có role phù hợp và không dùng alert popup chặn tương tác.

## Tự kiểm tra kết quả

- [ ] Empty chỉ xuất hiện sau request thành công.
- [ ] Retry hồi phục được sau lỗi.
- [ ] Không có request loop do effect tự cập nhật dependency.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
