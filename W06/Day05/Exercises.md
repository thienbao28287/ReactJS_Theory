# W06 · Day05 — Bài tập: Zod: schema và validation

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Mô tả quy tắc dữ liệu bằng schema và đọc lỗi có cấu trúc.

## Bài 1 — Schema cơ bản (15 phút)

Chạy module trong dự án Vite; thử email sai, password ngắn, confirm khác. Đọc issues/path/message, không log giá trị mật khẩu.

## Bài 2 — Schema checkout (30 phút)

Tạo schema tên nhận hàng bắt buộc sau trim, email, địa chỉ tối thiểu 10 ký tự và quantity là số nguyên 1–99. Chỉ dùng dữ liệu giả, không địa chỉ riêng thật.

## Bài 3 — Ca biên (20 phút)

Kiểm tra quantity="", "2", 0, 1, 99, 100 và 1.5. Ghi rõ contract nhận số hay chuỗi và nơi chuyển kiểu; không cho giá trị rỗng âm thầm thành số hợp lệ.

## Tự kiểm tra kết quả

- [ ] safeParse được kiểm tra success trước data.
- [ ] Confirm lỗi nằm đúng field.
- [ ] Quantity rỗng/ngoài giới hạn/thập phân bị xử lý rõ.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
