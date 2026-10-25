# W03 · Day05 — Loading, error, empty và retry

## Mục tiêu và nhịp học

Thiết kế bốn trạng thái request và cơ chế thử lại không tạo vòng lặp.

Thuộc tuần **useEffect và API**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Từ gốc ReactJS, chạy npm create vite@latest W03/api-lab -- --template react, sau đó cd W03/api-lab, npm install và npm run dev. Dùng dự án này cả tuần; không tạo lại mỗi ngày. Ví dụ dùng /products.json: tạo public/products.json chứa [{"id":1,"title":"Book","price":80},{"id":2,"title":"Pen","price":10}]. Đây là fixture cục bộ để học độc lập với mạng.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Bốn trạng thái UI

Loading báo đang xử lý; error giải thích thất bại; empty là tải thành công nhưng không có item; success hiển thị data. Không dùng mảng rỗng để đại diện đồng thời loading và empty.

### 2. Retry là ý định người dùng

Dùng counter retry trong dependencies hoặc hàm tải được gọi rõ ràng. Không tự retry liên tục trong catch. Disable nút khi đang tải để giảm thao tác trùng.

### 3. Dữ liệu cũ và mới

Chọn rõ giữ data cũ khi tải lại hay xóa nó. Demo này xóa data khi bắt đầu; nếu giữ lại cần thể hiện đang cập nhật để người dùng hiểu đó là dữ liệu cũ.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { useEffect, useState } from 'react';
export default function LessonDemo() {
  const [attempt, setAttempt] = useState(0);
  const [result, setResult] = useState({ status: 'loading', data: [], error: '' });
  useEffect(() => {
    let ignore = false;
    setResult({ status: 'loading', data: [], error: '' });
    async function load() {
      try {
        const r = await fetch('/products.json');
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        const data = await r.json();
        if (!Array.isArray(data)) throw new Error('Sai cấu trúc dữ liệu');
        if (!ignore) setResult({ status: 'success', data, error: '' });
      } catch (e) { if (!ignore) setResult({ status: 'error', data: [], error: e.message }); }
    }
    load();
    return () => { ignore = true; };
  }, [attempt]);
  return <section>{result.status === 'loading' && <p role="status">Đang tải</p>}{result.status === 'error' && <p role="alert">{result.error}</p>}{result.status === 'success' && <p>{result.data.length ? `Có ${result.data.length} sản phẩm` : 'Chưa có sản phẩm'}</p>}<button disabled={result.status === 'loading'} onClick={() => setAttempt(a => a + 1)}>Thử lại</button></section>;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Đặt error vào dependency rồi setError trong effect gây vòng lặp; báo không có data khi request đang tải.

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

[Bài tiếp theo](../Day06/Theory.md).
