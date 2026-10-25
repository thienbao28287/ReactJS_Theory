# W07 · Day02 — Bài tập: Context API và useContext

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Cung cấp dữ liệu qua Provider và phát hiện khi thiếu Provider.

## Bài 1 — Provider (15 phút)

Chạy demo; thử gỡ Provider rồi đọc lỗi rõ ràng, sau đó khôi phục. Ghi useContext tìm Provider gần nhất như thế nào.

## Bài 2 — Tách context (30 phút)

Tạo ThemeProvider và useTheme trong module riêng. Hai component xa nhau đọc cùng theme; button đổi theme phải cập nhật cả hai.

## Bài 3 — Phạm vi (20 phút)

Đặt hai ThemeProvider độc lập để thử state tách biệt. Giải thích vì sao Provider chỉ bao một phần cây không cấp dữ liệu cho component ngoài nó.

## Tự kiểm tra kết quả

- [ ] Consumer đọc đúng Provider.
- [ ] Thiếu Provider báo lỗi mô tả.
- [ ] Hai component trong cùng Provider cập nhật đồng bộ.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
