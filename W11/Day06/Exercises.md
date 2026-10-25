# W11 · Day06 — Bài tập: Docker nhiều giai đoạn và Nginx

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Hiểu build image và phục vụ SPA static trong container.

## Bài 1 — Đọc Dockerfile (15 phút)

Giải thích từng dòng, phân biệt build/runtime. Tạo Dockerfile ở W04/mini-shop và .dockerignore loại node_modules, dist, .git, .env.local, .env.*.local; giữ .env.example nếu cần tài liệu.

## Bài 2 — Nginx và chạy (30 phút)

Tạo nginx.conf: server { listen 80; root /usr/share/nginx/html; index index.html; location / { try_files $uri $uri/ /index.html; } }. Trong mini-shop: docker build -t mini-shop:learning . rồi docker run --rm -p 8080:80 mini-shop:learning. Cần Docker Desktop đã hoạt động.

## Bài 3 — Kiểm tra (20 phút)

Mở localhost:8080/products/1, refresh và kiểm tra products.json. Dừng container bằng Ctrl+C. Nếu môi trường chưa hỗ trợ Docker, ghi rõ phần nào chỉ đọc và chưa xác nhận chạy; không coi đó là hoàn thành vận hành.

## Tự kiểm tra kết quả

- [ ] Giải thích được hai stage và image/container.
- [ ] Có Dockerfile, nginx.conf, .dockerignore đúng context.
- [ ] Ghi thật kết quả build/run và deep link.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
