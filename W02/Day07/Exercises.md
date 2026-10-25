# W02 · Day07 — Bài tập: Tổng kết Props–State và Todo

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tự xây lại luồng Todo và giải thích vị trí State, callback và dữ liệu suy ra.

## Bài 1 — Tự làm lại (30 phút)

Không xem code cũ, dựng TodoForm và callback thêm Todo vào danh sách cha. Sau 20 phút mới đối chiếu nếu vướng. Giữ chức năng Enter, trim và id ổn định.

## Bài 2 — Kiểm tra luồng (20 phút)

Chạy ít nhất sáu ca: thêm hợp lệ, thêm rỗng, sửa/hủy, toggle, xóa hết, lọc không có kết quả. Ghi thao tác và kết quả vào review.md.

## Bài 3 — Giải thích kiến trúc (15 phút)

Vẽ cây component và nơi đặt todos, filter, input. Trả lời vì sao không sửa Props, vì sao cần key, vì sao không await setter. Đọc git diff rồi lưu bài.

## Tự kiểm tra kết quả

- [ ] Tự viết lại được form/callback không chép mẫu.
- [ ] Sáu ca thao tác có kết quả thực tế.
- [ ] Giải thích được state gốc và dữ liệu tính từ state.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
