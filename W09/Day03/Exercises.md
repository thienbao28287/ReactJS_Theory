# W09 · Day03 — Bài tập: React.memo và tham chiếu Props

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Dùng memo có mục đích và hiểu các đường render còn lại.

## Bài 1 — Memo primitive (15 phút)

Chạy demo và quan sát qua Profiler. Đổi title sau một thao tác riêng để xác nhận nội dung vẫn cập nhật.

## Bài 2 — Tham chiếu (30 phút)

Thử truyền object info={{title:"Book"}} vào child memo, so với title primitive. Ghi ảnh hưởng tham chiếu mới; không viết custom comparator vội.

## Bài 3 — State riêng (20 phút)

Thêm state mở chi tiết trong child memo. Click child vẫn render đúng dù Props không đổi; giải thích vì sao đây không phải memo hỏng.

## Tự kiểm tra kết quả

- [ ] Memo không làm mất cập nhật nội dung.
- [ ] Giải thích được object reference mới.
- [ ] Phân biệt parent render với state/Context update.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
