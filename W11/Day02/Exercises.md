# W11 · Day02 — Bài tập: Biến môi trường Vite và cấu hình API

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tách API base URL và hiểu dữ liệu nào xuất hiện trong bundle client.

## Bài 1 — Env (15 phút)

Tạo .env.example với VITE_API_BASE_URL=/ và .env.local cùng giá trị cho fixture. Kiểm tra .gitignore loại .env.local; không chép secrets thật vào bài.

## Bài 2 — API config (30 phút)

Thay baseURL hard-code ở instance đang dùng, không tạo client thứ hai không dùng. Restart dev server, xác nhận /products.json vẫn tải được; thử base URL hợp lệ khác có chủ đích.

## Bài 3 — Build-time (20 phút)

Build rồi quan sát giá trị công khai có thể xuất hiện trong output; không tìm/in secret. Ghi vì sao không thể cất API private key trong VITE_ và vì sao static deploy cần rebuild khi đổi cấu hình.

## Tự kiểm tra kết quả

- [ ] Service dùng một điểm config.
- [ ] .env.example đủ để người khác chạy fixture.
- [ ] Không có biến bí mật trong bundle hoặc commit.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
