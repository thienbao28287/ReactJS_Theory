# W07 · Day04 — Bài tập: useReducer: action và reducer thuần

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tách quy tắc cập nhật state khỏi JSX bằng reducer.

## Bài 1 — Luồng action (15 phút)

Dự đoán chuỗi increment, increment, decrement, reset từ 0. Chạy demo đối chiếu rồi vẽ dispatch→reducer→state→UI.

## Bài 2 — Reducer Todo (30 phút)

Tạo reducer có add/toggle/remove, id tạo ở handler. Chạy reducer bằng dữ liệu JS ngoài UI; input cũ không đổi sau mỗi action.

## Bài 3 — Action lạ (20 phút)

Kiểm tra action không biết, xóa id không tồn tại và decrement ở 0. Chọn return state hoặc throw có chủ đích cho action lạ, ghi chính sách.

## Tự kiểm tra kết quả

- [ ] Reducer trả state mới cho cập nhật thật.
- [ ] Không side effect hoặc sinh id trong reducer.
- [ ] Ca biên giữ state hợp lệ.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
