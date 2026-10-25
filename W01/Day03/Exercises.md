# W01 · Day03 — Hiểu ứng dụng trước khi viết thêm

Thực hành 65 phút với `W01/react-profile`; dành 10 phút cuối ghi chú. Tham khảo [Theory](./Theory.md).

## Bài 1 — Bản đồ file (15 phút)

Tìm và ghi vào `W01/Day03/notes.md`:

1. Dòng HTML chứa `id="root"`.
2. Dòng nạp entry script.
3. File gọi `createRoot` và file được import dưới tên `App`.
4. Script được chạy bởi `npm run dev` trong `package.json`.
5. Nơi import CSS toàn cục.

Kết quả cần có: sơ đồ do chính bạn viết, đi từ document đến nội dung trên trình duyệt; giải thích từng mũi tên trong một câu.

## Bài 2 — Thử nghiệm có kiểm soát (15 phút)

1. Đổi `<title>` trong `index.html` thành `Hồ sơ học tập của tôi`; quan sát tên tab.
2. Đổi nội dung `h1` trong `App.jsx`; quan sát nội dung trang.
3. Thêm quy tắc `body { background: #f4f7fb; }` vào file CSS đang được import.
4. Tạm bỏ import file CSS đó, ghi điều thay đổi rồi khôi phục import.

Không sửa `node_modules`. Nếu còn CSS mặc định khác ghi đè giao diện, dùng DevTools để tìm nguồn quy tắc thay vì thêm liên tiếp `!important`.

## Bài 3 — Quan sát document và tài nguyên (15 phút)

Mở DevTools → Network, tải lại ứng dụng và quan sát document, script, stylesheet. Ghi tên ít nhất ba tài nguyên cùng loại của chúng. Nếu thấy kết nối phục vụ cập nhật nóng của Vite, ghi nhận đây là hành vi môi trường phát triển.

Chưa cần chứng minh điều hướng SPA hôm nay vì chưa có Router. Trả lời bằng lý thuyết: tại sao ứng dụng SPA vẫn cần tải thêm ảnh hoặc API?

## Bài 4 — Giải thích và sửa nhận định (20 phút)

Đánh dấu đúng/sai và sửa các câu sai:

1. React là công cụ cài package.
2. SPA chỉ tải mọi thứ đúng một lần, không tải thêm tài nguyên.
3. Mỗi lần component render, toàn bộ DOM thật luôn được thay mới.
4. `App.jsx` thường ghép các component con thành giao diện ứng dụng.
5. Nên sửa thư viện trực tiếp trong `node_modules`.
6. Virtual DOM bảo đảm mọi ứng dụng React luôn nhanh hơn DOM viết tay.

Đáp án kiểm tra: chỉ câu 4 đúng. Với câu 2, phân biệt document với dữ liệu/tài nguyên. Với câu 3, phân biệt tính kết quả render với commit DOM.

## Tiêu chí hoàn thành

- [ ] Biết sửa title, nội dung trang và CSS ở đúng file.
- [ ] Tự giải thích được Node, Vite, React trong luồng chạy dự án.
- [ ] Phân biệt được render với cập nhật DOM ở mức khái niệm.
- [ ] Không còn lỗi đỏ trong Console do các thử nghiệm hôm nay.
