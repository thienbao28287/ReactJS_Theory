# W08 · Day06 — RTK Query và giới thiệu typed hooks

## Mục tiêu và nhịp học

Thử cache server state riêng và nhận biết typed hooks trong tài liệu.

Thuộc tuần **Redux Toolkit và async state**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop; npm install @reduxjs/toolkit@2 react-redux@9. Chỉ giữ một nguồn dữ liệu giỏ hàng: sau khi chuyển sang Redux, gỡ việc dùng CartContext ở giao diện tương ứng. Demo tự có Provider; khi ghép app thật, dùng Provider duy nhất ở entry.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Server state khác client state

RTK Query quản lý request/cache/subscription theo endpoint+argument. Giỏ client vẫn ở cart slice; không cần copy response RTK Query vào products slice bằng effect.

### 2. Tích hợp đủ hai phần

API reducer và middleware phải gắn vào store; hook generated chỉ hoạt động dưới Provider đúng store. refetch/invalidatesTags là cơ chế có chủ đích, không gọi refetch trong render.

### 3. TypeScript là tùy chọn

PDF có typed hooks: RootState/AppDispatch suy ra từ store và hooks pretyped. Dự án hiện tại JavaScript không ép chuyển toàn bộ sang TS trong một buổi; đọc và giải thích trước.

## Ví dụ có thể thử

Lưu src/services/productsApi.js. Store cần sửa như yêu cầu bài 1 trước khi gọi generated hook; ví dụ module không tự thay configureStore hiện có.

```js
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
export const productsApi = createApi({
  reducerPath: 'productsApi',
  baseQuery: fetchBaseQuery({ baseUrl: '/' }),
  endpoints: builder => ({ getProducts: builder.query({ query: () => 'products.json' }) }),
});
export const { useGetProductsQuery } = productsApi;
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Chỉ import hook nhưng quên middleware; dùng isLoading cho mọi lần refetch mà không hiểu isFetching.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: React-redux.pdf, trang 2–11; GitHub Lesson-09; roadmap Redux Toolkit. RTK Query và typed hooks là phần mở rộng.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://redux.js.org/tutorials/quick-start).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day07/Theory.md).
