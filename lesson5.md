# Bài 5: Sử dụng React.memo useMemo useCallback và useRef

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn kiểm soát những công việc được thực hiện lại khi component render và lưu tham chiếu khi cần thao tác với DOM. Bạn sẽ lần lượt thử `memo`, `useMemo`, `useCallback` và `useRef`, quan sát kết quả rồi xác định trường hợp phù hợp cho từng công cụ.

### Kiến thức cần có và chuẩn bị

Bạn cần nắm props, state và event handler ở bài 2; kiến thức Effect và cleanup ở [bài 4](./lesson4.md) sẽ được dùng trong bài tập mở rộng. Các API React dùng trong bài có sẵn trong package `react`.

Nếu project chưa cài dependencies, chạy `npm install` trước. Mở terminal tại project Vite, chạy `npm run dev` và mở địa chỉ Local. Với từng ví dụ hoàn chỉnh, thay toàn bộ nội dung `src/App.jsx` rồi lưu. Giữ `src/main.jsx` render `<App />`; các ví dụ này không cần router.

Để theo dõi log, mở DevTools của trình duyệt bằng F12 hoặc menu công cụ phát triển, chọn tab Console và xóa log trước mỗi lượt thử. Làm xong một ví dụ rồi mới thay sang ví dụ tiếp theo để tránh khai báo trùng component `App`.

### Kết quả sau bài học

- Phân biệt được render component với cập nhật DOM.
- Hiểu vì sao một prop object hoặc hàm mới có thể làm component con render lại.
- Chọn được công cụ ghi nhớ giá trị, tham chiếu hàm hoặc lưu ref.
- Dùng ref để focus input và biết khi nào dữ liệu phải được lưu bằng state.

## 1. Render và memoization

Khi state của component cha thay đổi, React thường gọi lại cha và các component con để tính giao diện. **Render không đồng nghĩa với thay đổi DOM**; React còn đối chiếu kết quả để quyết định thay đổi cần thiết.

**Memoization** là ghi nhớ kết quả hoặc tham chiếu để có thể dùng lại khi đầu vào chưa thay đổi. Nó có chi phí riêng, vì vậy hãy đo vấn đề trước khi thêm tối ưu.

| Công cụ                 | Ghi nhớ hoặc lưu gì?                              | Mục đích                                                               |
| ----------------------- | ------------------------------------------------- | ---------------------------------------------------------------------- |
| `memo` hay `React.memo` | Component được bọc để có thể bỏ qua render từ cha | Giảm render không cần thiết khi props không đổi.                       |
| `useMemo`               | Kết quả tính toán                                 | Tránh tính lại hoặc giữ tham chiếu giá trị khi dependencies không đổi. |
| `useCallback`           | Tham chiếu hàm                                    | Giữ callback ổn định khi dependencies không đổi.                       |
| `useRef`                | Object có thuộc tính `current`                    | Giữ DOM hoặc dữ liệu không cần kích hoạt render.                       |

`memo` là API bọc component, **không phải Hook**. Ba hàm có tiền tố `use` trong bảng là Hooks, cần được gọi ở cấp cao nhất của component hoặc custom Hook.

Các ví dụ minh họa cách ghi nhớ thủ công. Với dự án đã bật React Compiler, compiler có thể tự tối ưu giá trị, hàm và component, làm giảm nhu cầu thêm memoization bằng tay.

## 2. React memo

`memo(Component)` tạo phiên bản component mà React có thể bỏ qua render khi cha render lại nhưng props vẫn giống lần trước. Import `{ memo }` tương đương việc dùng API `React.memo` qua đối tượng `React`.

### Bước 1 Tạo component cha và con

Mục tiêu là để cha có một bộ đếm riêng, còn con luôn nhận giá trị `1`. Thay nội dung `src/App.jsx` bằng:

```jsx
import { memo, useState } from "react";

const Child = memo(function Child({ value }) {
  console.log("Child render");
  return <p>Giá trị của Child: {value}</p>;
});

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <main>
      <h1>Số lần bấm: {count}</h1>
      <button onClick={() => setCount((c) => c + 1)}>Tăng</button>
      <Child value={1} />
    </main>
  );
}
```

