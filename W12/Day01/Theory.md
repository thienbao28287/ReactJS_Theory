# W12 · Day01 — Data Router: loader, pending và lỗi

## Mục tiêu và nhịp học

Thử tải dữ liệu theo route mà không trộn hai Router gốc.

Thuộc tuần **React nâng cao và tổng kết**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop và React/React DOM cùng major 19 cho các API React 19: kiểm tra npm ls react react-dom, nâng cùng nhau bằng npm install react@19 react-dom@19 nếu cần. Giữ react-router-dom@6 từ W05 cho Data Router. Làm các demo nâng cao trong module riêng, không thay state manager của dự án đã hoàn thiện.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Data Router

createBrowserRouter định nghĩa route object; RouterProvider thay BrowserRouter/Routes ở app lab. Loader nhận params/request, tải dữ liệu trước khi render element mới phù hợp.

### 2. Loading đúng nơi

useNavigation mô tả navigation đang diễn ra sau khi router hoạt động; lần tải ban đầu có fallbackElement ở RouterProvider trong v6. Không coi loader là luôn thay thế mọi effect trong app.

### 3. Lỗi và hủy

Throw Response với status khi tài nguyên không có, errorElement/useRouteError hiển thị. Dùng request.signal cho fetch để navigation hủy được công việc mạng phù hợp.

## Ví dụ có thể thử

Ví dụ React: đặt trong src/LessonDemo.jsx, dùng default import để hiển thị từ App.jsx. Đây là demo độc lập; không thay toàn bộ ứng dụng bán hàng bằng demo khi ghép tính năng.

```jsx
import { createBrowserRouter, RouterProvider, useLoaderData, useRouteError, isRouteErrorResponse } from 'react-router-dom';
async function loader({ params, request }) {
  const response = await fetch('/products.json', { signal: request.signal });
  if (!response.ok) throw new Response('Không tải được dữ liệu', { status: response.status });
  const products = await response.json();
  if (!Array.isArray(products)) throw new Error('Sai model sản phẩm');
  const product = products.find(p => String(p.id) === params.id);
  if (!product) throw new Response('Không có sản phẩm', { status: 404 });
  return product;
}
function Detail() { const product = useLoaderData(); return <h1>{product.title}</h1>; }
function ErrorPage() { const error = useRouteError(); return <h1>{isRouteErrorResponse(error) ? `Lỗi ${error.status}` : 'Có lỗi dữ liệu'}</h1>; }
const router = createBrowserRouter([{ path: '/products/:id', loader, element: <Detail />, errorElement: <ErrorPage /> }]);
export default function LessonDemo() { return <RouterProvider router={router} fallbackElement={<p>Đang khởi tạo</p>} />; }
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Giữ BrowserRouter bao RouterProvider; đọc useLoaderData ở route không có loader tương ứng.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: React Router (1).pdf, trang 9–13; roadmap React 18/19 Hooks, Zustand, Redux Saga; GitHub Lesson-10/11 để tổng kết dự án.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://react.dev/reference/react).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day02/Theory.md).
