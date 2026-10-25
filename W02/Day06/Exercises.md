# W02 · Day06 — Bài tập: Controlled input và Todo CRUD

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Tạo Todo bằng form, quản lý input bằng State và cập nhật danh sách.

## Bài 1 — Form cơ bản (15 phút)

Thêm "Học JSX" bằng Enter và "Học State" bằng button. Input phải được xóa sau mỗi lần thêm. Chỉ nhập khoảng trắng không tạo item.

## Bài 2 — Hoàn thiện CRUD (30 phút)

Ghép TodoItem Day05 với form; thêm chức năng sửa tiêu đề bằng input chỉnh sửa và hai nút Lưu/Hủy. Lưu tiêu đề rỗng phải báo lỗi, Hủy giữ nội dung cũ.

## Bài 3 — Derived data (20 phút)

Hiển thị số Todo chưa hoàn thành và bộ lọc ba trạng thái. Thử thêm→sửa→toggle→xóa dưới các bộ lọc; số đếm phải dựa trên toàn bộ todos, không chỉ danh sách đang nhìn.

## Tự kiểm tra kết quả

- [ ] Input luôn có value chuỗi và onChange.
- [ ] Không tạo/lưu Todo chỉ có khoảng trắng.
- [ ] Hủy chỉnh sửa không đổi dữ liệu; số lượng còn lại chính xác.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
