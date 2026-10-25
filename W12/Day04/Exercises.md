# W12 · Day04 — Bài tập: Zustand: store nhỏ và selectors

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Thử state manager khác trong lab và so sánh với Redux/Context.

## Bài 1 — Lab (15 phút)

Trong mini-shop npm install zustand@5, chạy demo riêng. Xác nhận Badge và nút đọc cùng store, không cần Provider cho mẫu này.

## Bài 2 — Todo store (30 phút)

Tạo Todo lab có add/toggle/remove và selector count; giữ state bất biến. Chưa cần thêm persist middleware nếu chưa hoàn thiện luồng cơ bản.

## Bài 3 — So sánh (20 phút)

Viết bảng Context+reducer/RTK/Zustand: phạm vi state, cập nhật, debug, kiến trúc. Nêu lựa chọn cho mini-shop và lý do; không thay Redux của dự án chính trong buổi này.

## Tự kiểm tra kết quả

- [ ] Selector primitive không tạo object mới vô cớ.
- [ ] Todo store bất biến và cập nhật đồng bộ.
- [ ] Quyết định công cụ có lý do từ yêu cầu.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
