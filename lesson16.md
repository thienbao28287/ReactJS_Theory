# Bài 16: Build, triển khai và hoàn thiện ứng dụng

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn kiểm tra bản production, triển khai SPA lên Vercel và phục vụ cùng bản build bằng Docker với Nginx. Bạn sẽ làm quen pipeline CI để mỗi lần mở Pull Request đều có bước kiểm tra trước khi ghép code.

### Kiến thức cần có và chuẩn bị

Dùng project `react-shop` ở [bài 15](./lesson15.md), có `package-lock.json`, script `build`, `preview` và `lint` từ Vite template. Cần GitHub/Vercel để tự triển khai; Docker Engine hoặc Docker Desktop đang chạy để thử container. Phần Docker có thể thực hành sau nếu máy chưa cài công cụ, không ảnh hưởng cách build bằng Vite.

Bạn sẽ thao tác trong tài khoản và repository thực hành của mình. Không đưa file `.env` hoặc secret vào Git. API mẫu dùng URL công khai `https://dummyjson.com`.

### Kết quả sau bài học

- Phân biệt dev server, production build và preview.
- Deploy Vite lên Vercel, cấu hình biến môi trường và SPA fallback.
- Build Docker nhiều giai đoạn và phục vụ static bằng Nginx.
- Tạo CI chạy lint/build cho Pull Request và hiểu giới hạn của kết quả đó.
- Kiểm tra ứng dụng bằng các luồng người dùng cụ thể.

## 1. Kiểm tra bản production ở local

### Bước 1 Cài đúng dependencies và build

Trong project đã có lockfile đồng bộ, chạy lần lượt:

```bash
npm ci
npm run lint
npm run build
npm run preview
```

`npm ci` cài theo lockfile và yêu cầu nó khớp package.json. Nếu bạn cố ý đổi dependencies, chạy `npm install` để cập nhật lockfile, review rồi commit cả hai file. Không xóa lockfile chỉ để CI chạy qua.

Vite ghi sản phẩm build vào `dist`. `preview` phục vụ thử bản build tại địa chỉ được terminal in ra, không phải dev server có cập nhật nóng. Đây là công cụ kiểm tra local; không dùng làm dịch vụ production lâu dài.

### Bước 2 Thử các luồng

1. Mở `/`, đi tới `/products`, tải danh sách và mở chi tiết.
2. Thêm sản phẩm, chuyển sang chi tiết: số lượng ở Header vẫn giữ.
3. Tải lại URL chi tiết trực tiếp và kiểm tra routing.
4. Thử ID không tồn tại, đường dẫn không khai báo và Offline.
5. Kiểm tra 390px và màn hình desktop; dùng Tab/Enter để đi qua liên kết và nút.

Build thành công chứng minh mã có thể tạo bundle; chưa chứng minh request thật thành công hoặc mọi tương tác đúng. Nếu sửa code sau build, cần build lại trước khi đánh giá bản production mới.

## 2. Triển khai SPA lên Vercel

### Bước 1 Chuẩn bị Git và cấu hình

Đẩy code đã kiểm tra lên repository GitHub của bạn, bao gồm package.json và lockfile. Không đẩy thư mục `dist` nếu nền tảng sẽ tự build từ source.

Với ứng dụng React Router chạy thuần phía client ở root domain và không có API route cùng project, tạo `vercel.json` tại root:

```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

Mục đích là khi truy cập thẳng `/products/1`, server vẫn phục vụ tài liệu SPA để Router xử lý đường dẫn. Nếu dự án có server/API route hoặc framework routing khác, cần thiết kế rule phù hợp thay vì sao chép fallback rộng này.

### Bước 2 Import project

Trong Vercel, tạo project từ repository thực hành và kiểm tra cấu hình:

| Cấu hình | Giá trị cho ví dụ |
| --- | --- |
| Framework | Vite. |
| Root Directory | Thư mục có package.json của `react-shop`. |
| Build Command | `npm run build`. |
| Output Directory | `dist`. |
| Environment | `VITE_API_BASE_URL=https://dummyjson.com`. |

Thiết lập biến cho môi trường deploy cần dùng, ví dụ Preview và Production. Sau khi thay biến, tạo lượt deploy mới vì Vite đưa cấu hình vào bundle lúc build. Trong project thật, kiểm tra chính sách và giới hạn tài khoản trước khi bật thêm dịch vụ.

### Bước 3 Kiểm tra URL đã deploy

