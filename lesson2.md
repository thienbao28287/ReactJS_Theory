# Bài 2: Props và State trong ReactJS

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn truyền dữ liệu từ component cha xuống component con bằng props, bao bọc nội dung bằng `children` và quản lý dữ liệu thay đổi bằng state. Bạn sẽ áp dụng lần lượt vào bộ đếm và danh sách công việc có chức năng thêm, hoàn thành và xóa.

### Kiến thức cần có và chuẩn bị

Hoàn thành [bài 1](./lesson1.md) để có project React với Vite và biết component, JSX. Bạn cần đọc được destructuring, spread, `map` và `filter`; các thao tác này cũng sẽ được giải thích trong ví dụ.

Mở terminal trong thư mục chứa `package.json`, chạy `npm run dev` rồi mở địa chỉ Local. Nếu chưa cài dependencies của project, chạy `npm install` trước. Giữ `src/main.jsx` render `<App />`.

Mỗi ví dụ có `export default function App()` là một nội dung hoàn chỉnh để **thay toàn bộ `src/App.jsx`**. Những đoạn chỉ có hàm hoặc câu lệnh là minh họa, dùng để thay phần tương ứng trong ví dụ, không dán nối thành nhiều `App`.

### Kết quả sau bài học

- Truyền và đọc props, dùng giá trị mặc định và `children`.
- Dùng setter để cập nhật state và xử lý sự kiện.
- Tạo mảng và object mới khi cập nhật danh sách.
- Truyền callback từ cha xuống con để con yêu cầu thay đổi dữ liệu.

## 1. Props là gì?

**Props (properties)** là dữ liệu component cha truyền xuống component con thông qua các thuộc tính JSX. Component con nhận các giá trị này trong một đối tượng props.

Props có thể chứa chuỗi, số, boolean, object, array, hàm hoặc phần tử JSX. Nhờ props, cùng một component có thể hiển thị nội dung khác nhau.

### Bước 1 Truyền tên từ cha xuống con

Thay toàn bộ nội dung `src/App.jsx` bằng ví dụ sau:

```jsx
function Greeting({ name }) {
  return <h2>Xin chào, {name}!</h2>;
}

export default function App() {
  return (
    <main>
      <Greeting name="An" />
      <Greeting name="Bảo" />
    </main>
  );
}
```

`App` là component cha; `Greeting` là component con. Mỗi lần sử dụng `Greeting`, cha truyền một giá trị `name` khác nhau.

Lưu file và kiểm tra có hai lời chào dành cho An và Bảo. Đổi `name="An"` thành tên của bạn, lưu lại và quan sát chỉ lời chào tương ứng thay đổi.

**Props chỉ được đọc:** component con không được sửa trực tiếp props, kể cả các thuộc tính của object hoặc phần tử của array được truyền xuống. Nếu cần yêu cầu cha thay đổi dữ liệu, con có thể gọi một hàm callback được cha truyền qua props.

## 2. Truyền và đọc props

### Truyền props từ component cha

Trước tiên đặt một ảnh tên `avatar.png` vào `public/`. Sau đó thay toàn bộ `src/App.jsx` bằng code bên dưới. Thuộc tính trên thẻ component truyền dữ liệu; dấu `{}` cho phép truyền object hoặc số thay vì chuỗi.

```jsx
function Avatar({ person, size = 80 }) {
  return (
    <img src={person.imageUrl} alt={person.name} width={size} height={size} />
  );
}

export default function App() {
  const person = {
    name: "Nguyễn An",
    imageUrl: "/avatar.png",
  };

  return <Avatar person={person} size={100} />;
}
```

`person` là object; `size` là số. Giá trị mặc định `size = 80` được dùng khi cha không truyền `size` hoặc truyền `undefined`.

Lưu file, kiểm tra ảnh hiển thị với kích thước `100 × 100`. Bỏ `size={100}` khỏi `<Avatar />`, lưu lại và kiểm tra kích thước về `80 × 80`. Nếu ảnh không hiện, mở `/avatar.png` trên cùng địa chỉ ứng dụng để kiểm tra tên và vị trí file.

