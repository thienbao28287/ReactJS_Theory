# W12 · Day05 — Redux Saga: generator và quản lý side effects

## Mục tiêu và nhịp học

Làm quen call/put/takeLatest và phân biệt hủy task với hủy mạng.

Thuộc tuần **React nâng cao và tổng kết**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop và React/React DOM cùng major 19 cho các API React 19: kiểm tra npm ls react react-dom, nâng cùng nhau bằng npm install react@19 react-dom@19 nếu cần. Giữ react-router-dom@6 từ W05 cho Data Router. Làm các demo nâng cao trong module riêng, không thay state manager của dự án đã hoàn thiện.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Generator và effects

function* trả iterator, yield mô tả công việc. call gọi tác vụ, put dispatch action; Saga middleware diễn giải effects. Reducer vẫn thuần.

### 2. takeLatest

Khi action mới đến, task cũ đang chạy bị cancel. Điều đó không tự làm mọi Promise/fetch hủy ở tầng mạng; dùng AbortController/finally khi cần.

### 3. Phạm vi học

Saga hữu ích cho workflow điều phối phức tạp. Thunk/RTK Query vẫn đủ cho nhiều CRUD. Buổi này dùng store lab riêng, không thêm Saga vào luồng products đang ổn định.

## Ví dụ có thể thử

Lưu src/labs/sagaStore.js. Demo export store/actions, không có component mặc định. Tạo UI lab theo bài 2; đọc thêm https://redux-saga.js.org/docs/introduction/BeginnerTutorial/.

```js
import { configureStore, createSlice } from '@reduxjs/toolkit';
import createSagaMiddleware from 'redux-saga';
import { call, put, takeLatest, cancelled } from 'redux-saga/effects';
const slice = createSlice({ name: 'sagaProducts', initialState: { data: [], status: 'idle' }, reducers: {
  requested(state) { state.status = 'loading'; },
  succeeded(state, action) { state.data = action.payload; state.status = 'success'; },
  failed(state) { state.status = 'error'; },
} });
async function fetchProducts(signal) {
  const r = await fetch('/products.json', { signal });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json();
}
function* worker() {
  const controller = new AbortController();
  try { const data = yield call(fetchProducts, controller.signal); yield put(slice.actions.succeeded(data)); }
  catch { yield put(slice.actions.failed()); }
  finally { if (yield cancelled()) controller.abort(); }
}
function* rootSaga() { yield takeLatest(slice.actions.requested.type, worker); }
const saga = createSagaMiddleware();
export const sagaStore = configureStore({ reducer: slice.reducer, middleware: getDefaultMiddleware => getDefaultMiddleware().concat(saga) });
saga.run(rootSaga);
export const { requested } = slice.actions;
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Quên middleware.run; coi takeLatest tự hủy mọi request bất kỳ; thêm Saga chỉ để fetch danh sách đơn giản.

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

[Bài tiếp theo](../Day06/Theory.md).