### Bước 2 Quan sát khi props giữ nguyên

Tải trang một lần để con được hiển thị, sau đó xóa log trong Console và nhấn Tăng vài lần. Số ở cha vẫn tăng. Vì prop `value` của con luôn là số `1`, React thường có thể bỏ qua việc gọi lại con cho những cập nhật này.

Đặt `memo` ở ngoài `App` như code trên để component được bọc không bị tạo lại mỗi lần cha render.

### Bước 3 Thử làm props thay đổi

Đổi `<Child value={1} />` thành `<Child value={count} />`, lưu file, xóa log rồi bấm Tăng. Lúc này con nhận giá trị mới nên phải tính lại giao diện. Qua hai lần thử, bạn có thể thấy `memo` không ngăn cập nhật cần thiết khi đầu vào thay đổi.

### Props được so sánh như thế nào?

Mặc định, `memo` so sánh từng prop bằng `Object.is`. Object, array và hàm mới tạo có tham chiếu mới, dù nội dung nhìn giống nhau:

```js
Object.is(1, 1); // true
Object.is({ value: 1 }, { value: 1 }); // false
Object.is(
  () => {},
  () => {},
); // false
```

Nếu truyền `options={{ value: 1 }}` mỗi lần cha render, `options` là object mới nên `memo` không thể coi prop đó là không đổi theo so sánh mặc định.

`memo` chỉ là tối ưu, không bảo đảm component không bao giờ render lại. State riêng của con hoặc context mà con sử dụng vẫn có thể làm con render. Strict Mode cũng có thể gọi thêm khi phát triển; không dùng số log như một cam kết hành vi production.

## 3. useMemo ghi nhớ kết quả tính toán

### Cú pháp

```jsx
const memoizedValue = useMemo(() => {
  return calculateValue(a, b);
}, [a, b]);
```

Đây là mẫu cú pháp: `calculateValue`, `a` và `b` cần có trong component tương ứng. `useMemo` gọi hàm tính toán trong lần đầu, rồi có thể dùng lại kết quả khi dependencies chưa đổi.

Hàm tính toán phải thuần. Không fetch API, thay đổi DOM hoặc gọi setter trong callback của `useMemo`.

### Ví dụ lọc danh sách

#### Bước 1 Tạo bộ lọc và một state không liên quan

Màn hình có ô tìm kiếm để thay đổi `query` và nút đổi giao diện để thay đổi `dark`. Ta dùng hai thao tác này để phân biệt khi nào bộ lọc cần tính lại. Thay nội dung `src/App.jsx` bằng:

```jsx
import { useMemo, useState } from "react";

const products = [
  { id: 1, name: "Điện thoại" },
  { id: 2, name: "Máy tính" },
  { id: 3, name: "Tai nghe" },
];

export default function App() {
  const [query, setQuery] = useState("");
  const [dark, setDark] = useState(false);

  const filteredProducts = useMemo(() => {
    console.log("Tính lại danh sách lọc");
    const keyword = query.trim().toLocaleLowerCase("vi");
    return products.filter((product) =>
      product.name.toLocaleLowerCase("vi").includes(keyword),
    );
  }, [query]);

  return (
    <main
      style={{
        background: dark ? "#222" : "#fff",
        color: dark ? "#fff" : "#222",
      }}
    >
      <h1>Sản phẩm</h1>
      <label>
        Tìm sản phẩm
        <input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
        />
      </label>
      <button onClick={() => setDark((value) => !value)}>Đổi giao diện</button>
      <ul>
        {filteredProducts.map((product) => (
          <li key={product.id}>{product.name}</li>
        ))}
      </ul>
    </main>
  );
}
```

#### Bước 2 Hiểu cách tạo danh sách hiển thị

`trim()` bỏ khoảng trắng hai đầu từ khóa; `toLocaleLowerCase("vi")` chuyển về chữ thường để so sánh không phân biệt chữ hoa và chữ thường. `filter` tạo mảng gồm những sản phẩm có tên chứa từ khóa. Khi từ khóa rỗng, mọi tên đều khớp nên cả danh sách được hiển thị.

