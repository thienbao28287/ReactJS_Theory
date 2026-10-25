# W11 · Day05 — Conflict, README và bàn giao

## Mục tiêu và nhịp học

Giải quyết conflict có hiểu nội dung và viết hướng dẫn tái hiện dự án.

Thuộc tuần **Tổ chức dự án, Git và triển khai**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Các lệnh Git thực hiện ở gốc ReactJS, không git init ở dự án con. Lệnh npm chạy trong W04/mini-shop. Trước khi thao tác branch/merge, lưu công việc và đọc git status. Bài Docker cần Docker Desktop đã hoạt động; nếu chưa có, vẫn phải đọc và giải thích Dockerfile, đánh dấu phần chạy thực tế chưa hoàn thành.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Conflict là quyết định nội dung

Hai nhánh sửa cùng đoạn khiến Git cần bạn chọn/ghép. Không bấm accept all mà bỏ mất yêu cầu một bên. Sau merge phải chạy lại test.

### 2. Lab an toàn

Tạo repository tạm riêng để mô phỏng conflict, không dùng file bài học đang làm làm nơi phá thử. git merge --abort chỉ hủy merge đang diễn ra, không thay việc lưu công việc.

### 3. README đủ chạy

Ghi Node/package manager, cài npm ci, env mẫu, dev/build/test, fixture, route và giới hạn auth/checkout mô phỏng. Chỉ ghi URL deploy nếu có thật.

## Ví dụ có thể thử

Khung README là ví dụ hoàn chỉnh tối thiểu để sửa theo dự án; bổ sung kết quả và URL thật khi đã có. Không ghi tên lab lồng .git vào app chính hoặc commit nhầm repo lab vào repository học.

```text
# Mini Shop học React

## Cài đặt
Chạy npm ci trong W04/mini-shop sau khi đã clone repository và có lockfile.

## Cấu hình
Sao chép .env.example thành .env.local; fixture dùng API base URL /.

## Chạy
npm run dev

## Kiểm tra
npx vitest run
npm run build

## Phạm vi
Auth và checkout là mô phỏng; không có giao dịch thanh toán thật.
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Dùng git reset --hard để thoát conflict mà mất công việc; README ghi lệnh chưa từng chạy.

Khi lỗi xuất hiện, đọc terminal và Console trước; xác định lỗi ở dữ liệu, luồng cập nhật hay cách hiển thị. Chỉ sửa một nguyên nhân mỗi lần, chạy lại đúng thao tác gây lỗi rồi kiểm tra một trường hợp bình thường để tránh làm hỏng phần đang hoạt động.

## Những điều cần tự giải thích

1. Vấn đề nào của ứng dụng được giải quyết bởi bài hôm nay?
2. Dữ liệu đi vào đâu, thay đổi ở đâu và được hiển thị ở đâu?
3. Nếu bỏ cơ chế chính trong ví dụ, hành vi nào sẽ thay đổi?

Viết câu trả lời vào notes.md cùng thư mục Day, kèm một lỗi thực tế và cách sửa. Hoàn thành khi đạt các tiêu chí trong Exercises, không chỉ khi đã đọc xong.

## Nguồn và phạm vi

- Tài liệu gốc đối chiếu: GitHub Lesson-10 và Lesson-11; roadmap Build/Deployment. Đây là phần quy trình dự án mở rộng ngoài các PDF React cốt lõi.
- [Thư mục Theory trên GitHub](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory).
- [Roadmap React](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).
- [Tài liệu chính thức để kiểm tra API](https://vite.dev/guide/static-deploy.html).

Ví dụ, dữ liệu fixture, cách chia 2 tiếng và tiêu chí bài tập được biên soạn bổ sung. Những chỗ ghi mô phỏng dùng để học luồng giao diện; không coi đó là API hay xác thực production.

[Bài tiếp theo](../Day06/Theory.md).
