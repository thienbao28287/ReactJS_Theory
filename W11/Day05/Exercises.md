# W11 · Day05 — Bài tập: Conflict, README và bàn giao

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Giải quyết conflict có hiểu nội dung và viết hướng dẫn tái hiện dự án.

## Bài 1 — Conflict lab (25 phút)

Trong W11/git-conflict-lab tạo repository riêng với một file note. Tạo hai nhánh sửa cùng một dòng khác nhau, commit rồi merge để sinh conflict. Nếu thư mục đã tồn tại thì chọn tên lab mới, không ghi đè.

## Bài 2 — Giải quyết (20 phút)

Đọc markers, ghép nội dung theo yêu cầu do bạn ghi trước; git add file rồi commit merge. Ghi log ngắn chứng minh hai thay đổi cần thiết còn tồn tại.

## Bài 3 — README (20 phút)

Viết README mini-shop theo tình trạng thật. Nhờ chính bạn làm lại từ terminal mới bằng hướng dẫn đó; ghi các bước còn thiếu và sửa tài liệu.

## Tự kiểm tra kết quả

- [ ] Conflict được tạo và giải thích trên repo lab riêng.
- [ ] File cuối không còn markers và giữ ý định hai nhánh.
- [ ] README có đường dẫn chạy/fixture/test/giới hạn đúng.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
