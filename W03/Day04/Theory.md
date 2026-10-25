# W03 · Day04 — fetch và HTTP cơ bản

## Mục tiêu và nhịp học

Tải JSON, kiểm tra HTTP status và hiển thị dữ liệu trong React.

Thuộc tuần **useEffect và API**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Từ gốc ReactJS, chạy npm create vite@latest W03/api-lab -- --template react, sau đó cd W03/api-lab, npm install và npm run dev. Dùng dự án này cả tuần; không tạo lại mỗi ngày. Ví dụ dùng /products.json: tạo public/products.json chứa [{"id":1,"title":"Book","price":80},{"id":2,"title":"Pen","price":10}]. Đây là fixture cục bộ để học độc lập với mạng.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Hai bước của fetch

await fetch trả Response; await response.json đọc body. HTTP 404/500 thường không tự reject, phải kiểm tra response.ok rồi throw lỗi.

### 2. Không đặt async trực tiếp vào effect

Callback effect phải trả cleanup hoặc undefined, không trả Promise. Tạo hàm async bên trong và gọi nó; xử lý lỗi để không có rejection bị bỏ quên.

### 3. Tách trạng thái request

Data, loading và error mô tả request. Khi bắt đầu tải mới phải xóa lỗi cũ; kết thúc phải dừng loading, kể cả thất bại. Hôm nay dùng flag ignore, ngày mai nâng ca lỗi.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useEffect, useState } from 'react';
export default function LessonDemo() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState('');
  useEffect(() => {
    let ignore = false;
    async function load() {
      try {
        const response = await fetch('/products.json');
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        if (!Array.isArray(data)) throw new Error('Dữ liệu phải là array');
        if (!ignore) setProducts(data);
      } catch (err) { if (!ignore) setError(err.message); }
    }
    load();
    return () => { ignore = true; };
  }, []);
  return <section>{error ? <p role="alert">{error}</p> : <ul>{products.map(p => <li key={p.id}>{p.title}</li>)}</ul>}</section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Viết useEffect(async () => ...); mặc định mọi response đều là JSON hợp lệ.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: Hook Trong ReactJS (2).pdf, trang 2–4; GitHub Lesson-03; roadmap Component Lifecycle và useEffect.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/learn/synchronizing-with-effects).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day05/Theory.md).
