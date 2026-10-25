# W05 · Day05 — Query params và useLocation

## Mục tiêu và nhịp học

Đồng bộ tìm kiếm với URL để refresh và chia sẻ được.

Thuộc tuần **Điều hướng với React Router**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Trong W04/mini-shop, chạy npm install react-router-dom@6. Dùng nhánh v6 để khớp PDF, không trộn import/cấu hình framework mode của phiên bản khác. Dự án chỉ có một BrowserRouter: các demo bên dưới tự bọc Router, vì vậy main.jsx không bọc thêm. Giữ trang sản phẩm hiện có để ghép dần.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Path và query khác vai trò

/products/:id nhận diện tài nguyên; ?q=book&category=all là bộ lọc. Query values là chuỗi và có thể thiếu hoặc sai, phải có default/validation.

### 2. Một nguồn dữ liệu chuẩn

useSearchParams đọc/ghi URL. Tránh vừa state query chính vừa URL query chính mà không có quy tắc đồng bộ. Input nháp có thể riêng nếu chỉ submit mới đổi URL.

### 3. Giữ param khác

Khi sửa q, sao chép URLSearchParams hiện tại để không xóa category/page ngoài ý muốn. useLocation đọc pathname/search/state nhưng state không thay persistence bền vững.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { BrowserRouter, useSearchParams, useLocation } from 'react-router-dom';
function Search() {
  const [params, setParams] = useSearchParams();
  const location = useLocation();
  const query = params.get('q') ?? '';
  function update(value) {
    const next = new URLSearchParams(params);
    value ? next.set('q', value) : next.delete('q');
    setParams(next, { replace: true });
  }
  return <section><label>Tìm<input value={query} onChange={e => update(e.target.value)} /></label><p>{location.pathname}: {query}</p></section>;
}
export default function LessonDemo() { return <BrowserRouter><Search /></BrowserRouter>; }
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Nối query bằng chuỗi thủ công; thay toàn bộ params chỉ để sửa một trường.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: React Router (1).pdf, trang 2–8; GitHub Lesson-07; roadmap Routing/Navigation.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://reactrouter.com/6.30.1).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day06/Theory.md).
