# W11 · Day03 — Bài tập: Build, preview và deploy Vercel

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Đưa bản build lên host và kiểm tra deep link/biến môi trường.

## Bài 1 — Build local (15 phút)

Trong mini-shop chạy npm run build, npm run preview; mở URL preview thật và kiểm tra catalog/cart/account. Ghi lỗi khác dev nếu có.

## Bài 2 — Deploy (30 phút)

Tự import repository vào Vercel và chọn Root Directory W04/mini-shop. Chỉ publish dữ liệu học tập công khai; đặt env công khai phù hợp và deploy. Nếu không có tài khoản/quyền, lưu cấu hình cùng log preview và ghi chưa deploy.

## Bài 3 — Smoke test (20 phút)

Mở trực tiếp /products/1, refresh /cart, kiểm tra products.json và asset không nhận HTML. Nếu cần thêm vercel.json theo ví dụ rồi deploy lại. Ghi URL và trạng thái thật, không tự nhận đã deploy khi chỉ preview.

## Tự kiểm tra kết quả

- [ ] Build/preview thành công có bằng chứng.
- [ ] Root Directory và output đúng dự án con.
- [ ] Deep link và fixture/asset kiểm tra riêng.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