Mở URL Vercel trả về, thực hiện lại các luồng ở phần 1. Mở trực tiếp `/products/1` trong tab mới và refresh: trang chi tiết phải tải được. Kiểm tra Network gọi đúng API HTTPS, không phải địa chỉ localhost của máy bạn.

Nếu lỗi, đọc build log hoặc Console/Network để phân biệt lỗi build, route fallback, thiếu env, CORS và API. So sánh request cụ thể trước khi thay code.

## 3. Phục vụ ứng dụng bằng Docker

**Image** là gói cấu hình và file để chạy ứng dụng; **container** là phiên đang chạy từ image. Với SPA Vite, Node được dùng để build, sau đó Nginx phục vụ các file tĩnh. Không cần chạy dev server bên trong container production.

### Bước 1 Tạo cấu hình Nginx

Tạo `nginx.conf` tại root project:

```nginx
server {
  listen 80;
  server_name _;
  root /usr/share/nginx/html;
  index index.html;

  location / {
    try_files $uri $uri/ /index.html;
  }

  location /assets/ {
    try_files $uri =404;
  }
}
```

`try_files` tìm file thật trước, rồi trả index.html cho đường dẫn SPA. Riêng `/assets/` trả 404 nếu thiếu file để không gửi HTML giả làm JavaScript. Ví dụ chỉ chạy HTTP local ở cổng được ánh xạ; public production cần HTTPS ở hạ tầng phía trước.

### Bước 2 Tạo Dockerfile

Tạo file `Dockerfile`, không có đuôi mở rộng:

```dockerfile
FROM node:24-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
ARG VITE_API_BASE_URL=https://dummyjson.com
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL
RUN npm run build

FROM nginx:stable-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
```

Multi-stage build giữ Node và dependencies build ở giai đoạn đầu; image cuối chỉ cần Nginx và file tĩnh. Các image tag trong ví dụ không khóa digest, có thể thay đổi theo thời gian; dự án cần tái hiện nghiêm ngặt nên kiểm tra và cố định digest theo quy trình nhóm.

Tạo `.dockerignore`:

```text
node_modules
dist
.git
.env
.env.*
npm-debug.log*
```

Build arg chỉ truyền URL công khai. Không dùng ARG/ENV của Dockerfile để nhúng secret vào frontend. Đổi environment lúc chạy Nginx không tự đổi URL đã được Vite đóng vào file JS.

### Bước 3 Build và chạy

Chạy trong thư mục có Dockerfile, package.json và nginx.conf:

```bash
docker build --build-arg VITE_API_BASE_URL=https://dummyjson.com -t react-shop:local .
docker run --rm -d -p 8080:80 --name react-shop-local react-shop:local
docker logs react-shop-local
```

Mở `http://localhost:8080`, thử danh sách, chi tiết và refresh `/products/1`. Nếu tên container đã được dùng, kiểm tra `docker ps -a` và xác định container của bài thực hành trước khi dừng hoặc chọn tên khác. Nếu cổng 8080 đang bận, đổi phần bên trái, ví dụ `8081:80`.

Kết thúc thử nghiệm bằng:

```bash
docker stop react-shop-local
```

`--rm` khiến container được xóa sau khi dừng; image vẫn còn để dùng lại. Docker không tự sửa CORS, không thay backend và không biến state trong trình duyệt thành dữ liệu lưu trên server.

## 4. Tạo pipeline CI cơ bản

**CI** chạy các bước kiểm tra tự động khi có thay đổi. **CD** đưa bản đã kiểm tra lên môi trường đích theo quy trình nhóm; có thể có bước phê duyệt. Bài này tạo CI lint/build. Vercel có thể tự tạo preview/production deploy từ Git theo cấu hình riêng.

Tạo `.github/workflows/ci.yml` trong project thực hành:

```yaml
name: Frontend checks

on:
  pull_request:
  push:
    branches: [main, develop]

permissions:
  contents: read

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 24
          cache: npm
      - run: npm ci
      - run: npm run lint
      - run: npm run build
        env:
          VITE_API_BASE_URL: https://dummyjson.com
```

Workflow giả định package.json nằm ở root repository `react-shop`, có lockfile và script lint/build. Nếu project ở thư mục con, cần cấu hình working-directory cùng cache-dependency-path cho đúng. Nếu chưa có test script, không thêm `npm test` giả để tạo cảm giác đã kiểm thử.

