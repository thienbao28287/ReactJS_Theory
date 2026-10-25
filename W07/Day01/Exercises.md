# W07 · Day01 — Bài tập: State cục bộ, nâng State và prop drilling

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Chọn nơi sở hữu dữ liệu trước khi đưa vào global state.

## Bài 1 — Nâng State (15 phút)

Chạy demo, vẽ component nào sở hữu count, ai đọc và ai yêu cầu cập nhật.

## Bài 2 — Bản đồ dữ liệu (30 phút)

Liệt kê query, cart, draft form, auth và product data trong mini-shop. Với mỗi dữ liệu ghi phạm vi dùng, nguồn thật, nơi lưu hiện tại và đề xuất local/global/server state.

## Bài 3 — Composition (20 phút)

Tạo hai lớp trung gian rồi thử truyền JSX children chứa CartBadge thay vì mọi lớp nhận count. Ghi khi nào cách này đủ và khi nào Context rõ hơn.

## Tự kiểm tra kết quả

- [ ] Có bảng phân loại ít nhất năm loại dữ liệu.
- [ ] Hai component dùng cùng count nhất quán.
- [ ] Không tạo state trùng để đồng bộ bằng effect.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
