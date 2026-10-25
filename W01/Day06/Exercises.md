# W01 · Day06 — Mini project: Hồ sơ học tập

Thời lượng thực hành 75 phút. Dùng tiếp `W01/react-profile`; đọc [Theory](./Theory.md). Mục tiêu là trang tĩnh hoàn chỉnh, chưa yêu cầu tương tác hay API.

## Đề bài

Xây trang giới thiệu bạn với vai trò người học Frontend. Nội dung tối thiểu:

| Vùng | Yêu cầu |
| --- | --- |
| Header | Tên trang, một h1 và câu mô tả ngắn |
| Profile | Tên, thành phố, giới thiệu bản thân bằng dữ liệu JavaScript |
| Skills | Danh sách ít nhất ba kỹ năng, viết bằng `ul/li` |
| LearningGoals | Ba mục tiêu cụ thể; hiển thị `2 × 7 = 14 giờ/tuần` từ biến |
| Footer | Link tài liệu React và lời nhắc học |

Giữ một component StudyReminder dùng ở hai vị trí từ Day05. Không cần thông tin riêng tư như địa chỉ nhà hay số điện thoại.

## Bước 1 — Nội dung và cấu trúc (20 phút)

- Hoàn thiện đủ các component và thông tin cá nhân.
- App ghép Header, một main chứa nội dung và Footer.
- Dùng h2 cho các phần, không chọn heading chỉ để lấy cỡ chữ.
- Dùng biểu thức cho tên, thành phố và số giờ; không viết cứng kết quả `14`.

## Bước 2 — Bố cục và CSS (25 phút)

- Bổ sung container, khoảng cách, màu nền và panel.
- Một cột ở 375px; có thể hai cột khi từ 720px.
- Cỡ chữ nội dung dễ đọc, màu chữ tương phản với nền.
- Không dùng chiều rộng cố định khiến trang tràn ngang.

Có thể bắt đầu bằng CSS trong Theory, nhưng phải giải thích được `.container`, `.content-grid`, `.panel` đang gắn ở đâu và làm gì.

## Bước 3 — Kiểm tra người dùng (15 phút)

1. Mở trang ở chiều rộng 375px, 768px, 1280px bằng DevTools.
2. Kiểm tra không có thanh cuộn ngang và nội dung không bị che.
3. Bấm link tài liệu; kiểm tra đúng địa chỉ.
4. Dùng Tab để đến link; thấy rõ focus.
5. Kiểm tra Console và Network, sửa lỗi tài nguyên hỏng nếu có.

## Bước 4 — Kiểm tra khả năng bảo trì (15 phút)

Đổi số giờ học mỗi ngày từ 2 sang 3: tổng phải thành 21 mà không sửa phép hiển thị. Đổi câu nhắc trong StudyReminder: hai vị trí phải cùng đổi. Khôi phục 2 tiếng/ngày sau khi thử.

Lưu `W01/Day06/notes.md`: ba quyết định bạn đã đưa ra, một lỗi và cách sửa. Có thể lưu ảnh màn hình trong Day06 để so sánh tiến bộ.

## Thang tự chấm: 10 điểm

- 3 điểm: đủ nội dung và năm component chính.
- 2 điểm: JSX, dữ liệu và import/export đúng.
- 2 điểm: bố cục không tràn ở ba kích thước kiểm tra.
- 2 điểm: semantic HTML, link/focus hợp lệ, không lỗi Console.
- 1 điểm: giải thích được cây component và cách tính tổng giờ.

Đạt từ 8 điểm và không có lỗi làm trang không chạy là đủ để chuyển sang Day07. Nếu còn thời gian, chỉnh khoảng cách/typography; không thêm thư viện mới để lấy điểm.
