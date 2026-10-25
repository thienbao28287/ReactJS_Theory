# W09 · Day02 — Bài tập: Profiler và phương pháp đo

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Ghi bằng chứng hiệu năng bằng React DevTools/Profiler.

## Bài 1 — Ghi profile (15 phút)

Cài/mở React DevTools, record một chuỗi gõ input. Nếu không dùng extension được, thử Profiler onRender trong demo.

## Bài 2 — Đo catalog (30 phút)

Record thao tác lọc ở dataset cố định; chạy ít nhất ba lần. Ghi component nổi bật, thời gian tương đối và điều kiện đo vào notes.

## Bài 3 — Đặt giả thuyết (20 phút)

Chọn một giả thuyết kiểm chứng được: props callback mới, tính toán lặp hoặc state đặt quá cao. Ghi phép thay đổi và kết quả kỳ vọng, chưa thay nhiều thứ cùng lúc.

## Tự kiểm tra kết quả

- [ ] Có ít nhất ba lần đo cùng điều kiện.
- [ ] Giả thuyết chỉ rõ component và nguyên nhân.
- [ ] Không kết luận production nhanh hơn từ log development.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
