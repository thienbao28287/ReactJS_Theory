# W04 · Day03 — Bài tập: Custom Hook useFetch có cleanup

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tách trạng thái tải dữ liệu thành Hook có URL đầu vào.

## Bài 1 — Dùng Hook (15 phút)

Import useFetch vào ProductList, gọi với /products.json. Component xử lý cả data=null trước khi map.

## Bài 2 — Hai nơi sử dụng (30 phút)

Dùng Hook trong một trang danh sách và một bảng thống kê nhỏ. Giữ UI khác nhau nhưng logic request chung; quan sát có thể có hai request vì Hook không có cache.

## Bài 3 — Ca URL đổi (20 phút)

Tạo hai fixture khác nhau và nút đổi URL nhanh; kiểm tra kết quả cuối đúng URL cuối, URL rỗng không request và unmount không hiện lỗi hủy.

## Tự kiểm tra kết quả

- [ ] Hook có data/loading/error và cleanup.
- [ ] Component không map null.
- [ ] URL rỗng và đổi URL nhanh có kết quả đúng.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
