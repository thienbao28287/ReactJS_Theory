# W11 · Day06 — Docker nhiều giai đoạn và Nginx

## Mục tiêu và nhịp học

Hiểu build image và phục vụ SPA static trong container.

Thuộc tuần **Tổ chức dự án, Git và triển khai**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Các lệnh Git thực hiện ở gốc ReactJS, không git init ở dự án con. Lệnh npm chạy trong W04/mini-shop. Trước khi thao tác branch/merge, lưu công việc và đọc git status. Bài Docker cần Docker Desktop đã hoạt động; nếu chưa có, vẫn phải đọc và giải thích Dockerfile, đánh dấu phần chạy thực tế chưa hoàn thành.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Image và container

Image là gói đã build, container là instance chạy từ image. Build React cần Node; phục vụ dist có thể dùng Nginx mà không mang node_modules vào runtime.

### 2. Multi-stage

Stage build npm ci/npm run build, stage runtime copy dist. .dockerignore loại node_modules, dist, .git và env cá nhân; COPY . . không được đưa secret không cần thiết vào build context.

### 3. Fallback và config

Nginx try_files cho client routes; asset lỗi không nên ngầm giả thành data JSON. VITE_ được bake lúc build, không tự đổi bằng docker run -e sau khi đã có dist.

## Ví dụ có thể thử

Lưu Dockerfile tại W04/mini-shop. nginx.conf và .dockerignore phải tạo theo bài trước khi docker build; không chạy build ở gốc ReactJS. Tham khảo https://docs.docker.com/build/building/multi-stage/.

```dockerfile
FROM node:24-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:stable-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Copy node_modules máy Windows vào Linux image; thiếu SPA fallback; dùng env runtime thay cho build-time mà không có cơ chế riêng.

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

[Bài tiếp theo](../Day07/Theory.md).
