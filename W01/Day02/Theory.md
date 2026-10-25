# W01 · Day02 — Xử lý dữ liệu, async và khởi tạo Vite

## Mục tiêu và lịch học

Biết dùng `map`, `filter`, `find`; phân biệt Promise với kết quả đã chờ; tạo được dự án React chạy trên máy.

120 phút: 10 phút ôn Day01, 35 phút học, 65 phút [thực hành](./Exercises.md), 10 phút tổng kết. Cài đặt/download có thể lâu tùy mạng; nếu cần, chuyển bài async mở rộng sang Day07.

## 1. Array methods thường gặp

```js
const products = [
  { id: 1, name: 'Book', price: 80000, inStock: true },
  { id: 2, name: 'Pen', price: 10000, inStock: false },
  { id: 3, name: 'Bag', price: 200000, inStock: true },
];
const names = products.map((product) => product.name);
const available = products.filter((product) => product.inStock);
const selected = products.find((product) => product.id === 2);
console.log(names, available.length, selected.name);
```

`map` biến đổi từng phần tử và tạo array mới; `filter` giữ phần tử đạt điều kiện; `find` trả phần tử đầu tiên phù hợp hoặc `undefined`. Các phương thức này không tự sửa array gốc, nhưng callback của bạn vẫn có thể sửa object bên trong: tránh làm vậy khi muốn giữ dữ liệu gốc.

```js
const discounted = products.map((product) => ({
  ...product,
  price: product.price * 0.9,
}));
console.log(products[0].price, discounted[0].price);
```

## 2. Promise và async/await

Promise biểu diễn kết quả có thể có trong tương lai. Hàm `async` luôn trả về Promise. `await` chờ Promise trong luồng của hàm async, không khóa toàn bộ trình duyệt.

```js
function loadCourse(shouldFail = false) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (shouldFail) {
        reject(new Error('Không tải được khóa học'));
        return;
      }
      resolve({ title: 'React cơ bản' });
    }, 300);
  });
}
async function showCourse(shouldFail) {
  try {
    const course = await loadCourse(shouldFail);
    console.log(course.title);
  } catch (error) {
    console.error(error.message);
  }
}
showCourse(false);
```

Ví dụ mô phỏng tác vụ bất đồng bộ, chưa cần API thật. `try/catch` xử lý Promise bị reject khi đã `await`. Không nên thêm `async` vào mọi hàm nếu hàm chỉ tính toán đồng bộ.

## 3. Vai trò công cụ

| Công cụ | Vai trò |
| --- | --- |
| Node.js | Chạy JavaScript ngoài trình duyệt, phục vụ công cụ phát triển |
| npm | Cài package và chạy scripts của dự án |
| Vite | Cung cấp dev server, xử lý mã nguồn và build |
| React | Mô tả và tổ chức giao diện bằng component |

Cài Node.js từ [trang chính thức](https://nodejs.org/en/download), chọn bản LTS được Vite hiện hành hỗ trợ; kiểm tra yêu cầu tại [Vite Guide](https://vite.dev/guide/). Mở lại terminal sau khi cài.

```powershell
node -v
npm -v
git --version
```

Nếu Git chưa có, cài từ [Git SCM](https://git-scm.com/downloads). W01 chỉ cần các thao tác cơ bản; chưa học Gitflow.

## 4. Tạo một dự án dùng suốt tuần

Chạy từ thư mục gốc `ReactJS`, không chạy từ Day02:

```powershell
npm create vite@latest W01/react-profile -- --template react
cd W01/react-profile
npm install
npm run dev
```

Mở URL terminal cung cấp; không mặc định port luôn là 5173. Dừng server bằng `Ctrl+C`. Những ngày sau dùng lại dự án này, không khởi tạo lại.

Để chạy module của Day01, đổi tên `helpers.js` thành `helpers.mjs`, `main.js` thành `main.mjs`, sửa import thành `./helpers.mjs`, rồi chạy `node W01/Day01/main.mjs` từ gốc. Đuôi `.mjs` giúp Node nhận diện ES module mà không cần sửa cấu hình thư mục gốc.

## Lỗi thường gặp

- `node`/`npm` không được nhận diện: mở terminal mới và kiểm tra cài đặt/PATH.
- Engine không tương thích: đối chiếu phiên bản Node với Vite Guide.
- PowerShell chặn `npm.ps1`: có thể gọi `npm.cmd` thay cho `npm`; chưa cần thay đổi execution policy toàn máy.
- `find` không thấy kết quả: kiểm tra trước khi đọc thuộc tính.
- Quên `await`: biến đang giữ Promise thay vì dữ liệu mong muốn.

## Nguồn

- PDF `ReactJS (1) (1).pdf`, trang 7: Node.js, npm, Vite.
- [GitHub Lesson-01](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory/Lesson-01): thiết lập môi trường.
- [MDN Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), [MDN async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).

Tiếp theo: [Day03 — React và cấu trúc dự án](../Day03/Theory.md).
