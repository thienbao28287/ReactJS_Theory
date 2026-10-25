# W08 · Day05 — Bài tập: createAsyncThunk và request lifecycle

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Quản lý pending/fulfilled/rejected và tránh response cũ ghi đè.

## Bài 1 — Lifecycle (15 phút)

Thêm reducer products vào store; dispatch loadProducts, quan sát pending/fulfilled trong DevTools.

## Bài 2 — Trang dùng thunk (30 phút)

ProductsPage select data/status/error, effect dispatch thunk và cleanup abort promise. Thêm retry; bỏ request effect cũ để không tải trùng từ hai cơ chế.

## Bài 3 — Lỗi/race (20 phút)

Thử fixture lỗi, unmount và hai lần retry nhanh. aborted không hiện lỗi; chỉ request hiện hành được cập nhật data/status.

## Tự kiểm tra kết quả

- [ ] Có idle/loading/succeeded/failed rõ.
- [ ] Cleanup abort và rejected xử lý đúng.
- [ ] Không đồng thời dùng thunk và service effect cũ cho cùng nguồn UI.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
