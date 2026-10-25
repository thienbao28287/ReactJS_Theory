# W04 · Day05 — Interceptors, Swagger và Postman

## Mục tiêu và nhịp học

Đọc hợp đồng API và quản lý interceptor có vòng đời rõ.

Thuộc tuần **Custom Hooks, Axios và dự án bán hàng**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Từ gốc chạy npm create vite@latest W04/mini-shop -- --template react; cd W04/mini-shop; npm install; npm install axios@1; npm run dev. W04–W12 dùng tiếp chính dự án này. Tạo public/products.json chứa [{"id":1,"title":"Book","price":80},{"id":2,"title":"Pen","price":10}]. Giá trong fixture là đơn vị quy ước, chưa cần chuyển đổi tiền tệ. Không tạo lại dự án vào các tuần sau.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Hợp đồng trước code

Đọc method, path, query/body, schema response và status. Postman giúp tách lỗi API với lỗi browser; gọi được trong Postman không bảo đảm browser không gặp CORS.

### 2. Interceptor dùng chung

Request interceptor có thể bổ sung header kỹ thuật; response interceptor chuẩn hóa lỗi. Phải return config/response hoặc Promise.reject để chuỗi không bị đứt.

### 3. Vòng đời và quyền hạn

Đăng ký một lần trên instance hoặc eject khi hết dùng. Demo chỉ thêm X-Learning-Client cho fixture cùng origin; không gửi header tùy ý tới API bên ngoài vì có thể gây preflight CORS.

## Ví dụ có thể thử

Module độc lập: thử ở src/services/interceptorDemo.js. Khi tích hợp, thêm interceptor vào instance api đã có; không tạo hai instance rồi cấu hình nhầm cái không dùng.

```js
import axios from 'axios';
export const api = axios.create({ baseURL: '/', timeout: 8000 });
const requestId = api.interceptors.request.use(config => {
  config.headers['X-Learning-Client'] = 'mini-shop';
  return config;
});
const responseId = api.interceptors.response.use(
  response => response,
  error => Promise.reject(error)
);
export function removeLearningInterceptors() {
  api.interceptors.request.eject(requestId);
  api.interceptors.response.eject(responseId);
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Đăng ký interceptor trong mỗi render; response error handler không reject nên nuốt lỗi.

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

[Bài tiếp theo](../Day06/Theory.md).
