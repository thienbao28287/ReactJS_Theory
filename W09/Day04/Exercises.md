# W09 · Day04 — Bài tập: useMemo cho tính toán suy ra

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Memo hóa giá trị tính toán khi đã có lý do đo được.

## Bài 1 — Dependency (15 phút)

Chạy demo; khi đổi dark filter không cần tính lại, đổi query phải tính lại. Nếu products chuyển thành Props, thêm nó vào dependencies.

## Bài 2 — Áp dụng có đo (30 phút)

Đưa phép lọc/tính toán đã chọn ở Day02 vào useMemo. Record trước/sau với cùng data và thao tác; ghi nếu lợi ích không rõ.

## Bài 3 — Kiểm tra đúng (20 phút)

Thử query rỗng, không khớp và đổi data. Kết quả phải giống phiên bản không memo; ghi nơi quyết định không dùng memo vì phép tính quá nhỏ.

## Tự kiểm tra kết quả

- [ ] Đủ dependencies khi đầu vào đổi.
- [ ] Không có side effect trong callback useMemo.
- [ ] Có đối chiếu kết quả trước/sau.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
