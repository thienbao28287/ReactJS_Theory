# W10 · Day03 — Bài tập: React Testing Library: render và query

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Kiểm thử component qua role/label và chuẩn bị môi trường DOM.

## Bài 1 — Môi trường (15 phút)

Lưu demo thành Greeting.test.jsx trong src/labs, chạy npx vitest run. Xác nhận thiếu jsdom/matcher tạo lỗi gì, rồi giữ cấu hình đúng.

## Bài 2 — Test ProductCard (30 phút)

Import ProductCard thật; cung cấp product mẫu và callback cần thiết. Kiểm tra tên, giá và link đúng id; nếu dùng Link, bọc MemoryRouter. Không sửa app để chỉ khớp test giả.

## Bài 3 — Empty state (20 phút)

Test component danh sách với [] hiển thị thông báo và không có hàng sản phẩm. Dùng queryByRole cho phần tử không tồn tại, không viết getBy gây throw trước assertion.

## Tự kiểm tra kết quả

- [ ] Test DOM dùng jsdom và cleanup.
- [ ] Queries dựa trên role/label.
- [ ] ProductCard thật được kiểm tra với dependencies tối thiểu.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
