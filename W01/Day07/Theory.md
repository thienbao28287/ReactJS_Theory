# W01 · Day07 — Ôn tập, tự đánh giá và lưu kết quả

## Mục tiêu và thời lượng

Tự dựng được giao diện nhỏ, giải thích được code đã viết và ghi lại phần cần ôn trước W02. Buổi này không thêm React State, Router hay thư viện mới.

120 phút: 15 phút nhớ lại không nhìn tài liệu, 15 phút đối chiếu lý thuyết, 70 phút [bài tổng kết](./Exercises.md), 20 phút kiểm tra và commit.

## 1. Sơ đồ kiến thức W01

```text
JavaScript
  Hàm, object/array, destructuring, spread, module
  map/filter/find, Promise, async/await
       ↓
Node + npm + Vite
       ↓
index.html → main.jsx → App → Component con
       ↓
JSX + dữ liệu tĩnh + CSS
       ↓
Trang hồ sơ học tập
```

Bạn chưa cần nhớ mọi cú pháp. Điều quan trọng là biết dữ liệu ở đâu, file nào chạy trước, component nào hiển thị phần nào và đọc thông báo lỗi để tìm đúng chỗ sửa.

## 2. Những phân biệt phải nói rõ được

| Cặp khái niệm | Điều cần nhớ |
| --- | --- |
| Node / trình duyệt | Hai môi trường chạy JavaScript, có API khác nhau |
| npm / Vite | Quản lý package và scripts / công cụ dev server và build |
| React / JSX | Thư viện UI / cú pháp mô tả giao diện |
| HTML tag / component | Chữ thường / tên bắt đầu bằng chữ hoa trong JSX |
| Render / commit DOM | Tính giao diện / áp dụng thay đổi vào DOM |
| Default / named export | Import không có ngoặc nhọn / import khớp tên với ngoặc nhọn |
| Biến thường / State | Biến thường chưa cung cấp cơ chế yêu cầu React cập nhật giao diện; State học ở W02 |

## 3. Đọc lỗi theo thứ tự

- Lỗi cú pháp JSX: kiểm tra file/dòng báo lỗi, thẻ đóng, dấu ngoặc, phần tử bao ngoài.
- Không tìm thấy module: kiểm tra đường dẫn tương đối, tên file, chữ hoa/thường.
- Không có export phù hợp: kiểm tra named/default.
- Trang trắng: xem terminal và Console trước khi sửa CSS.
- Không có style: kiểm tra import CSS và className, sau đó mới xem thứ tự ghi đè.

Sửa một nguyên nhân rồi chạy lại. Đổi nhiều thứ ngẫu nhiên khiến bạn khó biết cách sửa nào có tác dụng.

## 4. Lưu bài bằng Git

Thư mục gốc ReactJS đã có repository; không chạy `git init` trong từng ngày hay trong dự án con. Từ thư mục gốc:

```powershell
git status --short
git add W01
git diff --cached --stat
git diff --cached
git commit -m "docs: complete week 01 React fundamentals"
```

Chỉ commit sau khi xem diff đúng nội dung muốn lưu. Không thêm `node_modules`, `dist`, thông tin bí mật hoặc file không liên quan. Vite thường tạo `.gitignore` trong dự án; kiểm tra nó thực sự bỏ qua các thư mục đầu ra. Commit message có thể đổi cho phù hợp nội dung bài thực hành.

Nếu Git báo thiếu danh tính, cấu hình tên/email của bạn theo hướng dẫn lỗi; không dùng thông tin giả hoặc của người khác. Chưa cần push hay tạo remote để hoàn thành W01.

## 5. Điều kiện chuyển W02

Bạn tự tạo được component, truyền dữ liệu tĩnh vào JSX, ghép nhiều component và sửa lỗi import cơ bản. Nếu JavaScript còn yếu, dành thêm thời gian cho hàm/object/array trước; Hooks không thay thế nền tảng JavaScript.

W02 sẽ trả lời: làm sao component nhận dữ liệu khác nhau qua Props, và làm sao giao diện đổi khi người dùng thao tác với State?

## Nguồn và đối chiếu cả tuần

- Nguồn chính: PDF `ReactJS (1) (1).pdf`, trang 2–7; [GitHub Theory/Lesson-01](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory/Lesson-01); [roadmap](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap), bài JSX và Components, Virtual DOM.
- JavaScript, CSS, cách luyện tập và tiêu chí đánh giá là phần bổ sung để học theo nhịp 2 tiếng/ngày.
- PDF Props & State, Hooks, Router và Redux dành cho các tuần sau; W01 không cố đưa hết nội dung ba nguồn vào bảy ngày.
- Đối chiếu cú pháp: [React Learn](https://react.dev/learn), [Vite Guide](https://vite.dev/guide/).