### Đọc props trong component con

Các đoạn dưới đây minh họa hai cách viết của cùng component; chỉ giữ một định nghĩa `Greeting` khi thử trong ví dụ đầu bài. Có thể đọc từ đối tượng `props`:

```jsx
function Greeting(props) {
  return <h2>Xin chào, {props.name}!</h2>;
}
```

Hoặc dùng **destructuring** để lấy trực tiếp thuộc tính cần dùng:

```jsx
function Greeting({ name }) {
  return <h2>Xin chào, {name}!</h2>;
}
```

Hai cách trên có cùng kết quả. Các ví dụ tiếp theo dùng destructuring để phần tham số thể hiện rõ component nhận những props nào.

## 3. Sử dụng children

**`children`** chứa nội dung nằm giữa thẻ mở và thẻ đóng của component. Cách này phù hợp khi tạo khung bố cục dùng lại nhiều lần. Thay toàn bộ `src/App.jsx` bằng ví dụ sau:

```jsx
function Wrapper({ children }) {
  return <section className="wrapper">{children}</section>;
}

export default function App() {
  return (
    <Wrapper>
      <h1>Học ReactJS</h1>
      <p>Truyền nội dung qua children.</p>
    </Wrapper>
  );
}
```

`Wrapper` nhận `<h1>` và `<p>` qua prop `children`, sau đó hiển thị chúng tại vị trí `{children}`. Bạn cũng có thể đọc giá trị này bằng `props.children` nếu component nhận tham số `props`.

Lưu file và kiểm tra tiêu đề Học ReactJS cùng đoạn văn bên trong thẻ section. Thêm một đoạn `<p>` giữa hai thẻ `Wrapper`: nội dung mới cũng xuất hiện tại vị trí `{children}`.

## 4. State và useState

**State** là dữ liệu component ghi nhớ giữa các lần render. Khi gọi hàm cập nhật state, React yêu cầu render để tính lại giao diện dựa trên dữ liệu mới.

Một biến thông thường không thay thế được state: thay đổi biến không tự yêu cầu React render và biến cục bộ được tạo lại mỗi lần component chạy.

### Cấu trúc useState

Thay toàn bộ `src/App.jsx` bằng ví dụ sau. `useState` là một **Hook**, tức hàm cung cấp khả năng của React cho function component; ở đây nó giúp component ghi nhớ số đếm.

```jsx
import { useState } from "react";

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <main>
      <p>Giá trị: {count}</p>
      <button onClick={() => setCount((c) => c + 1)}>Tăng</button>
    </main>
  );
}
```

Lưu file, nhấn Tăng và kiểm tra số đếm đổi từ `0` sang `1`. Trong `onClick`, hàm mũi tên là **event handler**, tức hàm React gọi khi sự kiện click xảy ra.

`useState` trả về mảng gồm hai phần tử:

| Thành phần              | Ý nghĩa                                              |
| ----------------------- | ---------------------------------------------------- |
| `count`                 | Giá trị state trong lần render hiện tại.             |
| `setCount`              | Hàm yêu cầu cập nhật state cho lần render tiếp theo. |
| `0` trong `useState(0)` | Giá trị khởi tạo của state.                          |

State có thể là chuỗi, số, boolean, object hoặc array. Ví dụ, ô nhập liệu dùng state chuỗi; danh sách công việc dùng state array.

### Cập nhật dựa trên giá trị trước đó

Khi giá trị mới phụ thuộc vào giá trị trước, truyền một hàm cập nhật:

```jsx
setCount((previous) => previous + 1);
```

React đưa giá trị đang chờ cập nhật vào `previous` và dùng kết quả trả về làm giá trị mới. Cách này hữu ích khi có nhiều cập nhật liên tiếp.

State là một **ảnh chụp của mỗi lần render**. Gọi setter không đổi ngay biến state trong đoạn code đang chạy:

