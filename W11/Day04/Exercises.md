# W11 · Day04 — Bài tập: Gitflow thực hành và Pull Request

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Thực hiện một task trên branch riêng, commit có nghĩa và review thay đổi.

## Bài 1 — Chuẩn bị branch (15 phút)

Từ gốc ReactJS, kiểm tra và lưu công việc hiện tại trước khi tạo branch. Nếu branch đã có, dùng tên task khác; không xóa branch chứa bài học.

## Bài 2 — Task nhỏ (30 phút)

Cải thiện empty state giỏ hoặc label lỗi form, bổ sung/chỉnh test liên quan. Stage đúng file đã sửa, đọc diff rồi commit; thư mục trong ví dụ cần đổi cho khớp nơi file thực tế.

## Bài 3 — PR review (20 phút)

Nếu có remote/quyền, push feature và tạo PR để tự review; nếu chưa có, viết PR-description.md và đọc diff local. Ghi validation thật, không khẳng định PR tồn tại nếu chưa tạo.

## Tự kiểm tra kết quả

- [ ] Task nằm trên feature branch riêng.
- [ ] Staged diff chỉ gồm file đúng task.
- [ ] Mô tả PR có hành vi và kiểm tra cụ thể.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