Đẩy workflow lên feature branch và mở PR. Xem tab kiểm tra để xác nhận job đã chạy, không chỉ có file YAML. Thử một lỗi import trên nhánh thực hành để thấy CI thất bại, rồi sửa và push lại. CI này không gửi request live, không chạy trình duyệt và không triển khai Docker; bước publish image/deploy server cần registry và hạ tầng cụ thể ngoài ví dụ.

## 5. Bài thực hành tổng hợp sau 16 buổi

Từ base bài 15, hoàn thiện một cửa hàng thực hành. Thực hiện từng mốc, commit sau khi tự kiểm tra đạt. Các chức năng dưới đây là yêu cầu tự làm để tổng hợp bài trước, không phải cam kết base tối thiểu đã có sẵn.

| Mốc | Yêu cầu | Cách tự kiểm tra |
| --- | --- | --- |
| Giao diện | Dùng component, CSS/Tailwind tạo layout responsive. | 390px không cuộn ngang; Tab thấy focus; có nhãn input. |
| Catalog | Danh sách, tìm kiếm debounce, phân trang và chi tiết. | URL query đúng; đổi ID nhanh không hiện dữ liệu cũ; có loading/error/empty. |
| Giỏ | Thêm, tăng, giảm, xóa; tính tổng theo USD. | Thêm trùng gộp số lượng; tổng đúng; chuyển route vẫn giữ. |
| Form | Form người nhận dùng RHF + Zod. | Đầu vào sai không submit; đang gửi khóa nút; lỗi không xóa dữ liệu. |
| Phiên mô phỏng | Context lưu user và protected route cho trang đặt hàng. | Chưa đăng nhập bị chuyển về login; đăng xuất cập nhật Header. |
| Dữ liệu | Chọn service/Hook hoặc RTK Query cho catalog. | Không giữ hai bản catalog độc lập; có cleanup hoặc vòng đời cache rõ ràng. |
| Quy trình | Feature branch, PR, README và CI. | Reviewer đọc được cách chạy; lint/build thực sự chạy và pass. |
| Triển khai | Có URL Vercel; thử Docker local nếu đã cài. | Refresh URL con được; API HTTPS đúng; container phục vụ bản build. |

Nút Đặt hàng chỉ tạo bản ghi mô phỏng trong phiên hoặc storage theo thiết kế bạn ghi rõ. Không thu tiền, không giả định API mẫu lưu đơn thật. Đăng nhập mẫu ở bài 11 chỉ phục vụ học state; không dùng làm xác thực production.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Local được nhưng CI lỗi import | Kiểm tra chữ hoa/thường trong tên file; Linux phân biệt. |
| `npm ci` báo lockfile không khớp | Cập nhật có chủ ý bằng npm install, review và commit lockfile. |
| Refresh URL con trả 404 | Kiểm tra fallback đúng nền tảng và deploy lại cấu hình. |
| Thay env nhưng URL API chưa đổi | Biến Vite được lấy lúc build; tạo bản build/deploy mới. |
| Container không lên | Xem docker logs, trạng thái daemon, tên container và cổng. |
| Build xanh nhưng trang không tải API | Kiểm tra URL, CORS, HTTPS và phản hồi trong Network. |

## 7. Ôn tập và hướng mở rộng

1. Dev server, preview và Nginx phục vụ ứng dụng ở các giai đoạn nào?
2. Vì sao server cần SPA fallback khi người dùng refresh URL con?
3. Vì sao đổi biến runtime của container không đổi được bundle Vite đã build?
4. Pipeline hiện tại kiểm tra được gì và chưa kiểm tra được gì?
5. Sau khi hoàn thành các mốc, mở rộng bằng test component/luồng người dùng, xác thực backend thật hoặc mutation/cache invalidation. Làm từng phần có tiêu chí kiểm tra, không nâng mọi thư viện cùng lúc.

## Tài liệu tham khảo

- [Vite: Build production](https://vite.dev/guide/build).
- [Vercel: Vite](https://vercel.com/docs/frameworks/frontend/vite).
- [Docker: Multi-stage builds](https://docs.docker.com/build/building/multi-stage/).
- [Nginx: try_files](https://nginx.org/en/docs/http/ngx_http_core_module.html#try_files).
- [GitHub Actions: Build và test Node.js](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-nodejs).

[Bài 15: Base project và Gitflow](./lesson15.md) | [Quay về roadmap](./README.md)
