# W07 · Day07 — Bài tập: Tổng kết kiến trúc Context và reducer

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tự giải thích và kiểm tra giỏ hàng dùng chung nhiều route.

## Bài 1 — Luồng đa trang (30 phút)

Từ danh sách thêm Book hai lần, mở chi tiết thêm Pen, tới Cart đổi quantity và xóa. Header, Cart và reload phải nhất quán.

## Bài 2 — Ma trận reducer (20 phút)

Viết/chạy ít nhất sáu ca: add mới, add trùng, quantity hợp lệ, quantity sai, remove, action không biết. Ghi state trước/sau và xác nhận không mutation.

## Bài 3 — Tổng kết (15 phút)

Vẽ cây Provider/consumer, mô tả persistence và auth mô phỏng. Tạo mốc Git cho bản Context trước khi chuyển Redux để có thể so sánh.

## Tự kiểm tra kết quả

- [ ] Giỏ nhất quán qua route và reload.
- [ ] Có sáu ca reducer đã kiểm tra.
- [ ] Giải thích được state scope và giới hạn auth/giá client.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
