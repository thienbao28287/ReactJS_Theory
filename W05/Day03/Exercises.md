# W05 · Day03 — Bài tập: Dynamic routes và useParams

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tạo trang chi tiết sản phẩm từ tham số URL.

## Bài 1 — Đọc param (15 phút)

Chạy /products/1, /products/2, /products/99, /products/abc. Ghi useParams trả kiểu gì và cách tìm item.

## Bài 2 — Chi tiết thật trong dự án (30 phút)

ProductCard link tới /products/:id. DetailPage đọc id, dùng getProducts hiện có rồi tìm sản phẩm, có loading/error/not found và cleanup khi id đổi.

## Bài 3 — Đổi nhanh (20 phút)

Bật mạng chậm rồi chuyển hai id; chỉ hiện đúng id cuối. Nhập deep link trực tiếp không cần phải đi qua danh sách trước.

## Tự kiểm tra kết quả

- [ ] Chi tiết không phụ thuộc việc danh sách đã mở.
- [ ] Param không tồn tại hiển thị thông báo.
- [ ] Đổi id không hiển thị kết quả cũ.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
