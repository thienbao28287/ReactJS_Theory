# W09 · Day06 — Bài tập: Tối ưu catalog bằng một thay đổi đo được

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Thực hiện quy trình baseline–giả thuyết–thay đổi–đối chiếu.

## Bài 1 — Đo baseline (15 phút)

Record ba lần thao tác đã chọn, ghi dataset và môi trường. Dùng hàm ví dụ để tổng hợp nếu có số thời gian phù hợp.

## Bài 2 — Thay đổi (30 phút)

Áp dụng một cải tiến đã học: đưa state gần nơi dùng, memo child hoặc memo phép tính. Record cùng thao tác ba lần, so median và mức dao động.

## Bài 3 — Hồi quy (20 phút)

Kiểm tra query thay đổi, cart count/total và route. Viết đoạn kết luận có bằng chứng, không khẳng định nhanh hơn nếu số đo dao động chồng lấn lớn.

## Tự kiểm tra kết quả

- [ ] Có trước/sau cùng điều kiện.
- [ ] UI vẫn đúng với data mới.
- [ ] Chỉ giữ tối ưu có lý do rõ.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
