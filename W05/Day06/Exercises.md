# W05 · Day06 — Bài tập: Protected route và 404

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Bảo vệ luồng UI mô phỏng mà không nhầm với phân quyền Backend.

## Bài 1 — Guard cơ bản (15 phút)

Mở /account khi signedIn=false; phải tới /login. Sau click đăng nhập, mở lại /account để xem nhánh được phép.

## Bài 2 — Luồng đầy đủ (30 phút)

Trong dự án, login thành công tự quay về URL nội bộ đã yêu cầu hoặc /account. Thêm logout; sau logout không xem được account. Chưa lưu mật khẩu/token vào storage.

## Bài 3 — 404 (20 phút)

Thử /khong-ton-tai, link về trang chủ và refresh account. Viết rõ guard UI không thay kiểm tra quyền Backend; trạng thái mô phỏng mất khi reload là giới hạn hiện tại.

## Tự kiểm tra kết quả

- [ ] Chưa đăng nhập không thấy nội dung account.
- [ ] Đăng nhập quay đúng đích nội bộ, logout bảo vệ lại.
- [ ] URL lạ có 404 và link hồi phục.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
