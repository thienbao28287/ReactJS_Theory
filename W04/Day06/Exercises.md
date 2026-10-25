# W04 · Day06 — Bài tập: Service layer và khung mini-shop

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tách giao tiếp dữ liệu khỏi UI để thay API mà không sửa toàn bộ component.

## Bài 1 — Model (15 phút)

Viết model bằng bảng: id là number|string, title là string, price là number không âm. Cập nhật service kiểm tra thêm giá không âm.

## Bài 2 — Ghép trang (30 phút)

Tạo ProductsPage gọi service trong effect có cleanup; hiển thị ProductCard bằng Props. Có loading, error, empty và nút retry; không đặt axios trực tiếp trong ProductCard.

## Bài 3 — Đổi nguồn dữ liệu (20 phút)

Tạo fixture thứ hai cùng schema rồi đổi service một chỗ. Cả trang vẫn render đúng mà không sửa ProductCard; thử response thiếu price và xem lỗi rõ ràng.

## Tự kiểm tra kết quả

- [ ] UI không phụ thuộc cấu trúc Response của Axios.
- [ ] Đổi endpoint một chỗ vẫn render đúng.
- [ ] Dữ liệu sai không thành giá NaN trên giao diện.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
