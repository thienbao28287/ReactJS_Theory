# W02 · Day02 — Bài tập: Sự kiện và callback Props

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Xử lý click và cho component con thông báo hành động lên cha.

## Bài 1 — Quan sát thời điểm (15 phút)

Chạy ví dụ; tải lại trang phải chưa có log đã chọn, click một lần tạo một thông báo. Ghi khác biệt giữa truyền handler và gọi handler ngay.

## Bài 2 — Thanh công cụ (30 phút)

Tạo Toolbar chứa hai ActionButton dùng callback Props. Nút Xem hồ sơ và Xem kỹ năng báo tên hành động về cha qua console.log. Mọi nút có type rõ ràng.

## Bài 3 — Event mặc định (20 phút)

Tạo form tìm kiếm đơn giản với input không kiểm soát. onSubmit gọi preventDefault và log FormData; Enter và click submit đều xử lý một lần, không reload trang. State học ngày mai.

## Tự kiểm tra kết quả

- [ ] Handler không chạy khi vừa render.
- [ ] Cha nhận đúng hành động hoặc id từ từng nút.
- [ ] Form submit bằng Enter không tải lại document.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
