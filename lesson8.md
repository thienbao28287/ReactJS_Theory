# Bài 8: Tái sử dụng logic bằng Custom Hooks

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn đưa logic state và Effect ra khỏi component để dùng lại. Bạn sẽ viết `useToggle`, `useDebounce` và `useFetch`, sau đó kiểm tra xem nhiều component dùng cùng Hook có chia sẻ state hay không.

### Kiến thức cần có và chuẩn bị

Bạn cần biết `useState`, `useEffect`, dependencies và cleanup ở [bài 4](./lesson4.md). Mở project Vite, chạy `npm run dev` và giữ `src/main.jsx` render `<App />`. Ví dụ dùng `fetch` có sẵn, không cần cài thư viện mới.

Tạo thư mục `src/hooks`. Mỗi ví dụ `App.jsx` thay thế ví dụ trước; các file Hook có thể giữ để dùng tiếp.

### Kết quả sau bài học

- Phân biệt hàm tiện ích, component và custom Hook.
- Tái sử dụng logic mà không vô tình giả định state được chia sẻ.
- Dọn timer và request khi đầu vào thay đổi.
- Hiển thị loading, lỗi và dữ liệu từ Hook gọi API.

## 1. Custom Hook là gì?

**Custom Hook** là hàm có tên bắt đầu bằng `use` theo sau bởi chữ hoa, gọi các React Hooks để đóng gói logic. Hook trả dữ liệu và các thao tác; component quyết định JSX.

| Nhu cầu | Cách tổ chức |
| --- | --- |
| Định dạng giá, không dùng Hook | Hàm JavaScript như `formatPrice`. |
| Hiển thị thẻ sản phẩm | Component như `ProductCard`. |
| Quản lý timer, state hoặc Effect để dùng lại | Hook như `useDebounce`. |

Gọi Hook ở cấp cao nhất của component hoặc Hook khác. Không gọi trong `if`, vòng lặp hoặc event handler. Mỗi lần component gọi Hook có state riêng; dùng chung file Hook không đồng nghĩa dùng chung dữ liệu.

## 2. Viết useToggle

### Bước 1 Tách logic đóng mở

Tạo `src/hooks/useToggle.js`:

```js
import { useCallback, useState } from "react";

export function useToggle(initialValue = false) {
  const [isOpen, setIsOpen] = useState(initialValue);
  const toggle = useCallback(() => setIsOpen((value) => !value), []);
  return { isOpen, toggle };
}
```

Hàm cập nhật nhận giá trị mới nhất nên không đọc `isOpen` từ closure. `initialValue` chỉ khởi tạo state; đổi prop sau khi mount không tự đặt lại state.

### Bước 2 Dùng hai lần độc lập

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import { useToggle } from "./hooks/useToggle";

function Details({ title }) {
  const { isOpen, toggle } = useToggle();
  return (
    <section>
      <h2>{title}</h2>
      <button onClick={toggle} aria-expanded={isOpen}>
        {isOpen ? "Thu gọn" : "Xem thêm"}
      </button>
      {isOpen && <p>Nội dung của {title}</p>}
    </section>
  );
}

export default function App() {
  return (
    <main>
      <h1>Thực hành Custom Hooks</h1>
      <Details title="Vận chuyển" />
      <Details title="Đổi trả" />
    </main>
  );
}
```

Nhấn Xem thêm ở Vận chuyển rồi kiểm tra Đổi trả vẫn đóng. Hai component chia sẻ cách xử lý, mỗi component giữ một state. Muốn hai nơi cùng một dữ liệu, đưa state lên cha hoặc dùng Context ở bài 11.

## 3. Viết useDebounce cho ô tìm kiếm

**Debounce** chỉ cập nhật giá trị sau khi người dùng ngừng thay đổi một khoảng thời gian. Cách này giảm số lần gọi API khi gõ liên tục; không làm request đang chạy tự hủy.

Tạo `src/hooks/useDebounce.js`:

```js
import { useEffect, useState } from "react";

export function useDebounce(value, delay = 400) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}
```

Khi `value` đổi, cleanup xóa timer cũ và Effect tạo timer mới. Khi component bị gỡ, timer còn chờ cũng được xóa. Giá trị lần đầu được trả ngay từ state khởi tạo.

## 4. Viết useFetch có cleanup

### Bước 1 Tạo Hook

Tạo `src/hooks/useFetch.js`:

```js
import { useEffect, useState } from "react";