`products` nằm ngoài component nên không được tạo lại mỗi lần render. `query` thay đổi làm tính lại bộ lọc; đổi `dark` không thay đổi đầu vào của bộ lọc nên có thể dùng kết quả cũ. Nếu sau này danh sách được nhận từ props hoặc state, cần đưa danh sách đó vào dependencies cùng với `query`.

#### Bước 3 Kiểm tra hai loại tương tác

1. Tải trang và kiểm tra có ba sản phẩm.
2. Nhập `tai`: chỉ còn Tai nghe; Console cho thấy bộ lọc được tính theo từ khóa.
3. Xóa log, nhấn Đổi giao diện: màu nền đổi nhưng bộ lọc không cần tính lại vì query giữ nguyên.
4. Xóa nội dung ô tìm kiếm: ba sản phẩm xuất hiện trở lại.

Ba sản phẩm là dữ liệu minh họa, chưa phải lý do cần tối ưu thực tế. Với phép tính nhỏ, gọi `filter` trực tiếp thường đủ rõ ràng. Với danh sách lớn, đo chi phí rồi quyết định.

Không dùng `useMemo` làm nơi lưu dữ liệu quan trọng: React có thể loại bỏ cache. Ứng dụng phải vẫn đúng nếu phép tính được chạy lại.

## 4. useCallback ghi nhớ tham chiếu hàm

### Cú pháp

```jsx
const handleAction = useCallback(() => {
  doSomething(value);
}, [value]);
```

Đây là mẫu cú pháp; `doSomething` và `value` cần được khai báo phù hợp. Khi dependencies không đổi, React trả lại tham chiếu hàm đã lưu. `useCallback` không gọi hàm thay bạn và không làm công việc bên trong hàm chạy nhanh hơn.

### Kết hợp useCallback với memo

#### Bước 1 Truyền callback xuống component con

Ở ví dụ này, nút thêm công việc là component con được bọc bằng `memo`. Cha có một bộ đếm khác để tạo render mà không thay đổi nhiệm vụ của nút. Thay nội dung `src/App.jsx` bằng:

```jsx
import { memo, useCallback, useState } from "react";

const AddButton = memo(function AddButton({ onAdd }) {
  console.log("AddButton render");
  return <button onClick={onAdd}>Thêm công việc mẫu</button>;
});

export default function App() {
  const [todos, setTodos] = useState([]);
  const [count, setCount] = useState(0);

  const handleAdd = useCallback(() => {
    const todo = { id: crypto.randomUUID(), title: "Học Hooks" };
    setTodos((items) => [...items, todo]);
  }, []);

  return (
    <main>
      <h1>Công việc</h1>
      <button onClick={() => setCount((c) => c + 1)}>Bộ đếm: {count}</button>
      <AddButton onAdd={handleAdd} />
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>
    </main>
  );
}
```

#### Bước 2 Theo dõi callback và state

`App` truyền `handleAdd` qua prop `onAdd`. `AddButton` gắn nó vào `onClick`, vì vậy công việc chỉ được thêm khi người dùng nhấn nút. `useCallback` giữ tham chiếu `handleAdd` ổn định giữa các lần cha render khi dependencies không đổi.

`handleAdd` dùng hàm cập nhật `setTodos(items => ...)`, không đọc `todos` của lần render hiện tại nên không cần đưa `todos` vào dependencies. ID được tạo lúc người dùng bấm nút, không tạo trong hàm cập nhật state. Chạy trên `localhost` hoặc HTTPS với trình duyệt hỗ trợ `crypto.randomUUID`.

#### Bước 3 Kiểm tra callback vẫn nhận state mới

1. Nhấn Thêm công việc mẫu ba lần: danh sách phải có ba công việc, dù tiêu đề giống nhau nhưng ID riêng.
2. Xóa log, tăng bộ đếm vài lần: số đếm đổi nhưng prop callback của `AddButton` vẫn ổn định.
3. Nhấn thêm một lần nữa: danh sách có bốn công việc. Hàm cập nhật nhận mảng mới nhất nên không ghi đè các công việc đã thêm.

