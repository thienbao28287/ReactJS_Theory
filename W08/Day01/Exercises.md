# W08 · Day01 — Bài tập: Redux Core và luồng một chiều

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Nắm Store–Action–Reducer và phân biệt Redux với React Redux.

## Bài 1 — Luồng đồng bộ (15 phút)

Chạy module trong app Vite một lần, quan sát count=1. Vẽ thứ tự dispatch→reducer→store→subscriber.

## Bài 2 — So sánh Context (30 phút)

Viết bảng useReducer local, Context+reducer, Redux Toolkit theo phạm vi dữ liệu, cách đọc/cập nhật và công cụ debug. Dùng giỏ W07 làm ví dụ.

## Bài 3 — Đọc action (20 phút)

Dispatch action không biết, increment hai lần; kiểm tra state không reset. Dọn subscription sau thử nghiệm và không tạo store trong render.

## Tự kiểm tra kết quả

- [ ] Giải thích được ba phần và hai package.
- [ ] Store không bị tạo lại theo render.
- [ ] Subscription có cleanup.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
