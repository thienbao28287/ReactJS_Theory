# W01 · Day05 — Bài tập Component

Thực hành 65 phút trong dự án đang dùng, dựa trên [Theory](./Theory.md). Lưu phần trả lời vào `W01/Day05/notes.md`.

## Bài 1 — Vẽ cây trước khi code (10 phút)

Vẽ cây gồm App, Header, Profile, Skills, LearningGoals, Footer. Ghi một câu trách nhiệm cho từng component. Chỉ có một `main` cho nội dung chính; Header và Footer nằm ngoài main.

## Bài 2 — Tách file và ghép lại (30 phút)

Tạo năm file trong `src/components`:

- `Header.jsx`: tên trang và một câu giới thiệu.
- `Profile.jsx`: tên, thành phố và mô tả bản thân.
- `Skills.jsx`: danh sách HTML, CSS, JavaScript bằng ba thẻ `li` viết trực tiếp.
- `LearningGoals.jsx`: ít nhất hai mục tiêu có thể kiểm chứng.
- `Footer.jsx`: lời nhắc lịch học 2 tiếng/ngày.

Dùng default export cho bốn file đầu; named export cho Footer để luyện hai kiểu. App chỉ import và ghép các phần. Thông tin cá nhân phải là của bạn; chưa cần Props, State, `map()` hay event handler.

Kết quả: một trang có đủ năm vùng nội dung, tên component và import nhất quán. Sửa dòng mô tả trong Profile phải thấy đúng vùng giao diện đổi.

## Bài 3 — Tái sử dụng (10 phút)

Tạo component `StudyReminder` trả về một dòng nhắc học. Hiển thị nó ở hai vị trí: cuối Profile và trong Footer. Thay nội dung component một lần, xác nhận cả hai vị trí cập nhật.

Đây là tái sử dụng cấu trúc/nội dung tĩnh. Chưa yêu cầu mỗi vị trí có lời nhắc khác nhau; Props ở W02 giải quyết phần đó.

## Bài 4 — Chẩn đoán (15 phút)

Tạo lỗi tạm thời, quan sát thông báo rồi sửa ngay:

1. Đổi import default Header thành named import.
2. Đổi `<Header />` thành `<header />` và quan sát Elements, nội dung.
3. Xóa `return` của một component đơn giản.

Ghi lỗi nào làm hỏng import, lỗi nào tạo thẻ HTML thay vì component, lỗi nào làm mất nội dung. Kết thúc bài phải khôi phục ứng dụng bình thường.

## Tiêu chí hoàn thành

- [ ] App ghép năm vùng nội dung đúng cây đã vẽ.
- [ ] Phân biệt component React với thẻ HTML.
- [ ] Dùng được named và default import/export.
- [ ] Một component được dùng ở hai vị trí.
- [ ] Không có component được định nghĩa bên trong App.
- [ ] Giải thích được lý do tách từng component bằng trách nhiệm của nó.
