# W08 · Day05 — createAsyncThunk và request lifecycle

## Mục tiêu và nhịp học

Quản lý pending/fulfilled/rejected và tránh response cũ ghi đè.

Thuộc tuần **Redux Toolkit và async state**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop; npm install @reduxjs/toolkit@2 react-redux@9. Chỉ giữ một nguồn dữ liệu giỏ hàng: sau khi chuyển sang Redux, gỡ việc dùng CartContext ở giao diện tương ứng. Demo tự có Provider; khi ghép app thật, dùng Provider duy nhất ở entry.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Thunk async

createAsyncThunk tạo ba action lifecycle và có thunkAPI.signal/requestId. Nó không tự tạo reducer cho trạng thái; extraReducers phải định nghĩa cách cập nhật.

### 2. Rejected có kiểm soát

throw dùng cho lỗi bất ngờ; rejectWithValue cho payload lỗi nghiệp vụ đã chuẩn hóa. Component muốn catch kết quả thunk có thể await dispatch(thunk()).unwrap().

### 3. Request id và hủy

Khi có nhiều request, chỉ nhận kết quả có requestId hiện hành. Cleanup có thể gọi promise.abort; không hiển thị aborted như lỗi người dùng.

## Ví dụ có thể thử

Lưu src/features/products/productsSlice.js. Ví dụ đầy đủ module slice; tích hợp store bằng key products rồi import loadProducts vào page.

```js
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
export const loadProducts = createAsyncThunk('products/load', async (_, { signal }) => {
  const r = await fetch('/products.json', { signal });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  const data = await r.json();
  if (!Array.isArray(data)) throw new Error('Sai dữ liệu');
  return data;
});
const slice = createSlice({ name: 'products', initialState: { data: [], status: 'idle', error: null, requestId: null }, reducers: {}, extraReducers: builder => {
  builder.addCase(loadProducts.pending, (state, action) => { state.status = 'loading'; state.error = null; state.requestId = action.meta.requestId; });
  builder.addCase(loadProducts.fulfilled, (state, action) => { if (state.requestId === action.meta.requestId) { state.status = 'succeeded'; state.data = action.payload; state.requestId = null; } });
  builder.addCase(loadProducts.rejected, (state, action) => { if (state.requestId === action.meta.requestId) { state.status = action.meta.aborted ? 'idle' : 'failed'; state.error = action.meta.aborted ? null : action.error.message; state.requestId = null; } });
} });
export default slice.reducer;
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Nghĩ dispatch thunk reject sẽ tự throw cho await nếu chưa unwrap; quên xử lý requestId.

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

[Bài tiếp theo](../Day06/Theory.md).