Nếu viết `const handleAdd = () => ...` trong cha, mỗi lần cha render tạo hàm có tham chiếu mới. `memo` ở con thấy `onAdd` thay đổi. `useCallback` giúp giữ prop đó ổn định trong ví dụ này.

Không bỏ dependencies để giữ hàm ổn định bằng mọi giá: callback đọc props hoặc state nào thì phải khai báo đầy đủ, nếu không có thể giữ giá trị cũ. Cũng không cần bọc mọi event handler bằng `useCallback` khi không có lợi ích cụ thể.

## 5. Phân biệt useMemo và useCallback

| Tiêu chí                      | `useMemo`                                    | `useCallback`                                                |
| ----------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| Giá trị trả về                | Kết quả callback tính toán.                  | Chính tham chiếu hàm.                                        |
| Ví dụ                         | Danh sách lọc, tổng tiền.                    | Hàm truyền vào component được bọc `memo`.                    |
| Thời điểm thực hiện công việc | Callback tính toán chạy khi cần kết quả mới. | Công việc trong hàm chạy khi bạn hoặc component con gọi hàm. |

```text
useMemo      → ghi nhớ giá trị
useCallback  → ghi nhớ hàm
memo         → có thể bỏ qua render component theo props
```

Dependencies của cả hai được so sánh từng giá trị bằng `Object.is`. Việc quên dependency có thể gây kết quả cũ; tạo object dependency mới mỗi lần render có thể làm cache mất tác dụng.

## 6. useRef là gì?

**`useRef(initialValue)`** trả về object có thuộc tính `current`. Object này giữ nguyên danh tính giữa các lần render của cùng component; thay đổi `ref.current` không yêu cầu React render lại.

| Tình huống                                             | Công cụ phù hợp |
| ------------------------------------------------------ | --------------- |
| Dữ liệu cần hiển thị và làm giao diện đổi khi cập nhật | State.          |
| Tham chiếu DOM để focus hoặc cuộn                      | Ref.            |
| ID interval, giá trị nội bộ không phục vụ render       | Ref.            |

### Thực hành focus input

#### Bước 1 Gắn ref vào ô nhập

Mục tiêu là nhấn một nút bên ngoài để đưa con trỏ vào input. Thay nội dung `src/App.jsx` bằng:

```jsx
import { useRef, useState } from "react";

export default function App() {
  const inputRef = useRef(null);
  const [name, setName] = useState("");

  return (
    <main>
      <h1>Nhập tên</h1>
      <label htmlFor="name">Tên của bạn</label>
      <input
        id="name"
        ref={inputRef}
        value={name}
        onChange={(event) => setName(event.target.value)}
      />
      <button onClick={() => inputRef.current?.focus()}>Focus ô nhập</button>
      <p>Xin chào, {name || "bạn"}!</p>
    </main>
  );
}
```

#### Bước 2 Hiểu thời điểm ref có giá trị

Lúc khởi tạo, `inputRef.current` là `null`. Sau khi React gắn input vào DOM, thuộc tính này trỏ tới phần tử input. Nút gọi `focus()` trong event handler; dấu `?.` chỉ gọi phương thức khi tham chiếu không phải `null` hoặc `undefined`.

Tên người dùng vẫn nằm trong state `name`: mỗi lần gõ, `onChange` cập nhật state để dòng chào thay đổi. Ref phục vụ thao tác focus, còn state phục vụ nội dung giao diện.

#### Bước 3 Kiểm tra trên trình duyệt

1. Nhập tên, kiểm tra dòng chào cập nhật theo nội dung đã nhập.
2. Bấm vào vùng khác để input mất focus.
3. Nhấn Focus ô nhập rồi gõ tiếp: ký tự mới phải được nhập vào ô đó.

### Lưu dữ liệu không cần render

Ví dụ độc lập sau cho thấy cập nhật ref không tự cập nhật giao diện:

```jsx
import { useRef } from "react";

export default function App() {
  const clickCountRef = useRef(0);

  function handleClick() {
    clickCountRef.current += 1;
    console.log("Số lần bấm:", clickCountRef.current);
  }

  return <button onClick={handleClick}>Bấm rồi xem Console</button>;
}
```

