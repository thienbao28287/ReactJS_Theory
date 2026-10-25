# W11 · Day07 — CI/CD tổng quan và kiểm tra bản phát hành

## Mục tiêu và nhịp học

Tự động kiểm tra unit/build trong repository chứa nhiều tuần.

Thuộc tuần **Tổ chức dự án, Git và triển khai**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Các lệnh Git thực hiện ở gốc ReactJS, không git init ở dự án con. Lệnh npm chạy trong W04/mini-shop. Trước khi thao tác branch/merge, lưu công việc và đọc git status. Bài Docker cần Docker Desktop đã hoạt động; nếu chưa có, vẫn phải đọc và giải thích Dockerfile, đánh dấu phần chạy thực tế chưa hoàn thành.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. CI và CD

CI chạy kiểm tra tích hợp; CD triển khai sau điều kiện cho phép. Một workflow xanh chỉ xác nhận các lệnh nó chạy, không chứng minh mọi E2E/production đều đúng.

### 2. Thư mục làm việc

Repository nhiều tuần nên workflow đặt working-directory cho npm và cache-dependency-path đúng lockfile. npm ci cần lockfile đã commit và khớp package.json.

### 3. Phạm vi bài

Tự động unit/build trước; E2E cần khởi động server và cài browser phù hợp. Không thêm job deploy với secret giả; Vercel Git integration có thể lo deploy riêng.

## Ví dụ có thể thử

Workflow đầy đủ cho unit/build, chưa chạy E2E hoặc deploy. Actions major được ghi rõ để học; khi dùng trong nhóm hãy tuân chính sách pin/version của repository và xem tài liệu GitHub Actions.

```yaml
name: mini-shop-ci
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: W04/mini-shop
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 24
          cache: npm
          cache-dependency-path: W04/mini-shop/package-lock.json
      - run: npm ci
      - run: npx vitest run
      - run: npm run build
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Đặt root sai, cache sai lockfile; ghi workflow đã pass khi chỉ mới viết YAML.

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

[Bài tiếp theo](../../W12/Day01/Theory.md).
