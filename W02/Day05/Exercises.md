# W02 · Day05 — Bài tập: Điều kiện, lists và key

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Hiển thị trạng thái rỗng và danh sách có key ổn định.

## Bài 1 — Ba trạng thái (15 phút)

Chạy danh sách có dữ liệu, còn một item, rồi rỗng. Ghi UI ở mỗi trạng thái; trang không xuất hiện số 0 lẻ.

## Bài 2 — Todo hiển thị (30 phút)

Tạo TodoItem nhận todo và onToggle/onDelete. Cha map danh sách, gán key=todo.id. Hiển thị nhãn hoàn thành và nút hành động có tên phân biệt từng Todo.

## Bài 3 — Lọc và đổi thứ tự (20 phút)

Thêm bộ lọc tất cả/hoàn thành/chưa hoàn thành với state filter. Tạo nút đảo thứ tự bằng bản sao array; trạng thái done vẫn thuộc đúng id.

## Tự kiểm tra kết quả

- [ ] Xóa hết hiện thông báo rỗng.
- [ ] Không có cảnh báo missing key.
- [ ] Lọc không xóa dữ liệu gốc; đảo thứ tự không đổi trạng thái item.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
