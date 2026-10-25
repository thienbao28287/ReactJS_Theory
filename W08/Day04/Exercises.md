# W08 · Day04 — Bài tập: State structure, selectors và DevTools

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tổ chức slice theo tính năng, tính dữ liệu suy ra và đọc lịch sử action.

## Bài 1 — Selectors (15 phút)

Đặt selectors vào module riêng; thử state rỗng và cart Book×2/Pen×1, kết quả count=3 và total=170.

## Bài 2 — Persist Redux (30 phút)

Dùng cart validator W07, khởi tạo store bằng preloadedState đúng shape {cart:{items}}. Subscribe lưu chỉ items, có try/catch. Không giữ persistence effect Context cũ.

## Bài 3 — Debug (20 phút)

Gây lỗi thao tác giả rồi tìm action gây sai bằng Redux DevTools. Ghi action type/payload và state trước/sau; kiểm tra reload giỏ vẫn đúng.

## Tự kiểm tra kết quả

- [ ] Count/total không lưu trùng trong state.
- [ ] PreloadedState đúng shape và đã validate.
- [ ] DevTools giải thích được một thay đổi state.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
