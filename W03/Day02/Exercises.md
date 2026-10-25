# W03 · Day02 — Bài tập: Dependency array và stale closure

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Viết effect có đủ dependencies và hiểu dữ liệu bị chụp ở lần render nào.

## Bài 1 — Dự đoán thời điểm (15 phút)

Gõ liên tiếp ba ký tự; dự đoán log trước khi chạy. Giải thích tại sao cleanup timeout cũ làm chỉ còn giá trị cuối sau thời gian chờ.

## Bài 2 — Thực nghiệm dependency (30 phút)

Thử tạm bỏ query khỏi dependencies rồi đổi input; ghi hành vi stale. Khôi phục dependency và thêm một state khác không liên quan để kiểm tra nó không khởi động lại timer.

## Bài 3 — Sửa effect dư thừa (20 phút)

Tạo firstName/lastName bằng state, tính fullName ngay trong render. Giải thích vì sao không cần effect và state fullName riêng; kiểm tra đổi từng input.

## Tự kiểm tra kết quả

- [ ] Không có cảnh báo thiếu dependency.
- [ ] Gõ nhanh không để lại timer cũ.
- [ ] fullName được suy ra trực tiếp từ state.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
