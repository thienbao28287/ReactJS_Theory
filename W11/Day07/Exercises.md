# W11 · Day07 — Bài tập: CI/CD tổng quan và kiểm tra bản phát hành

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tự động kiểm tra unit/build trong repository chứa nhiều tuần.

## Bài 1 — Workflow (15 phút)

Đọc và tạo .github/workflows/mini-shop-ci.yml ở gốc repository khi app/lockfile/tests đã tồn tại. Không tạo ở dưới mini-shop/.github.

## Bài 2 — Chạy và đọc log (30 phút)

Nếu có remote GitHub, push branch rồi đọc Actions từng bước; nếu chưa, chạy cùng lệnh local và ghi chưa xác nhận trên runner Linux. Sửa chữ hoa/thường đường dẫn nếu chỉ lỗi trên Linux.

## Bài 3 — Release checklist (20 phút)

Kiểm tra env, route refresh, API state, cart, form, test/build và README. Tạo release-review.md có trạng thái từng mục, URL deploy thật hoặc ghi chưa triển khai.

## Tự kiểm tra kết quả

- [ ] Workflow chỉ đúng dự án con và lockfile.
- [ ] Test/build có log kết quả thật.
- [ ] Báo cáo tách local, CI và deploy.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