Muốn hiển thị số lần bấm trên màn hình, chuyển sang state. Không đọc hoặc ghi `ref.current` trong quá trình render để tính giao diện thông thường; thao tác ref trong event handler hoặc Effect. Không dùng ref để sửa trực tiếp object vốn đang là state.

## 7. Thực hành tổng hợp và kiểm tra

Chạy từng ví dụ độc lập bằng cách thay `src/App.jsx`, giữ `src/main.jsx` của project Vite. Các ví dụ bài này không cần router; nếu đang giữ cấu hình bài 3, dùng lại điểm khởi động render `<App />`.

1. **memo:** bấm Tăng ở cha, quan sát con nhận `value={1}` không cần render lại do count của cha đổi. Thử thay `value={count}` để thấy props đổi.
2. **useMemo:** nhập `tai` để lọc Tai nghe; đổi giao diện và quan sát bộ lọc không cần tính lại vì query không đổi.
3. **useCallback:** tăng bộ đếm rồi thêm công việc; kiểm tra nút con vẫn hoạt động với callback ổn định.
4. **useRef:** chuyển focus ra ngoài input, nhấn Focus ô nhập và kiểm tra con trỏ quay vào ô.
5. **Ref và state:** chạy ví dụ Console, bấm nhiều lần và kiểm tra số tăng dù component không được yêu cầu render bởi ref.

Console trong ví dụ chỉ phục vụ quan sát khi học; bỏ các log trong phần tính toán và render sau khi thực hành. Strict Mode hoặc compiler có thể làm quan sát khác với số lần gọi dự đoán đơn giản. Dùng React DevTools Profiler để đánh giá chi phí render thực tế, không khẳng định ứng dụng nhanh hơn chỉ vì log ít đi.

## 8. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Con bọc `memo` vẫn render khi cha đổi | Kiểm tra props object, array, hàm mới; state hoặc context của con cũng có thể thay đổi. |
| Memoization trả dữ liệu cũ | Khai báo đủ dependencies được callback đọc. |
| Thay ref nhưng số trên màn hình không đổi | Dữ liệu hiển thị cần dùng state, cập nhật ref không yêu cầu render. |
| `ref.current` là `null` | DOM có thể chưa được gắn hoặc đã bị gỡ; thao tác sau khi gắn trong event handler hoặc Effect. |
| `crypto.randomUUID` không tồn tại | Dùng trình duyệt hỗ trợ trên localhost hoặc HTTPS. |

## 9. Ôn tập và bài tập thêm

### Câu hỏi ôn tập

1. Vì sao `memo` không phải Hook?
2. Object hoặc hàm mới ảnh hưởng thế nào tới so sánh props?
3. `useMemo` trả về gì, `useCallback` trả về gì?
4. Vì sao memoization không được dùng để bảo đảm tính đúng của ứng dụng?
5. Khi nào nên dùng state thay vì ref?
6. Vì sao không nên bỏ dependency mà callback đang đọc?

### Bài tập mở rộng

1. Tách `AddButton` sang file riêng rồi giữ cách bọc bằng `memo`.
2. Thêm bộ lọc cho Todo List bài 2 và giải thích liệu danh sách nhỏ có cần `useMemo` không.
3. Thêm ref vào ô nhập Todo List để focus lại sau khi thêm công việc.
4. Kết hợp `useRef` và cleanup ở bài 4 để lưu ID interval cho nút Bắt đầu và Dừng. Chặn tạo thêm interval khi đã chạy và hủy interval khi unmount.

Các ví dụ đầy đủ có `export default function App()` thay thế nhau; không dán tất cả vào một file. Các đoạn mẫu cú pháp cần được ghép vào component với biến và hàm tương ứng.

## Tài liệu tham khảo

- [React: memo](https://react.dev/reference/react/memo).
- [React: useMemo](https://react.dev/reference/react/useMemo).
- [React: useCallback](https://react.dev/reference/react/useCallback).
- [React: useRef](https://react.dev/reference/react/useRef).

[Bài 4: useEffect và useReducer](./lesson4.md) | [Bài 6: Axios và Service Layer](./lesson6.md) | [Quay về roadmap](./README.md)
