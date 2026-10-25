# W04 · Day06 — Service layer và khung mini-shop

## Mục tiêu và nhịp học

Tách giao tiếp dữ liệu khỏi UI để thay API mà không sửa toàn bộ component.

Thuộc tuần **Custom Hooks, Axios và dự án bán hàng**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Từ gốc chạy npm create vite@latest W04/mini-shop -- --template react; cd W04/mini-shop; npm install; npm install axios@1; npm run dev. W04–W12 dùng tiếp chính dự án này. Tạo public/products.json chứa [{"id":1,"title":"Book","price":80},{"id":2,"title":"Pen","price":10}]. Giá trong fixture là đơn vị quy ước, chưa cần chuyển đổi tiền tệ. Không tạo lại dự án vào các tuần sau.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Service trả dữ liệu nghiệp vụ

Service biết endpoint và chuẩn hóa response. Component biết loading/error và cách hiển thị. Không để component đọc response.data.data ở nhiều chỗ.

### 2. Tổ chức tối thiểu

services/productService.js, components/ProductCard.jsx, pages/ProductsPage.jsx đủ cho hiện tại. Không cần cấu trúc doanh nghiệp hàng chục folder chưa dùng.

### 3. Fixture và API thật

Fixture giữ schema ổn định để phát triển UI. Ghi rõ nguồn dữ liệu; khi đổi API thật phải ánh xạ id/title/price về cùng model và kiểm tra lại status/contract.

## Ví dụ có thể thử

Thay nội dung src/services/productService.js bằng module này khi làm bài; import getProducts từ ProductsPage. Không giữ hai phiên bản service trùng tên.

```js
import axios from 'axios';
const api = axios.create({ baseURL: '/', timeout: 8000 });
export async function getProducts({ signal } = {}) {
  const { data } = await api.get('products.json', { signal });
  if (!Array.isArray(data)) throw new Error('Sản phẩm phải là array');
  return data.map(item => {
    if (!Number.isFinite(item.price) || item.id == null || typeof item.title !== 'string') {
      throw new Error('Sản phẩm thiếu id, title hoặc giá hợp lệ');
    }
    return { id: item.id, title: item.title, price: item.price };
  });
}
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Vừa useFetch vừa gọi axios cho cùng danh sách; nuốt lỗi trong service rồi trả [] khiến UI hiểu nhầm empty.

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

[Bài tiếp theo](../Day07/Theory.md).
