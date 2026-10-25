# W12 · Day03 — Bài tập: React 19 Actions và optimistic UI

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Thử useActionState, useFormStatus và useOptimistic trong một form client.

## Bài 1 — Phiên bản và form (15 phút)

Kiểm tra React/React DOM cùng major 19, chạy demo. Quan sát button pending chỉ đọc đúng khi là con của form.

## Bài 2 — Thành công và rollback (30 phút)

Gửi một ghi chú bình thường: hiện tạm rồi xác nhận; gửi từ fail: dòng tạm phải biến mất và lỗi xuất hiện. Thử submit rỗng; không tạo ghi chú trống.

## Bài 3 — Giải thích (20 phút)

Vẽ state chuẩn và optimistic state theo thời gian. So với RHF: bài này học Actions, không bắt chuyển form production đang hoạt động sang API mới. Ghi giới hạn Promise local.

## Tự kiểm tra kết quả

- [ ] Pending và optimistic hoạt động trong Action.
- [ ] Thất bại không giữ bản ghi chưa xác nhận.
- [ ] useFormStatus nằm trong component con form.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
