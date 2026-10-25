# W04 · Day03 — Custom Hook useFetch có cleanup

## Mục tiêu và nhịp học

Tách trạng thái tải dữ liệu thành Hook có URL đầu vào.

Thuộc tuần **Custom Hooks, Axios và dự án bán hàng**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Từ gốc chạy npm create vite@latest W04/mini-shop -- --template react; cd W04/mini-shop; npm install; npm install axios@1; npm run dev. W04–W12 dùng tiếp chính dự án này. Tạo public/products.json chứa [{"id":1,"title":"Book","price":80},{"id":2,"title":"Pen","price":10}]. Giá trong fixture là đơn vị quy ước, chưa cần chuyển đổi tiền tệ. Không tạo lại dự án vào các tuần sau.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Input và output

Hook nhận URL, trả data/loading/error. Component quyết định hiển thị, Hook quản lý đồng bộ và cleanup. Nếu URL rỗng, không gửi request.

### 2. Dependency phản ánh đầu vào

URL đổi thì request đổi; cleanup hủy request cũ. Nếu nhận object options tạo mới mỗi render, phải thiết kế ổn định để tránh loop; hôm nay chỉ nhận chuỗi URL.

### 3. Không hứa cache

Hook useFetch đơn giản không tự deduplicate, cache hoặc đồng bộ nhiều màn hình. Những nhu cầu đó dẫn tới thư viện server state như RTK Query, không tiếp tục nhồi mọi tính năng vào Hook hôm nay.

## Ví dụ có thể thử

Module Hook: lưu src/hooks/useFetch.js, import { useFetch } trong component. Module này không phải component default export.

```jsx
import { useEffect, useState } from 'react';
export function useFetch(url) {
  const [result, setResult] = useState({ data: null, loading: false, error: '' });
  useEffect(() => {
    if (!url) { setResult({ data: null, loading: false, error: '' }); return; }
    const controller = new AbortController();
    setResult({ data: null, loading: true, error: '' });
    async function load() {
      try {
        const response = await fetch(url, { signal: controller.signal });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        if (!controller.signal.aborted) setResult({ data, loading: false, error: '' });
      } catch (e) { if (!controller.signal.aborted) setResult({ data: null, loading: false, error: e.message }); }
    }
    load();
    return () => controller.abort();
  }, [url]);
  return result;
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Trả Promise từ effect; gọi Hook có điều kiện khi URL khác rỗng.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: Hook Trong ReactJS (2).pdf, trang 15; GitHub Lesson-04 và Lesson-07; roadmap Custom Hooks.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/learn/reusing-logic-with-custom-hooks).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day04/Theory.md).
