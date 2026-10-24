# Bài 7: Styling với CSS, SASS và Tailwind CSS

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn tạo giao diện danh sách sản phẩm, tổ chức CSS và điều chỉnh bố cục theo kích thước màn hình. Bạn sẽ thử CSS thuần trước, sau đó viết lại bằng SASS và Tailwind để hiểu mỗi công cụ thay đổi cách làm việc như thế nào.

### Kiến thức cần có và chuẩn bị

Bạn cần biết component, props và render danh sách ở hai bài đầu; biết selector, box model, Flexbox và Grid trong CSS. Mở project Vite và chạy `npm run dev`. Giữ `src/main.jsx` render `<App />`.

Ba phần thực hành là các phương án thay thế nhau. Hoàn thành và kiểm tra một phương án trước khi chuyển sang phương án khác. Mọi đường dẫn `src/` trong bài thuộc project thực hành, không phải kho tài liệu này.

### Kết quả sau bài học

- Import CSS và dùng `className` trong component.
- Tạo danh sách responsive, có trạng thái hover và focus.
- Dùng biến, nesting của SASS và hiểu phạm vi CSS Modules.
- Cài Tailwind CSS v4 qua Vite plugin và viết utility classes.

## 1. CSS hoạt động trong React như thế nào?

React không thay thế cơ chế CSS của trình duyệt. Khi import file CSS vào mã nguồn, Vite xử lý file và đưa style vào ứng dụng. File CSS thông thường có phạm vi toàn trang; import trong component không tự giới hạn selector vào component đó.

| Cách viết | Khi nào phù hợp? |
| --- | --- |
| CSS thuần | Giao diện nhỏ, cần hiểu rõ cascade và selector. |
| CSS Modules | Muốn class được đổi tên để hạn chế trùng giữa các file. |
| SASS | Muốn thêm biến, nesting, mixin trong quy trình viết CSS. |
| Tailwind | Muốn ghép utility classes trực tiếp trong JSX. |

Không cần dùng cả bốn cách cho cùng một giao diện. Chọn cách nhóm hiểu và tổ chức nhất quán.

## 2. Tạo danh sách bằng CSS thuần

### Bước 1 Viết component

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import "./App.css";

const products = [
  { id: 1, name: "Tai nghe", price: 350000 },
  { id: 2, name: "Bàn phím", price: 700000 },
  { id: 3, name: "Chuột", price: 250000 },
];

const formatPrice = (price) =>
  new Intl.NumberFormat("vi-VN", {
    style: "currency", currency: "VND",
  }).format(price);

function ProductCard({ product }) {
  return (
    <article className="product-card">
      <h2>{product.name}</h2>
      <p>{formatPrice(product.price)}</p>
      <button onClick={() => window.alert(`Đã chọn ${product.name}`)}>
        Chọn sản phẩm
      </button>
    </article>
  );
}