```jsx
function handleClick() {
  setCount((c) => c + 1);
  console.log(count); // Vẫn là giá trị của lần render hiện tại.
}
```

Để thử đoạn minh họa này, đặt `handleClick` bên trong `App` ở ví dụ vừa chạy, ngay sau khai báo state và trước `return`. Đổi thuộc tính của nút thành `onClick={handleClick}`, mở Console trong DevTools rồi bấm nút. Số trên giao diện tăng nhưng log trong lần bấm đó vẫn là số của lần render trước. React có thể gộp nhiều cập nhật trước khi render; không dùng `await setCount(...)` để chờ giá trị mới vì setter không trả về Promise.

### Quy tắc cần nhớ

- Gọi `useState` ở cấp cao nhất của function component hoặc custom Hook, không đặt trong điều kiện hay vòng lặp.
- Cập nhật state bằng setter, không gán trực tiếp như `count = count + 1`.
- Với object và array, tạo giá trị mới thay vì sửa trực tiếp giá trị hiện có.
- Truyền hàm xử lý sự kiện, chẳng hạn `onClick={handleClick}` hoặc `onClick={() => setCount(0)}`; không gọi setter ngay khi render bằng `onClick={setCount(0)}`.

## 5. So sánh Props và State

| Tiêu chí      | Props                                 | State                                    |
| ------------- | ------------------------------------- | ---------------------------------------- |
| Nguồn dữ liệu | Được component cha truyền xuống.      | Được component quản lý.                  |
| Cách cập nhật | Component con không sửa trực tiếp.    | Gọi hàm setter.                          |
| Vai trò       | Truyền dữ liệu và cấu hình component. | Ghi nhớ dữ liệu thay đổi theo tương tác. |
| Ví dụ         | Tên người dùng truyền vào `Greeting`. | Giá trị bộ đếm trong `Counter`.          |

State của component cha có thể được truyền xuống component con dưới dạng props:

```text
Component cha quản lý state
  → Truyền giá trị và callback qua props
  → Component con hiển thị và gọi callback khi tương tác
  → Cha cập nhật state, React tính lại giao diện
```

## 6. Thực hành Counter

### Yêu cầu

- Giá trị ban đầu bằng `0`.
- **Increment** tăng giá trị lên một đơn vị.
- **Decrement** giảm giá trị một đơn vị; không cho phép giá trị âm.
- **Reset** đưa giá trị về `0`.
- Khi giá trị bằng `0`, nút **Decrement** và **Reset** bị vô hiệu hóa.

### Bước 1 Tạo bộ đếm

Thay nội dung `src/App.jsx` bằng đoạn sau:

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <section>
      <h1>Counter</h1>
      <p>Giá trị: {count}</p>
      <button onClick={() => setCount((c) => c + 1)}>Increment</button>
      <button
        onClick={() => setCount((c) => Math.max(0, c - 1))}
        disabled={count === 0}
      >
        Decrement
      </button>
      <button onClick={() => setCount(0)} disabled={count === 0}>
        Reset
      </button>
    </section>
  );
}

export default function App() {
  return <Counter />;
}
```

### Bước 2 Hiểu cách cập nhật và khóa nút

Khi nhấn Increment, setter nhận hàm tính giá trị mới từ giá trị trước. Khi React render với số mới, biểu thức `count === 0` cũng được tính lại để bật hoặc khóa nút.

`disabled={count === 0}` điều khiển khả năng tương tác của nút. `Math.max(0, c - 1)` bảo đảm kết quả không nhỏ hơn `0`.

### Kiểm tra kết quả

1. Mở ứng dụng: giá trị bằng `0`, Decrement và Reset bị khóa.
2. Nhấn Increment hai lần: giá trị bằng `2`, hai nút được bật.
3. Nhấn Decrement: giá trị bằng `1`.
4. Nhấn Reset: trở về `0`, Decrement và Reset bị khóa trở lại.

## 7. Thực hành Todo List

Bạn sẽ tạo Todo List gồm ô nhập và danh sách công việc. `App` giữ dữ liệu chung; `TodoItem` nhận một công việc và các callback để hiển thị, đổi trạng thái hoặc yêu cầu xóa. **Callback** là hàm được truyền cho phần khác gọi khi cần.

### Yêu cầu

- Nhập tên công việc và thêm bằng nút **Thêm** hoặc phím Enter.
- Bỏ qua nội dung rỗng hoặc chỉ có khoảng trắng.
- Dùng checkbox để đánh dấu hoàn thành.
- Xóa từng công việc.

### Bước 1 Tạo state và giao diện danh sách

Thay nội dung `src/App.jsx` bằng đoạn sau:

```jsx
import { useState } from "react";

