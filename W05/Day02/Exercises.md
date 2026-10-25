# W05 · Day02 — Bài tập: Link, NavLink và useNavigate

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Điều hướng khai báo và điều hướng sau hành động.

## Bài 1 — Active link (15 phút)

Chạy demo, inspect aria-current của NavLink active. Thêm CSS cho class active và trạng thái focus.

## Bài 2 — Điều hướng theo hành động (30 phút)

Tạo trang đăng nhập mô phỏng: submit hợp lệ đợi Promise nhỏ rồi navigate tới /products. Chỉ chuyển khi thành công; lỗi mô phỏng giữ nguyên trang.

## Bài 3 — History (20 phút)

So sánh navigate thường với replace sau login. Ghi Back sẽ đến trang nào; giữ link tường minh về sản phẩm thay vì chỉ nút quay lại không rõ đích.

## Tự kiểm tra kết quả

- [ ] Link active đúng ở / và /products.
- [ ] Submit thất bại không điều hướng.
- [ ] Giải thích được replace với push history.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
