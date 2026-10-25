# W09 · Day05 — Bài tập: useCallback và callback Props

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Ổn định tham chiếu hàm khi child memo cần, không tạo stale closure.

## Bài 1 — Callback (15 phút)

Gõ input, quan sát child với/không useCallback. Click Thêm vẫn tăng đúng dù gõ nhiều lần.

## Bài 2 — Callback có id (30 phút)

Trong lab ProductCard memo nhận onAdd(productId). Thiết kế callback cha ổn định, mọi id đi qua tham số; không quên data dependency nếu callback đọc data.

## Bài 3 — Stale closure (20 phút)

Tạo ví dụ callback đọc query rồi cố ý thiếu query dependency để quan sát cũ; sửa lại. Giải thích vì sao tăng count có thể dùng updater còn đọc query thì không bỏ được query.

## Tự kiểm tra kết quả

- [ ] Click tăng đúng, callback không giữ dữ liệu cũ.
- [ ] Memo child nhận đầy đủ Props ổn định cần thiết.
- [ ] Không xóa dependency để giảm render giả tạo.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
