# W02 · Day04 — Bài tập: State object và array bất biến

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Cập nhật hồ sơ và danh sách mà giữ nguyên phiên bản dữ liệu trước.

## Bài 1 — Cập nhật lồng nhau (15 phút)

Chạy ví dụ; sau khi đổi thành phố tên vẫn còn. Thêm district vào dữ liệu, đổi city nhưng giữ district.

## Bài 2 — Danh sách có id (30 phút)

Dùng state tasks gồm id, title, done. Tạo ba handler: thêm item với id ổn định, xóa theo id, đảo done bằng map. Có thể dùng nút và dữ liệu cố định; input sẽ học Day06.

## Bài 3 — Kiểm tra mutation (20 phút)

Giữ một bản dữ liệu cũ để so sánh ngoài React trong file .mjs. Chạy hàm đổi item; xác nhận bản cũ không bị sửa và item khác vẫn giữ nội dung. Thử xóa id không tồn tại.

## Tự kiểm tra kết quả

- [ ] Đổi thuộc tính lồng nhau không làm mất trường khác.
- [ ] Xóa/sửa đúng id, không sửa nhầm hàng.
- [ ] Không dùng push/splice trực tiếp lên state.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
