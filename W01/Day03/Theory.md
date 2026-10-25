# W01 · Day03 — React, SPA và cấu trúc dự án

## Mục tiêu và thời lượng

Bạn giải thích được vai trò React, phân biệt SPA/MPA, hiểu sơ bộ render và tìm được file cần sửa trong dự án Vite.

120 phút: 10 phút ôn công cụ, 35 phút lý thuyết, 65 phút [bài tập](./Exercises.md), 10 phút tự giải thích. Dùng lại `W01/react-profile` đã tạo ở Day02.

## 1. React giải quyết vấn đề gì?

React là thư viện JavaScript xây dựng giao diện. Bạn mô tả giao diện cần hiển thị từ dữ liệu; React tổ chức việc render và cập nhật DOM. Một ứng dụng được chia thành các component có trách nhiệm rõ ràng: Header, Profile, Footer.

So với tự tìm phần tử rồi gán `textContent`, cách viết khai báo tập trung vào kết quả giao diện. W01 dùng dữ liệu tĩnh; State để thay đổi giao diện do tương tác sẽ học ở W02.

React không tự cung cấp mọi chức năng của sản phẩm: Router, công cụ form hoặc quản lý dữ liệu có thể được bổ sung khi cần. Không nên cài toàn bộ thư viện của 12 tuần ngay ngày đầu.

## 2. SPA và MPA

| Góc nhìn | SPA dùng điều hướng phía client | MPA truyền thống |
| --- | --- | --- |
| Chuyển màn hình nội bộ | JavaScript cập nhật giao diện, thường không tải document mới | Thường yêu cầu document HTML mới |
| Dữ liệu và tài nguyên | Có thể tải thêm API, ảnh, JavaScript theo nhu cầu | Có thể tải lại document và tận dụng cache tài nguyên |
| Ví dụ kiểu tương tác | Dashboard chuyển tab giữ khung giao diện | Các trang nội dung được server trả riêng |

Không phải mọi click trong SPA đều tránh reload: link ra ngoài, refresh hoặc điều hướng document vẫn có thể tải trang mới. React có thể tham gia nhiều mô hình render, không chỉ SPA.

Tài liệu gốc tóm tắt SPA có hạn chế SEO. Cách hiểu chính xác hơn: SPA chỉ render ở client có thể làm việc lập chỉ mục và hiển thị nội dung ban đầu khó hơn; kết quả phụ thuộc cách triển khai, công cụ tìm kiếm và có dùng server rendering/prerender hay không. Chưa cần triển khai các kỹ thuật này trong W01.

## 3. DOM và Virtual DOM

DOM là cấu trúc đối tượng trình duyệt dùng để biểu diễn document. Khi React render, nó tính mô tả giao diện từ component. Khi dữ liệu thay đổi, React đối chiếu kết quả và commit những cập nhật cần thiết lên DOM.

```text
Dữ liệu đầu vào
    ↓
Component tính giao diện (render)
    ↓
React đối chiếu cấu trúc
    ↓
Commit cập nhật DOM khi cần
    ↓
Trình duyệt hiển thị
```

“Virtual DOM” là cách nói phổ biến về biểu diễn giao diện trong bộ nhớ; không phải một bản sao đầy đủ của mọi thuộc tính DOM thật. Render lại component không đồng nghĩa mọi DOM node đều bị tạo lại. Cơ chế này cũng không bảo đảm luôn nhanh hơn mọi cách thao tác DOM thủ công.

## 4. Đọc cây thư mục Vite

```text
react-profile/
  node_modules/
  public/
  src/
    App.jsx
    main.jsx
    index.css
  index.html
  package.json
  package-lock.json
```

Template có thể có thêm file như `App.css`, `assets`, cấu hình lint và Vite. Tên thực tế có thể thay đổi theo template.

- `index.html`: document gốc, chứa phần tử có id `root` và entry script.
- `src/main.jsx`: khởi động React, gắn cây component vào DOM container.
- `src/App.jsx`: component đầu ứng dụng; nơi ghép các phần giao diện.
- `src/index.css`: CSS chung nếu được import từ entry.
- `public`: tài nguyên được phục vụ trực tiếp, tham chiếu bằng đường dẫn từ gốc.
- `node_modules`: package đã cài, không sửa trực tiếp và không commit.
- `package.json`: dependencies và scripts. `package-lock.json` khóa cây phiên bản npm; nên commit.

## 5. Theo dấu từ HTML đến component

Trong `main.jsx` của template, bạn thường thấy `createRoot`, `<StrictMode>` và `<App />`. Giữ cấu hình có sẵn. `StrictMode` bổ sung kiểm tra trong phát triển; có thể chạy thêm một số thao tác để phát hiện lỗi, không có nghĩa giao diện production bị hiển thị hai lần.

Luồng cần nhớ: `index.html` → `main.jsx` → `App.jsx` → component con. CSS chỉ tác động khi được nạp qua import hoặc liên kết phù hợp.

## Nguồn

- PDF `ReactJS (1) (1).pdf`, trang 2–4 và 7.
- [GitHub Lesson-01](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory/Lesson-01).
- [Roadmap](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap): JSX/Components và Virtual DOM.
- Đọc thêm: [React — Render and Commit](https://react.dev/learn/render-and-commit).

Tiếp theo: [Day04 — JSX](../Day04/Theory.md).
