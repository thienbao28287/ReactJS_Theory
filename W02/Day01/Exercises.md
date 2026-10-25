# W02 · Day01 — Bài tập: Props và children

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tạo component nhận dữ liệu từ cha và tái sử dụng với nội dung khác nhau.

## Bài 1 — Dự đoán Props (15 phút)

Chạy ví dụ; thử bỏ name, truyền name="" rồi name={null}. Ghi ba kết quả và giải thích khi nào giá trị mặc định được dùng.

## Bài 2 — Tái sử dụng hồ sơ (30 phút)

Nâng Profile của W01 để nhận name, city, goal. App hiển thị hai học viên khác nhau; tạo Section nhận title và children để bọc nội dung. Không sửa object đầu vào trong component.

## Bài 3 — Kiểm tra ranh giới (20 phút)

Đổi dữ liệu người thứ nhất, xác nhận người thứ hai không đổi. Viết vì sao children khác với một chuỗi truyền qua title; thử một Section có hai phần tử con.

## Tự kiểm tra kết quả

- [ ] Hai Profile có nội dung khác nhau từ cùng một component.
- [ ] Section render được nhiều phần tử con.
- [ ] Không có thao tác gán lại Props hoặc cảnh báo Console.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
