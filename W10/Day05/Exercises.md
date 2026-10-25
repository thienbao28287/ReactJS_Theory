# W10 · Day05 — Bài tập: Test validation và loading/error

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Kiểm tra form và request với Promise/mạng được điều khiển.

## Bài 1 — Request (15 phút)

Chạy demo, thêm nhánh thành công bằng mockResolvedValue. Ghi lý do load phải giữ tham chiếu ổn định khi truyền Props.

## Bài 2 — Form thật (30 phút)

Viết test Checkout: submit rỗng có lỗi, không gọi service; dữ liệu hợp lệ gọi service một lần; reject giữ input và hiện lỗi. Dùng tên field/label thật từ W06.

## Bài 3 — Bốn trạng thái (20 phút)

Test trang sản phẩm với mock service cho loading, [], data và reject. Restore mock sau test; dùng findBy/waitFor thay sleep cố định.

## Tự kiểm tra kết quả

- [ ] Invalid form không gọi service.
- [ ] API state được điều khiển, không phụ thuộc mạng thật.
- [ ] Có test lỗi và thử lại hoặc giữ input.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
