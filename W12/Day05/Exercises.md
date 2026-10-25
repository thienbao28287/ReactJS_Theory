# W12 · Day05 — Bài tập: Redux Saga: generator và quản lý side effects

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Làm quen call/put/takeLatest và phân biệt hủy task với hủy mạng.

## Bài 1 — Đọc generator (15 phút)

Trước khi chạy, mô tả yield call, put và takeLatest. Trong mini-shop npm install redux-saga@1; không gọi saga.run mỗi render.

## Bài 2 — Store lab (30 phút)

Tạo component lab bọc Provider bằng sagaStore, button dispatch requested() và UI đọc status/data. Không đặt thêm Provider vào app cart chính; lab dùng store riêng có chủ đích.

## Bài 3 — Hủy/lỗi (20 phút)

Bật mạng chậm và dispatch hai lần, quan sát task/request cũ được hủy qua finally. Thử URL lỗi, status=error; so số phần cần thiết với thunk W08.

## Tự kiểm tra kết quả

- [ ] Hiểu generator/effect descriptor, không gọi Saga như async thường.
- [ ] Saga middleware chạy một lần cho store lab.
- [ ] Phân biệt cancel task và abort request.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
