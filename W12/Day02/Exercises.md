# W12 · Day02 — Bài tập: Hooks React 18: useId, transition và deferred value

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Phân biệt tính duy nhất id, cập nhật ưu tiên thấp và giá trị trì hoãn.

## Bài 1 — ID (15 phút)

Render hai instance input có useId, xác nhận id khác và label focus đúng. Giải thích vì sao không dùng id này làm key sản phẩm.

## Bài 2 — Deferred và transition (30 phút)

Chạy demo với CPU throttling nếu cần; giữ input phản hồi nhanh. Làm bản lab khác dùng useTransition cho state kết quả, input vẫn state đồng bộ. So sánh cơ chế, không áp cả hai vô cớ.

## Bài 3 — Giới hạn (20 phút)

Quan sát Network để chứng minh deferred không tự debounce fetch. Viết bảng mục đích useSyncExternalStore/useInsertionEffect; không tự triển khai store/CSS engine trong buổi này.

## Tự kiểm tra kết quả

- [ ] Input controlled không bị đưa vào transition.
- [ ] Key danh sách từ row.id.
- [ ] Phân biệt deferred, transition và debounce.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
