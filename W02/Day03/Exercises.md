# W02 · Day03 — Bài tập: useState và cập nhật theo state trước

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Xây Counter hiểu đúng snapshot state và functional updater.

## Bài 1 — So sánh updater (15 phút)

Chạy +3, sau đó thử ba lần setCount(count + 1). Ghi kết quả của hai cách trong cùng handler rồi khôi phục functional updater.

## Bài 2 — Counter hoàn chỉnh (30 phút)

Làm tăng 1, giảm 1, reset. Không cho số âm. Theo bài PDF, khi count=0 thì disable cả giảm và reset. Thêm nút +3 bằng updater.

## Bài 3 — Giải thích snapshot (20 phút)

Click liên tục và kiểm tra 0→1→4→3→0. Thêm log trước/sau setter để quan sát snapshot; xóa log tạm sau khi hiểu. Viết vì sao await setCount không lấy được state mới.

## Tự kiểm tra kết quả

- [ ] Counter không xuống dưới 0.
- [ ] +3 tăng chính xác ba đơn vị.
- [ ] Giảm/reset bị disable ở 0, giải thích được snapshot.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
