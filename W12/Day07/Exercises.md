# W12 · Day07 — Bài tập: Tự đánh giá 12 tuần và hướng phát triển

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tự trình bày dự án, nhận diện lỗ hổng và chọn bước học tiếp theo.

## Bài 1 — Demo không xem mẫu (30 phút)

Trình bày 10 phút: mở sản phẩm, lọc URL, xem chi tiết, thêm giỏ, reload, thử form sai/đúng và logout. Dùng 20 phút còn lại giải thích code của ba luồng bất kỳ.

## Bài 2 — Bài sửa nhỏ (20 phút)

Tự thêm một quy tắc: giới hạn quantity 10 thay 99, hoặc filter theo khoảng giá. Sửa logic/UI/test liên quan; không search lại toàn bộ lời giải. Khôi phục hoặc ghi rõ contract mới.

## Bài 3 — Tổng kết (15 phút)

Viết final-review.md: 5 kỹ năng có bằng chứng, 3 điểm còn yếu, phần chưa chạy và kế hoạch 2 tuần kế tiếp. Tự chấm theo hành vi thực tế, lưu mốc Git cuối.

## Tự kiểm tra kết quả

- [ ] Giải thích được luồng code không chỉ định nghĩa.
- [ ] Thay đổi nhỏ được phản ánh ở logic/UI/test.
- [ ] Có đánh giá trung thực và kế hoạch bù lỗ hổng.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
