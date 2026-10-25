# W08 · Day06 — Bài tập: RTK Query và giới thiệu typed hooks

Đọc [Theory](./Theory.md) trước. Phần thực hành có 65 phút; nằm trong buổi 120 phút đã phân bổ. Dùng dự án và phiên bản thư viện ghi trong Theory. Các file lời giải/notes do bạn tạo khi học; bộ tài liệu này không làm bài thay bạn.

## Kết quả cần tạo

Thử cache server state riêng và nhận biết typed hooks trong tài liệu.

## Bài 1 — Gắn API (15 phút)

Tạo module productsApi; trong configureStore thêm [productsApi.reducerPath]: productsApi.reducer và middleware: getDefaultMiddleware => getDefaultMiddleware().concat(productsApi.middleware). Giữ cart reducer.

## Bài 2 — Lab cache (30 phút)

Tạo trang lab dùng useGetProductsQuery ở hai component cùng argument, đọc isLoading/isFetching/error/data. Dùng Network/DevTools quan sát cache; không khẳng định số request khi StrictMode/HMR khác môi trường.

## Bài 3 — Typed hooks (20 phút)

Đọc PDF Redux trang 10 và quick start chính thức. Ghi RootState/AppDispatch/useSelector.withTypes/useDispatch.withTypes dùng để làm gì. Chọn thunk hoặc RTK Query cho app chính, không đồng bộ cả hai.

## Tự kiểm tra kết quả

- [ ] RTK Query có cả reducer và middleware.
- [ ] Không copy response sang slice không cần thiết.
- [ ] Phân biệt TypeScript type với runtime validation.

Với mỗi tiêu chí, ghi thao tác kiểm tra và kết quả thực tế; đánh dấu chưa đạt nếu chưa chạy được. Nếu API ngoài lỗi, dùng fixture cục bộ theo Theory để tiếp tục kiểm tra UI, đồng thời ghi rõ chưa xác nhận tích hợp mạng thật.

## Bàn giao cuối ngày (10 phút ngoài phần thực hành)

- Lưu code ở dự án đang dùng; lưu giải thích ở notes.md trong Day này.
- Ghi đầu vào, kết quả mong đợi và kết quả thực tế của ít nhất một ca bình thường và một ca biên/lỗi liên quan bài.
- Viết ba câu giải thích cơ chế chính bằng lời của bạn, một lỗi đã sửa và một điểm cần ôn.
- Đọc thay đổi bằng Git trước khi commit riêng phần đã hoàn thành; không commit node_modules, dist hoặc dữ liệu nhạy cảm.

## Tự chấm và quyết định chuyển bài

10 điểm: 4 điểm cho hành vi đúng, 2 điểm cho ca biên/lỗi, 2 điểm cho cách tổ chức code, 2 điểm cho giải thích và bằng chứng kiểm tra. Đạt từ 8 điểm và không còn lỗi ngăn chạy phần cốt lõi thì chuyển bài. Nếu chưa đạt, ghi chính xác hạng mục cần bù vào ngày ôn tập; ưu tiên sửa nền tảng thay vì thêm thư viện.
