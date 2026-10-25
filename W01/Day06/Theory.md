# W01 · Day06 — Xây trang hồ sơ học tập

## Mục tiêu và lịch học

Ghép kiến thức JavaScript, JSX và Component thành một trang hoàn chỉnh, có CSS cơ bản và bố cục sử dụng được trên màn hình nhỏ.

120 phút: 10 phút ôn, 25 phút đọc phương pháp, 75 phút [thực hành](./Exercises.md), 10 phút kiểm tra. Đây là buổi áp dụng, không học thêm thư viện.

## 1. Đọc yêu cầu rồi phân rã

Sản phẩm gồm Header, Profile, Skills, LearningGoals, Footer. Tận dụng code Day05 thay vì tạo dự án khác. Bắt đầu bằng nội dung và semantic HTML, sau đó mới chỉnh màu/khoảng cách.

Một yêu cầu tốt phải quan sát được. “Giao diện đẹp” khó kiểm chứng; “không cuộn ngang ở chiều rộng 375px, chữ không đè nhau, link mở đúng” kiểm tra được.

## 2. Cấu trúc tối thiểu

```text
src/
  components/
    Header.jsx
    Profile.jsx
    Skills.jsx
    LearningGoals.jsx
    Footer.jsx
    StudyReminder.jsx
  App.jsx
  main.jsx
  index.css
```

Một file CSS chung đủ cho bài này. Chưa cần folder services, Redux, Router hoặc framework CSS. Giữ file cấu hình template; chỉ gỡ tài nguyên mẫu khi chắc chắn không còn import đến nó.

## 3. Đặt dữ liệu và cấu trúc giao diện

Dùng object tĩnh trong module hoặc trong component. Ví dụ hoàn chỉnh cho Profile, có thể thay nội dung bằng thông tin của bạn:

```jsx
const profile = {
  name: 'Thien Bao',
  city: 'Ha Noi',
  goal: 'Tự xây dựng ứng dụng React đầu tiên',
};

export default function Profile() {
  return (
    <section className="panel" aria-labelledby="profile-heading">
      <h2 id="profile-heading">Về tôi</h2>
      <p>Tôi là {profile.name}, hiện ở {profile.city}.</p>
      <p>{profile.goal}</p>
    </section>
  );
}
```

Dùng một h1 làm tiêu đề chính; h2 cho các phần. Danh sách có `ul/ol` và `li`. Link là `a` với `href` thật. Không tạo button giả chưa có hành động.

## 4. CSS nền tảng đủ dùng

Bạn có thể dùng đoạn sau làm điểm bắt đầu trong `src/index.css`, sau đó tự chỉnh. Đảm bảo `main.jsx` import file này và CSS mẫu cũ không gây xung đột.

```css
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  line-height: 1.6;
  color: #172033;
  background: #f3f6fa;
}

.container {
  width: min(100% - 2rem, 960px);
  margin-inline: auto;
}

.site-header,
.site-footer {
  padding-block: 2rem;
}

.content-grid {
  display: grid;
  gap: 1rem;
}

.panel {
  padding: 1.5rem;
  border: 1px solid #cbd5e1;
  border-radius: 12px;
  background: #ffffff;
}

a {
  color: #1745a0;
  overflow-wrap: anywhere;
}

a:focus-visible {
  outline: 3px solid #1745a0;
  outline-offset: 4px;
}

@media (min-width: 720px) {
  .content-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```

`container` giới hạn chiều rộng và tạo lề; grid một cột trên màn hình nhỏ, hai cột khi đủ chỗ. Muốn áp dụng, gán đúng `className` cho wrapper. CSS không tự hiểu component nào là Header hay Profile.

## 5. Cách tự kiểm tra trước khi nhờ người khác

1. Đọc terminal: có lỗi biên dịch không?
2. Đọc Console: có lỗi runtime hoặc cảnh báo không?
3. Kiểm tra Elements: class, cấu trúc tiêu đề, CSS có đúng không?
4. Thu nhỏ 375px và mở rộng 1280px: có chữ tràn hoặc cuộn ngang không?
5. Dùng Tab đến link: có thấy vị trí focus không?

Nếu thêm ảnh vào `public/avatar.jpg`, tham chiếu bằng `/avatar.jpg`, không phải đường dẫn ổ đĩa Windows. Nếu chưa có ảnh, bỏ phần ảnh để tránh tài nguyên hỏng.

## Nguồn và phần bổ sung

- Tích hợp nội dung component/JSX/Vite từ PDF `ReactJS (1) (1).pdf`, trang 2–7.
- [GitHub Lesson-01](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory/Lesson-01) và [roadmap JSX/Components](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- Semantic HTML, responsive CSS và quy trình kiểm tra là phần bổ sung thực hành để bài chạy được thành một trang sử dụng được, không phải chương nâng cao bắt buộc của tuần đầu.

Tiếp theo: [Day07 — Ôn tập](../Day07/Theory.md).