export function useFetch(url) {
  const [result, setResult] = useState({
    url: null, data: null, loading: true, error: "",
  });

  useEffect(() => {
    const controller = new AbortController();
    let active = true;
    async function load() {
      try {
        const response = await fetch(url, { signal: controller.signal });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        if (active) setResult({ url, data, loading: false, error: "" });
      } catch (error) {
        if (!active || error.name === "AbortError") return;
        setResult({ url, data: null, loading: false, error: error.message });
      }
    }

    load();
    return () => {
      active = false;
      controller.abort();
    };
  }, [url]);

  if (result.url !== url) {
    return { data: null, loading: true, error: "" };
  }
  return { data: result.data, loading: result.loading, error: result.error };
}
```

`fetch` không tự ném lỗi cho HTTP 404 nên cần kiểm tra `response.ok`. `AbortController` yêu cầu hủy request; cờ `active` chặn kết quả của lần Effect cũ cập nhật state. Lưu URL cùng kết quả giúp không hiển thị dữ liệu của URL trước trong lần render chuyển đầu vào.

Hook này dành cho GET JSON với URL dạng chuỗi. Nó chưa cung cấp cache, phân trang, retry hoặc mutation; RTK Query ở bài 13 xử lý nhiều nhu cầu đó.

### Bước 2 Kết hợp tìm kiếm và gọi API

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import { useState } from "react";
import { useDebounce } from "./hooks/useDebounce";
import { useFetch } from "./hooks/useFetch";

export default function App() {
  const [query, setQuery] = useState("");
  const keyword = useDebounce(query.trim(), 400);
  const url = `https://dummyjson.com/products/search?q=${encodeURIComponent(keyword)}`;
  const { data, loading, error } = useFetch(url);
  const waiting = query.trim() !== keyword;

  return (
    <main>
      <h1>Tìm sản phẩm</h1>
      <label htmlFor="search">Tên sản phẩm</label>
      <input id="search" value={query} onChange={(e) => setQuery(e.target.value)} />
      {waiting || loading ? (
        <p role="status">Đang tìm kiếm...</p>
      ) : error ? (
        <p role="alert">Không tải được dữ liệu: {error}</p>
      ) : !Array.isArray(data?.products) ? (
        <p role="alert">Dữ liệu sản phẩm không hợp lệ.</p>
      ) : data.products.length === 0 ? (
        <p>Không tìm thấy sản phẩm.</p>
      ) : (
        <ul>{data.products.map((p) => <li key={p.id}>{p.title}</li>)}</ul>
      )}
    </main>
  );
}
```

URL là chuỗi được dựng từ keyword, không phải object mới đưa vào dependency. `encodeURIComponent` giữ ký tự như `&` nằm trong giá trị query thay vì trở thành tham số mới.

### Bước 3 Kiểm tra kết quả

1. Mở Network, nhập nhanh `phone`. Request tìm từ hoàn chỉnh chỉ bắt đầu sau khoảng chờ; vẫn có thể có request ban đầu khi mount.
2. Gõ từ khác khi mạng chậm: dữ liệu từ tìm kiếm cũ không được ghi đè kết quả mới.
3. Nhập chuỗi khó khớp để thấy danh sách rỗng.
4. Bật Offline rồi đổi từ khóa: thấy lỗi; trở lại Online và đổi từ khóa để thử lại.
5. Trong Strict Mode có thể thấy setup, cleanup rồi setup lại lúc phát triển. Request bị hủy trong lượt kiểm tra không phải lỗi cần hiển thị.

## 5. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Invalid hook call | Kiểm tra Hook có được gọi trong component/Hook khác, ở top-level không. |
| Hai component không cùng mở | Mỗi lần gọi `useToggle` có state riêng; đây là hành vi mong đợi. |
| API chạy liên tục | Kiểm tra dependencies có object hoặc hàm mới mỗi render không. |
| Kết quả cũ ghi đè kết quả mới | Giữ cleanup, cờ active và truyền signal. |
| Gõ xong chưa có dữ liệu ngay | Debounce phải chờ; sau đó còn thời gian request mạng. |

## 6. Ôn tập và bài tập thêm

1. Vì sao hàm định dạng tiền không cần tên bắt đầu bằng `use`?
2. Cleanup của debounce và cleanup của fetch giải quyết hai việc khác nhau như thế nào?
3. Thêm nút Xóa tìm kiếm và kiểm tra input cập nhật ngay.
4. Tách phần danh sách sang component nhận `products` qua props, giữ logic lấy dữ liệu trong App.
5. Bổ sung cơ chế thử lại bằng một state đếm và dependency tương ứng; không gọi Hook trong nút bấm.

## Tài liệu tham khảo

- [React: Tái sử dụng logic với Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks).
- [React: useEffect](https://react.dev/reference/react/useEffect).
- [DummyJSON: Tìm kiếm sản phẩm](https://dummyjson.com/docs/products).

[Bài 7: Styling](./lesson7.md) | [Bài 9: React Hook Form](./lesson9.md) | [Quay về roadmap](./README.md)
