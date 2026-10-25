# W07 · Day06 — Bài tập: Persist giỏ hàng và derived data

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Khôi phục giỏ an toàn và tính count/total từ một nguồn dữ liệu.

## Bài 1 — Hydrate (15 phút)

Dùng readCart làm initializer của reducer: useReducer(cartReducer, undefined, readCart). Chỉ áp dụng trong app client đang học.

## Bài 2 — Persist (30 phút)

Effect ghi key mini-shop-cart-v1 với version=1 và items. Bắt lỗi storage; thêm UI báo không lưu được nhưng vẫn cho giỏ hoạt động trong bộ nhớ.

## Bài 3 — Dữ liệu hỏng (20 phút)

Thử JSON hỏng, quantity âm, price chuỗi và version khác. Giỏ khởi tạo an toàn, total hữu hạn; reload dữ liệu đúng phải giữ giỏ.

## Tự kiểm tra kết quả

- [ ] Reload giữ giỏ hợp lệ.
- [ ] Dữ liệu sai không làm NaN/crash.
- [ ] Count/total suy ra từ items, không có state trùng.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
