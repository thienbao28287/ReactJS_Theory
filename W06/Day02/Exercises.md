# W06 · Day02 — Bài tập: Tailwind CSS v4 và responsive

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Cài Tailwind theo Vite plugin hiện hành và chỉnh bố cục mini-shop.

## Bài 1 — Cài và kiểm tra (15 phút)

Thêm plugin theo ví dụ; thêm @import "tailwindcss"; ở đầu CSS được main.jsx import. Tạo heading có class text-2xl font-bold; xác nhận style thực sự áp dụng.

## Bài 2 — Responsive catalog (30 phút)

Dùng grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 cho danh sách. Card có tên, giá, link chi tiết; kiểm tra 375/768/1280px, không tràn ngang.

## Bài 3 — SASS và lựa chọn (20 phút)

Đọc vai trò nesting/variables của SASS từ GitHub Lesson-03; ghi so sánh với utility. Không cần thêm pipeline SASS trong dự án này; hoàn thiện focus-visible và tương phản.

## Tự kiểm tra kết quả

- [ ] Build/dev nhận utility v4.
- [ ] Catalog không tràn ở ba kích thước.
- [ ] Link/button có focus rõ và class đầy đủ.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