export default function App() {
  return (
    <main className="catalog">
      <h1>Sản phẩm thực hành</h1>
      <div className="product-grid">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </main>
  );
}
```

Nút chỉ thông báo sản phẩm được chọn để kiểm tra tương tác, chưa thêm vào giỏ hàng. `Intl.NumberFormat` định dạng tiền; không thay đổi dữ liệu giá gốc.

### Bước 2 Viết CSS

Thay toàn bộ `src/App.css` bằng:

```css
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, sans-serif; color: #172033; }
button { font: inherit; }
.catalog { max-width: 1040px; margin: auto; padding: 32px 16px; }
.product-grid { display: grid; grid-template-columns: 1fr; gap: 20px; }
.product-card { border: 1px solid #cbd5e1; border-radius: 12px; padding: 24px; }
.product-card h2 { margin-top: 0; }
.product-card button {
  border: 0; border-radius: 6px; padding: 10px 16px;
  background: #1d4ed8; color: white; cursor: pointer;
}
.product-card button:hover { background: #1e40af; }
.product-card button:focus-visible { outline: 3px solid #111827; outline-offset: 3px; }
@media (min-width: 640px) {
  .product-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 960px) {
  .product-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
```

Nếu `main.jsx` đang import `index.css` chứa style demo như `body { display: flex }`, thay nội dung file đó bằng file rỗng khi làm ví dụ. Hai file cùng khai báo `body` có thể tạo kết quả khác dự kiến.

### Bước 3 Kiểm tra bố cục

1. Ở màn hình rộng từ 960px, kiểm tra có ba cột.
2. Thu về 700px: có hai cột; thu về 390px: có một cột và không cuộn ngang.
3. Dùng Tab để đến nút: phải thấy viền focus. Dùng Enter để kích hoạt nút.
4. Mở DevTools, kiểm tra computed styles nếu màu hoặc khoảng cách không đúng.

Media query dùng chiều rộng viewport, không phải chiều rộng riêng của thẻ. `minmax(0, 1fr)` giúp cột có thể co lại khi nội dung dài.

## 3. Viết lại bằng SASS

### Bước 1 Cài compiler và đổi import

```bash
npm install -D sass
```

Đổi dòng import trong `App.jsx` thành `import "./App.scss";`. Tạo `src/App.scss` với toàn bộ nội dung dưới đây. Không import cả `App.css` và `App.scss` cùng lúc trong ví dụ này.

```scss
$primary: #1d4ed8;
$border: #cbd5e1;

* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, sans-serif; color: #172033; }
button { font: inherit; }
.catalog { max-width: 1040px; margin: auto; padding: 32px 16px; }
.product-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  @media (min-width: 640px) { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  @media (min-width: 960px) { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
.product-card {
  border: 1px solid $border;
  border-radius: 12px;
  padding: 24px;
  h2 { margin-top: 0; }
  button {
    font: inherit;
    border: 0; border-radius: 6px; padding: 10px 16px;
    background: $primary; color: white; cursor: pointer;
    &:hover { background: #1e40af; }
    &:focus-visible { outline: 3px solid #111827; outline-offset: 3px; }
  }
}
```

`$primary` là biến được xử lý lúc biên dịch. `&:hover` tham chiếu selector hiện tại, tạo ra `.product-card button:hover`. SASS tạo CSS thông thường, trình duyệt không trực tiếp chạy biến SASS.

### Bước 2 Hiểu CSS Modules

Nesting không tự tạo phạm vi riêng. Để dùng CSS Modules, đặt tên file là `ProductCard.module.scss`, import bằng `import styles from "./ProductCard.module.scss"` rồi gắn `className={styles.card}` với selector `.card` trong file đó. Đây là cách chuyển đổi tên class; không viết `className="styles.card"`.

Phần CSS Modules là hướng mở rộng của component ở trên. Nếu chuyển sang Modules, cần chuyển các selector tương ứng và bỏ class toàn cục cũ của component để dễ theo dõi kết quả.

## 4. Thử Tailwind CSS v4

### Bước 1 Cài package và Vite plugin

```bash
npm install -D tailwindcss@4 @tailwindcss/vite@4
```

Với project Vite React dùng plugin React thông thường, thay toàn bộ `vite.config.js` bằng:

```js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
});
```

Nếu project có cấu hình khác cần giữ, chỉ thêm import và plugin Tailwind vào cấu hình hiện có. Ví dụ này dùng quy trình Tailwind v4; không chạy `tailwindcss init -p` của hướng dẫn v3.

### Bước 2 Thay CSS và component

Thay toàn bộ `src/index.css` bằng:

```css
@import "tailwindcss";
```

Giữ dòng `import "./index.css"` trong `src/main.jsx`. Thay toàn bộ `src/App.jsx` bằng:

```jsx
const products = [
  { id: 1, name: "Tai nghe" },
  { id: 2, name: "Bàn phím" },
  { id: 3, name: "Chuột" },
];

export default function App() {
  return (
    <main className="mx-auto max-w-5xl px-4 py-8 text-slate-900">
      <h1 className="mb-6 text-3xl font-bold">Sản phẩm thực hành</h1>
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {products.map((product) => (
          <article key={product.id} className="rounded-xl border border-slate-300 p-6">
            <h2 className="mb-4 text-xl font-semibold">{product.name}</h2>
            <button
              className="rounded-md bg-blue-700 px-4 py-2 text-white hover:bg-blue-800 focus-visible:outline-2 focus-visible:outline-offset-4"
              onClick={() => window.alert(`Đã chọn ${product.name}`)}
            >
              Chọn sản phẩm
            </button>
          </article>
        ))}
      </div>
    </main>
  );
}
```

Dừng và khởi động lại `npm run dev` sau khi đổi Vite config. Ví dụ Tailwind dùng breakpoint mặc định của Tailwind; `lg` không tương đương mốc 960px trong phần CSS thuần.

Tailwind cần nhìn thấy tên class hoàn chỉnh trong source. Khi đổi màu theo trạng thái, dùng `active ? "bg-blue-700" : "bg-slate-600"`, tránh ghép tên như `bg-${color}-700` khiến class không được tạo.

## 5. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| CSS ảnh hưởng component khác | Kiểm tra selector toàn cục; cân nhắc tên class rõ nghĩa hoặc Modules. |
| Trang nằm giữa màn hình và quá hẹp | Kiểm tra CSS demo trong `index.css` và `App.css`. |
| SASS không được xử lý | Kiểm tra package `sass`, đuôi `.scss` và đường dẫn import. |
| Tailwind không có tác dụng | Kiểm tra Vite plugin, import CSS trong `main.jsx`, khởi động lại server. |
| Màu động không xuất hiện | Dùng chuỗi class đầy đủ trong source. |

## 6. Ôn tập và bài tập thêm

1. Vì sao import CSS trong component không tự giới hạn phạm vi selector?
2. Biến SASS khác CSS custom property ở thời điểm xử lý như thế nào?
3. Tạo trạng thái hết hàng, disable nút và hiển thị chữ Hết hàng; không chỉ phân biệt bằng màu.
4. Thêm ảnh với `alt` mô tả sản phẩm và giữ ảnh không tràn thẻ.
5. Viết lại một ProductCard bằng CSS Modules rồi kiểm tra không ảnh hưởng các thẻ khác.

## Tài liệu tham khảo

- [Vite: CSS và CSS Modules](https://vite.dev/guide/features#css).
- [SASS: Tài liệu](https://sass-lang.com/documentation/).
- [Tailwind CSS: Cài với Vite](https://tailwindcss.com/docs/installation/using-vite).

[Bài 6: Axios](./lesson6.md) | [Bài 8: Custom Hooks](./lesson8.md) | [Quay về roadmap](./README.md)
