# W06 · Day01 — Bài tập: Form có kiểm soát và UX nhập liệu

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Hiểu submit, validation và phản hồi trước khi dùng thư viện form.

## Bài 1 — Nhãn và lỗi (15 phút)

Chạy demo với rỗng, khoảng trắng và tên hợp lệ. Bấm label focus input; lỗi phải đọc được bằng nội dung và gắn đúng trường.

## Bài 2 — Form đăng ký cơ bản (30 phút)

Tạo email, password và confirm bằng State; kiểm tra bắt buộc, password tối thiểu 8 ký tự và confirm khớp. Không log hay lưu mật khẩu vào notes/storage.

## Bài 3 — Submit mô phỏng (20 phút)

Thêm Promise chờ 500ms và nút mô phỏng lỗi. Disable khi đang gửi; lỗi giữ nguyên input, thành công hiển thị thông báo rõ. Đây chưa phải đăng ký thật.

## Tự kiểm tra kết quả

- [ ] Enter và click xử lý cùng một luồng.
- [ ] Lỗi gắn đúng trường, không chỉ đổi màu.
- [ ] Lỗi gửi giữ dữ liệu; không log mật khẩu.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
