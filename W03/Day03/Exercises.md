# W03 · Day03 — Bài tập: Cleanup timer và event listener

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Dọn tài nguyên khi effect chạy lại hoặc component bị gỡ.

## Bài 1 — Timer (15 phút)

Chạy demo, ẩn rồi hiện lại; timer mới bắt đầu từ 0 và không tăng nhanh gấp đôi sau nhiều lần ẩn/hiện.

## Bài 2 — Listener (30 phút)

Tạo component hiển thị window.innerWidth; effect đăng ký resize và cleanup gỡ listener. Thử thu nhỏ, unmount, mount ba lần; mỗi event chỉ thực hiện một handler đang hoạt động.

## Bài 3 — Giải thích cleanup (20 phút)

Viết bảng setup→cleanup cho interval, timeout, listener. Tạm bỏ cleanup listener để quan sát bằng log rồi sửa ngay; ghi bằng chứng đã dọn đúng.

## Tự kiểm tra kết quả

- [ ] Ẩn timer dừng tài nguyên của instance cũ.
- [ ] Resize cập nhật chiều rộng chính xác.
- [ ] removeEventListener dùng cùng hàm đã đăng ký.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
