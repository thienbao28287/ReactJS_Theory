# W09 · Day07 — Bài tập: Tổng kết performance và rà soát effects

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Giữ code dễ hiểu, loại bỏ cache/effect dư thừa và ghi quyết định.

## Bài 1 — Audit (30 phút)

Đọc toàn bộ effect và memo trong mini-shop. Lập bảng file, mục đích, dependency, cleanup và quyết định giữ/bỏ; không bỏ cơ chế request chỉ vì có nhiều render.

## Bài 2 — Kiểm tra (20 phút)

Chạy lại API, filter, cart, form và routing sau khi dọn. Không còn cảnh báo dependency; abort/unmount vẫn đúng.

## Bài 3 — Báo cáo (15 phút)

Viết performance-review.md có số đo và kết luận. Nếu app nhỏ chưa có bottleneck, ghi rõ kết quả đó và giữ lab minh họa riêng.

## Tự kiểm tra kết quả

- [ ] Mỗi memo/effect có lý do mô tả được.
- [ ] Không mất cleanup sau refactor.
- [ ] Báo cáo phân biệt đo được với suy đoán.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
