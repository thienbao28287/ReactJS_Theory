# W03 · Day07 — Bài tập: Lưu localStorage và tổng kết effects

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Lưu Todo an toàn và rà soát toàn bộ luồng tải dữ liệu.

## Bài 1 — Persist Todo (30 phút)

Áp dụng initializer và effect vào Todo W02. Dùng key riêng, parse JSON có try/catch và kiểm tra array cùng id/title/done trước khi nhận dữ liệu.

## Bài 2 — Kiểm tra hồi phục (20 phút)

Thử reload, storage trống, JSON hỏng, đúng JSON nhưng sai cấu trúc. App khởi động được và dùng fallback an toàn; không xóa toàn bộ localStorage của origin.

## Bài 3 — Tổng kết (15 phút)

Vẽ sơ đồ request từ mount tới cleanup. Liệt kê sáu ca đã kiểm tra trong tuần; giải thích effect nào cần thiết và phép tính nào không cần effect. Hoàn thiện bài còn thiếu.

## Tự kiểm tra kết quả

- [ ] Reload khôi phục đúng Todo.
- [ ] Storage hỏng không làm app crash.
- [ ] API có loading/error/empty, retry và cleanup.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
