# W04 · Day05 — Bài tập: Interceptors, Swagger và Postman

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Đọc hợp đồng API và quản lý interceptor có vòng đời rõ.

## Bài 1 — Đọc endpoint (15 phút)

Chọn một endpoint công khai có tài liệu; ghi method, params bắt buộc, success schema và hai lỗi có thể có. Nếu chưa có Swagger riêng, dùng tài liệu REST API công khai.

## Bài 2 — Postman và browser (30 phút)

Tạo collection và biến baseUrl trong Postman, gửi request rồi so sánh Network trình duyệt. Ghi rõ CORS là kiểm soát của trình duyệt, không đề xuất tắt bảo vệ browser.

## Bài 3 — Interceptor (20 phút)

Thêm interceptor cùng origin, kiểm tra header trong Network. Thử đăng ký/gỡ một interceptor log có id và xác nhận không log trùng sau nhiều lần mount.

## Tự kiểm tra kết quả

- [ ] Có ghi chép contract, không đoán cấu trúc response.
- [ ] Interceptor return đúng và có cách eject.
- [ ] Phân biệt lỗi API với CORS/browser.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
