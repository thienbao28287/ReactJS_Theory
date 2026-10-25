# W01 · Day07 — Bài tổng kết tuần

Đọc [Theory](./Theory.md). Tổng thời gian: 120 phút; kiểm tra trí nhớ trước, đối chiếu sau. Không xem lời giải của các ngày trước trong phần tự làm.

## Phần A — Nhớ lại kiến thức (15 phút)

Trả lời ngắn vào `W01/Day07/review.md`:

1. React, JSX và Vite khác nhau như thế nào?
2. Vì sao `const` không có nghĩa object bất biến?
3. `map`, `filter`, `find` trả về gì?
4. Hàm `async` trả về gì; `await` dùng để làm gì?
5. Fragment giải quyết vấn đề nào?
6. Vì sao `<Profile />` khác `<profile />`?
7. Dữ liệu JavaScript đi vào JSX bằng cách nào?
8. Render lại có luôn thay toàn bộ DOM không?
9. Luồng từ `index.html` đến component con đi qua các file nào?
10. Làm sao phân biệt lỗi import với lỗi CSS?

## Phần B — Đối chiếu (15 phút)

Đọc lại đúng mục lý thuyết tương ứng với câu chưa chắc. Viết câu sửa bằng lời của mình và ghi ngày cần ôn lại. Mục tiêu là phát hiện lỗ hổng, không chép nguyên đoạn tài liệu.

## Phần C — Tự xây một màn hình mới (45 phút)

Trong `W01/react-profile`, giữ lại các component cũ. Tạo `src/WeeklySummary.jsx` bằng default export, rồi tạm đổi `App.jsx` để hiển thị màn hình này.

Màn hình cần có:

- Component Header và Footer dùng lại từ dự án.
- Một h1: `Tổng kết tuần đầu học React`.
- Component `StudySummary` đặt ở cấp module hoặc file riêng, chứa dữ liệu tên người học, số ngày đã học và số giờ/ngày.
- Tổng thời gian tính bằng biểu thức; 7 ngày × 2 giờ hiển thị 14 giờ.
- Ba mục kiến thức bằng `ul/li`: JavaScript, JSX, Component.
- Link thật đến tài liệu React.
- Bố cục không tràn ở 375px; không lỗi Console.

Chưa dùng Props, State, Router hay API. Không cần tự dựng lại tooling. Khi xong, khôi phục App hiển thị trang hồ sơ của Day06; giữ WeeklySummary để lưu bài tự kiểm tra.

## Phần D — Bài JavaScript ngắn (15 phút)

Viết `W01/Day07/checkpoint.mjs` với dữ liệu:

```js
const lessons = [
  { id: 1, title: 'JavaScript', completed: true },
  { id: 2, title: 'JSX', completed: true },
  { id: 3, title: 'Component', completed: false },
];
```

Yêu cầu:

1. Lấy tên các bài đã hoàn thành → `['JavaScript', 'JSX']`.
2. Tạo array mới đánh dấu id 3 hoàn thành, array gốc vẫn giữ `false`.
3. Tìm id 99 và hiển thị `Không tìm thấy bài học` khi kết quả là `undefined`.

Chạy `node W01/Day07/checkpoint.mjs` từ thư mục gốc và đối chiếu kết quả. Có thể dùng Console nếu chưa chạy được Node, nhưng cần ghi rõ lỗi môi trường để xử lý.

## Phần E — Kiểm tra và lưu bài (30 phút)

Dành 10 phút đầu kiểm tra trang hồ sơ sau khi khôi phục. Thử ba kích thước màn hình, link, tiêu đề và Console. Sau đó dành 20 phút ghi tổng kết, kiểm tra diff và commit theo Theory. Không push nếu chưa chủ động thiết lập remote.

Trong `review.md`, ghi:

- Ba kiến thức tự giải thích được.
- Hai lỗi đã tự sửa và nguyên nhân.
- Một phần cần ôn lại trước W02.
- Điểm tự chấm theo thang dưới đây.

## Thang tự chấm: 10 điểm

| Hạng mục | Điểm tối đa |
| --- | --- |
| Trả lời đúng ít nhất 8/10 câu sau đối chiếu, giải thích được bằng lời mình | 2 |
| Màn hình tổng kết có cấu trúc và component đúng | 3 |
| JSX và phép tính giờ đúng; dữ liệu đổi thì kết quả đổi | 1 |
| Ba yêu cầu JavaScript chạy đúng, không sửa array gốc | 2 |
| Không lỗi Console, không tràn ngang, link đúng | 1 |
| Có tổng kết và kiểm tra thay đổi bằng Git | 1 |

Đạt từ 8 điểm, đồng thời ứng dụng chạy và không còn vướng hàm/import/JSX cơ bản: chuyển W02. Nếu chưa đạt, ưu tiên làm lại đúng phần yếu trong 1–2 buổi; chưa cần bổ sung thư viện hay làm thêm giao diện mới.
