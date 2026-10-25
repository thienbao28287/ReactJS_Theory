# W11 · Day04 — Gitflow thực hành và Pull Request

## Mục tiêu và nhịp học

Thực hiện một task trên branch riêng, commit có nghĩa và review thay đổi.

Thuộc tuần **Tổ chức dự án, Git và triển khai**. Tổng 120 phút: 10 phút nhớ lại bài trước, 35 phút đọc và chạy ví dụ, 65 phút làm [Exercises](./Exercises.md), 10 phút ghi chú và tự giải thích. Ngày ôn tập dùng 35 phút lý thuyết để đọc lại phần yếu thay vì học thêm thư viện.

## Chuẩn bị và nơi thực hành

Dùng W04/mini-shop. Các lệnh Git thực hiện ở gốc ReactJS, không git init ở dự án con. Lệnh npm chạy trong W04/mini-shop. Trước khi thao tác branch/merge, lưu công việc và đọc git status. Bài Docker cần Docker Desktop đã hoạt động; nếu chưa có, vẫn phải đọc và giải thích Dockerfile, đánh dấu phần chạy thực tế chưa hoàn thành.

Các lệnh cài đặt là hướng dẫn để bạn thực hành, chưa được tự động chạy khi mở tài liệu. Với ví dụ React, giữ cấu hình entry của Vite; không gọi component như hàm thường và không tắt lint để che lỗi dependency.

## Kiến thức trọng tâm

### 1. Luồng branch

main giữ mốc ổn định; feature/* cho tính năng; fix/* cho sửa lỗi. develop chỉ cần khi quy trình nhóm yêu cầu; bài học giải thích Gitflow, không bắt app cá nhân phải có mọi branch.

### 2. Commit nhỏ có nghĩa

Stage đúng file, xem diff staged, commit mô tả hành vi. Không git add . theo thói quen khi repository có nhiều tuần và thay đổi khác.

### 3. PR cụ thể

Mô tả vấn đề, hành vi sau sửa, cách kiểm tra, ảnh nếu UI đổi và giới hạn. Review tìm lỗi/rủi ro, không chỉ nhận xét style. Không force push nhánh dùng chung.

## Ví dụ có thể thử

Các lệnh là trình tự học ở gốc repository. Hãy tạo/thay đổi file trước git add/commit; nếu không có thay đổi Git sẽ không có gì để commit. Không chạy lại git init.

```powershell
git status --short
git switch -c feature/cart-empty-message
git diff -- W04/mini-shop
git add W04/mini-shop/src/features/cart
git diff --cached
git commit -m "fix: clarify empty cart message"
```

Trước khi chạy, dự đoán kết quả; sau khi chạy, thay một đầu vào và giải thích điều gì đổi. Ví dụ làm rõ cơ chế của bài; phần bài tập yêu cầu bạn vận dụng thành tính năng riêng.

## Lỗi dễ mắc và cách kiểm tra

Commit luôn file bài tập không liên quan; đổi branch khi chưa hiểu các thay đổi chưa lưu.

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

[Bài tiếp theo](../Day05/Theory.md).
