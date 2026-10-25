# W05 · Day07 — Bài tập: Tổng kết navigation của mini-shop

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Hoàn thiện sơ đồ URL, deep link, bộ lọc và luồng login mô phỏng.

## Bài 1 — Hoàn thiện (30 phút)

Ghép RootLayout, danh sách, chi tiết, cart, account, login và 404. Tạo bảng URL trong README của mini-shop, nêu path/query và trạng thái mô phỏng.

## Bài 2 — Ma trận route (20 phút)

Chạy tám ca: deep link hợp lệ, id sai, query có ký tự đặc biệt, Back/Forward, refresh, guard, logout và 404. Ghi kết quả thực tế.

## Bài 3 — Review (15 phút)

Giải thích một Router gốc, Outlet, param string và query. Thử getLoginDestination với /products/1, //example.com, https://example.com; không điều hướng ra ngoài.

## Tự kiểm tra kết quả

- [ ] Có bảng route và tám ca kiểm tra.
- [ ] Không có Router lồng nhau hoặc Header trùng.
- [ ] Login chỉ nhận đích nội bộ; guard vẫn chỉ là mô phỏng.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
