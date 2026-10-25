# W03 · Day04 — Bài tập: fetch và HTTP cơ bản

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tải JSON, kiểm tra HTTP status và hiển thị dữ liệu trong React.

## Bài 1 — Đọc response (15 phút)

Mở Network, xem status và body của /products.json. Phân biệt lỗi mạng với HTTP lỗi; thử đường dẫn không tồn tại và quan sát content-type/body.

## Bài 2 — Danh sách sản phẩm (30 phút)

Tạo component ProductList tải fixture; bổ sung loading và kết thúc loading trong finally khi request còn hiệu lực. Hiển thị title và price.

## Bài 3 — Ca dữ liệu sai (20 phút)

Thử fixture {}, JSON lỗi cú pháp rồi array hợp lệ; ứng dụng báo lỗi thay vì crash khi map. Khôi phục fixture cuối buổi.

## Tự kiểm tra kết quả

- [ ] Hiển thị hai sản phẩm từ fixture.
- [ ] HTTP lỗi và JSON không hợp lệ được bắt.
- [ ] Unmount không cập nhật từ request đã bị bỏ qua.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
