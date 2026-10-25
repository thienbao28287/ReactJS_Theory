# W04 · Day02 — Bài tập: Custom Hook useToggle

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Đóng gói logic dùng lại mà mỗi lần gọi vẫn có State riêng.

## Bài 1 — Hai instance (15 phút)

Chạy ví dụ; mở Chi tiết không được tự mở Trợ giúp. Ghi điều này chứng minh điều gì về custom Hook.

## Bài 2 — Tách module (30 phút)

Tạo src/hooks/useToggle.js có named export; dùng cho hai khu vực độc lập trong mini-shop. Thêm open để mở rõ ràng, close để đóng rõ ràng.

## Bài 3 — API rõ nghĩa (20 phút)

Kiểm tra close hai lần vẫn đóng, open hai lần vẫn mở, toggle đảo một lần. Viết hàm formatPrice thuần riêng và giải thích vì sao không đặt tên useFormatPrice.

## Tự kiểm tra kết quả

- [ ] Hai instance hoạt động độc lập.
- [ ] open/close có hành vi xác định.
- [ ] Hook được import và gọi ở top level.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
