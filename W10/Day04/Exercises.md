# W10 · Day04 — Bài tập: userEvent và giỏ hàng tích hợp

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Kiểm tra tương tác qua UI với store độc lập mỗi test.

## Bài 1 — userEvent (15 phút)

Chạy ví dụ, giải thích vì sao await click. Không dùng delay cố định để chờ state.

## Bài 2 — Cart UI thật (30 phút)

Tạo store mới từ cart reducer trong từng test; render vùng giỏ và nút thêm. Thực hiện Book×2/Pen×1, kiểm tra tổng 170 bằng nhãn/text thực tế.

## Bài 3 — Quantity và xóa (20 phút)

Test đổi quantity thành 3 rồi xóa item cuối; tổng/badge/empty state cập nhật. Test input sai theo hành vi app, không ép giá trị không được phép.

## Tự kiểm tra kết quả

- [ ] Hành động được await.
- [ ] Mỗi test có store mới.
- [ ] Kiểm tra cả tổng tiền và empty state sau thao tác.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
