# W10 · Day01 — Bài tập: Testing pyramid và Jest cơ bản

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Phân biệt test cấp hàm, component và E2E; chạy bài Jest độc lập.

## Bài 1 — Chạy Jest (15 phút)

Tạo thư mục W10/jest-lab riêng, npm init -y, npm install -D jest. Tạo total.test.cjs theo ví dụ và jest.config.cjs chứa module.exports = { testEnvironment: "node", testMatch: ["**/*.test.cjs"] }; chạy npx jest từ lab.

## Bài 2 — Test có ích (30 phút)

Tách hàm total sang total.cjs rồi require từ test. Thêm ca một dòng quantity>1 và input hợp lệ có price=0. Sửa tạm hàm bỏ quantity, xác nhận test thất bại rồi khôi phục.

## Bài 3 — Kế hoạch (20 phút)

Lập bảng 8 hành vi mini-shop và chọn tầng test phù hợp: reducer, filter, form, API state, route và giỏ. Không dùng snapshot toàn trang thay kiểm tra hành vi.

## Tự kiểm tra kết quả

- [ ] Lab Jest chạy được độc lập.
- [ ] Test thất bại khi cố ý tạo lỗi rồi xanh sau sửa.
- [ ] Có kế hoạch test theo rủi ro/hành vi.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