function TodoItem({ todo, onToggle, onDelete }) {
  return (
    <li>
      <label>
        <input
          type="checkbox"
          checked={todo.done}
          onChange={() => onToggle(todo.id)}
        />
        {todo.done ? <s>{todo.title}</s> : todo.title}
      </label>
      <button onClick={() => onDelete(todo.id)}>Xóa</button>
    </li>
  );
}

export default function App() {
  const [text, setText] = useState("");
  const [todos, setTodos] = useState([]);

  function addTodo(event) {
    event.preventDefault();
    const title = text.trim();
    if (!title) return;

    const newTodo = {
      id: crypto.randomUUID(),
      title,
      done: false,
    };

    setTodos((items) => [...items, newTodo]);
    setText("");
  }

  function toggleTodo(id) {
    setTodos((items) =>
      items.map((item) =>
        item.id === id ? { ...item, done: !item.done } : item,
      ),
    );
  }

  function deleteTodo(id) {
    setTodos((items) => items.filter((item) => item.id !== id));
  }

  return (
    <main>
      <h1>Todo List</h1>
      <form onSubmit={addTodo}>
        <label htmlFor="todo-title">Tên công việc</label>
        <input
          id="todo-title"
          value={text}
          onChange={(event) => setText(event.target.value)}
        />
        <button type="submit">Thêm</button>
      </form>
      <ul>
        {todos.map((todo) => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
          />
        ))}
      </ul>
    </main>
  );
}
```

### Bước 2 Theo dõi thao tác thêm công việc

Gõ vào input làm `onChange` cập nhật `text`. Đây là input được điều khiển bởi React: nội dung hiển thị lấy từ `value={text}`. Nhấn Thêm hoặc Enter khiến form gọi `addTodo`; `preventDefault` ngăn tải lại trang, `trim` loại khoảng trắng và lệnh `if` bỏ qua tên rỗng.

Hàm tạo object có ID, tiêu đề và trạng thái chưa hoàn thành. `[...items, newTodo]` sao chép các phần tử cũ vào mảng mới rồi thêm công việc. Cuối cùng, `setText("")` xóa nội dung input để nhập việc tiếp theo.

### Bước 3 Theo dõi thao tác hoàn thành và xóa

`map` trong JSX biến từng object thành một `TodoItem`. Khi bấm checkbox, con gọi `onToggle(todo.id)` để cha biết cần đổi công việc nào. Cha dùng `map` tạo mảng mới; riêng công việc khớp ID được sao chép thành object mới với `done` đảo ngược.

Khi nhấn Xóa, callback gửi ID về cha. `filter` giữ lại các công việc có ID khác, tạo danh sách mới mà không sửa mảng cũ. Cả hai thao tác đều đi qua setter nên React có thể cập nhật giao diện.

### Tra cứu các phần code chính

| Phần code                                | Vai trò                                                      |
| ---------------------------------------- | ------------------------------------------------------------ |
| `text` và `setText`                      | Quản lý nội dung ô nhập.                                     |
| `todos` và `setTodos`                    | Quản lý danh sách công việc.                                 |
| `value` và `onChange`                    | Giữ nội dung input đồng bộ với state.                        |
| `event.preventDefault()`                 | Ngăn form tải lại trang khi submit.                          |
| `[...items, newTodo]`                    | Tạo mảng mới có thêm công việc.                              |
| `map` và `{ ...item, done: !item.done }` | Tạo mảng mới và object mới cho công việc cần đổi trạng thái. |
| `filter`                                 | Tạo mảng mới không chứa công việc cần xóa.                   |
| `key={todo.id}`                          | Giúp React nhận diện từng công việc khi danh sách thay đổi.  |
| `todo`, `onToggle`, `onDelete`           | Props truyền từ `App` xuống `TodoItem`.                      |

`TodoItem` gọi callback để yêu cầu cha cập nhật dữ liệu; không sửa trực tiếp `todo`. `key` được React sử dụng riêng và không được truyền vào component như một prop thông thường.

`crypto.randomUUID()` tạo ID khi thêm công việc. Chạy ví dụ trên trình duyệt hỗ trợ API này qua `localhost` của Vite hoặc HTTPS. Không tạo ID mới ngay trong mỗi lần render.

Danh sách chỉ được lưu trong state nên sẽ mất khi tải lại trang. Có thể bổ sung lưu trữ ở bài học sau.

### Kiểm tra kết quả

1. Nhập `Học props` rồi nhấn Enter: danh sách có công việc mới và ô nhập được xóa.
2. Nhập toàn dấu cách rồi nhấn Thêm: danh sách không thay đổi.
3. Thêm công việc thứ hai; đánh dấu công việc đầu tiên và kiểm tra chỉ tên của nó được gạch ngang.
4. Bỏ chọn checkbox để đưa công việc về trạng thái chưa hoàn thành.
5. Xóa một công việc và kiểm tra các công việc khác vẫn còn.

## 8. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Số tăng liên tục hoặc báo quá nhiều render | Truyền hàm cho `onClick`, không gọi setter ngay khi render. |
| Thêm công việc làm trang tải lại | Giữ `event.preventDefault()` trong hàm submit. |
| Sửa array nhưng giao diện không cập nhật đúng | Dùng setter với mảng mới, không sửa trực tiếp bằng `push` hoặc `splice`. |
| Cảnh báo thiếu key | Gắn `key={todo.id}` vào phần tử được trả về trực tiếp từ `map`. |
| Mất danh sách khi tải lại trang | Đây là state trong bộ nhớ; ví dụ chưa lưu dữ liệu lâu dài. |

## 9. Ôn tập và bài tập thêm

### Câu hỏi ôn tập

1. Component cha truyền props xuống component con như thế nào?
2. `children` chứa nội dung ở vị trí nào trong JSX?
3. Hai phần tử của mảng do `useState` trả về có ý nghĩa gì?
4. Vì sao gọi setter không đổi ngay biến state trong đoạn code đang chạy?
5. Khi nào nên dùng hàm cập nhật như `setCount(c => c + 1)`?
6. Vì sao không nên dùng `todos.push(...)` để sửa trực tiếp state?

### Bài tập mở rộng

1. Tách `TodoItem` sang file `src/TodoItem.jsx`, export rồi import vào `App.jsx`.
2. Hiển thị số công việc chưa hoàn thành bằng `todos.filter(todo => !todo.done).length`.
3. Hiển thị thông báo khi danh sách chưa có công việc nào.

Các ví dụ đầy đủ có `export default function App()` là các phương án thay thế nhau cho `src/App.jsx`; không dán tất cả vào cùng một file. Các đoạn minh họa riêng cho `Greeting`, `setCount` và `handleClick` cần được đặt vào component tương ứng.

## Tài liệu tham khảo

- [React: Truyền props](https://react.dev/learn/passing-props-to-a-component).
- [React: useState](https://react.dev/reference/react/useState).
- [React: Cập nhật array trong state](https://react.dev/learn/updating-arrays-in-state).


[Bài 1: Nhập môn ReactJS](./lesson1.md) | [Bài 3: React Router →](./lesson3.md) | [Quay về roadmap](./README.md)
