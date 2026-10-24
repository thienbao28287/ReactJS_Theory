# Bài 2: Props và State trong ReactJS

[← Quay về roadmap](./README.md)

Bài học tổng hợp nội dung Props và State trong tài liệu `ReactJS_state_props.pdf`: truyền props, sử dụng `children`, quản lý state bằng `useState` và thực hành Counter, Todo List. Các ví dụ được bổ sung để bạn có thể thực hành trong project đã tạo ở [bài 1](./lesson1.md).

## 1. Props là gì?

**Props (properties)** là dữ liệu component cha truyền xuống component con thông qua các thuộc tính JSX. Component con nhận các giá trị này trong một đối tượng props.

Props có thể chứa chuỗi, số, boolean, object, array, hàm hoặc phần tử JSX. Nhờ props, cùng một component có thể hiển thị nội dung khác nhau.

Thay nội dung `src/App.jsx` bằng ví dụ sau:

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

**Props chỉ được đọc:** component con không được sửa trực tiếp props, kể cả các thuộc tính của object hoặc phần tử của array được truyền xuống. Nếu cần yêu cầu cha thay đổi dữ liệu, con có thể gọi một hàm callback được cha truyền qua props.

## 2. Truyền và đọc props

### Truyền props từ component cha

Viết thuộc tính trên thẻ component. Dùng dấu ngoặc nhọn `{}` để truyền biểu thức JavaScript như object hoặc số:

```jsx
function Avatar({ person, size = 80 }) {
  return (
    <img
      src={person.imageUrl}
      alt={person.name}
      width={size}
      height={size}
    />
  );
}

export default function App() {
  const person = {
    name: 'Nguyễn An',
    imageUrl: '/avatar.png',
  };

  return <Avatar person={person} size={100} />;
}
```

Đặt một ảnh có tên `avatar.png` trong thư mục `public/` để chạy ví dụ. `person` là object; `size` là số. Giá trị mặc định `size = 80` được dùng khi cha không truyền `size` hoặc truyền `undefined`.

### Đọc props trong component con

Có thể đọc từ đối tượng `props`:

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

**`children`** chứa nội dung nằm giữa thẻ mở và thẻ đóng của component. Cách này phù hợp khi tạo khung bố cục dùng lại nhiều lần:

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

## 4. State và useState

**State** là dữ liệu component ghi nhớ giữa các lần render. Khi gọi hàm cập nhật state, React yêu cầu render để tính lại giao diện dựa trên dữ liệu mới.

Một biến thông thường không thay thế được state: thay đổi biến không tự yêu cầu React render và biến cục bộ được tạo lại mỗi lần component chạy.

### Cấu trúc useState

Import `useState` từ React rồi gọi bên trong function component:

```jsx
import { useState } from 'react';

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <main>
      <p>Giá trị: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Tăng</button>
    </main>
  );
}
```

`useState` trả về mảng gồm hai phần tử:

| Thành phần | Ý nghĩa |
| --- | --- |
| `count` | Giá trị state trong lần render hiện tại. |
| `setCount` | Hàm yêu cầu cập nhật state cho lần render tiếp theo. |
| `0` trong `useState(0)` | Giá trị khởi tạo của state. |

State có thể là chuỗi, số, boolean, object hoặc array. Ví dụ, ô nhập liệu dùng state chuỗi; danh sách công việc dùng state array.

### Cập nhật dựa trên giá trị trước đó

Khi giá trị mới phụ thuộc vào giá trị trước, truyền một hàm cập nhật:

```jsx
setCount(previous => previous + 1);
```

React đưa giá trị đang chờ cập nhật vào `previous` và dùng kết quả trả về làm giá trị mới. Cách này hữu ích khi có nhiều cập nhật liên tiếp.

State là một **ảnh chụp của mỗi lần render**. Gọi setter không đổi ngay biến state trong đoạn code đang chạy:

```jsx
function handleClick() {
  setCount(c => c + 1);
  console.log(count); // Vẫn là giá trị của lần render hiện tại.
}
```

Đoạn `handleClick` trên đặt trong component có khai báo `count` và `setCount`. React có thể gộp nhiều cập nhật trước khi render; không dùng `await setCount(...)` để chờ giá trị mới vì setter không trả về Promise.

### Quy tắc cần nhớ

- Gọi `useState` ở cấp cao nhất của function component hoặc custom Hook, không đặt trong điều kiện hay vòng lặp.
- Cập nhật state bằng setter, không gán trực tiếp như `count = count + 1`.
- Với object và array, tạo giá trị mới thay vì sửa trực tiếp giá trị hiện có.
- Truyền hàm xử lý sự kiện, chẳng hạn `onClick={handleClick}` hoặc `onClick={() => setCount(0)}`; không gọi setter ngay khi render bằng `onClick={setCount(0)}`.

## 5. So sánh Props và State

| Tiêu chí | Props | State |
| --- | --- | --- |
| Nguồn dữ liệu | Được component cha truyền xuống. | Được component quản lý. |
| Cách cập nhật | Component con không sửa trực tiếp. | Gọi hàm setter. |
| Vai trò | Truyền dữ liệu và cấu hình component. | Ghi nhớ dữ liệu thay đổi theo tương tác. |
| Ví dụ | Tên người dùng truyền vào `Greeting`. | Giá trị bộ đếm trong `Counter`. |

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

### Code thực hành

Thay nội dung `src/App.jsx` bằng đoạn sau:

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <section>
      <h1>Counter</h1>
      <p>Giá trị: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>
        Increment
      </button>
      <button
        onClick={() => setCount(c => Math.max(0, c - 1))}
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

`disabled={count === 0}` điều khiển khả năng tương tác của nút. `Math.max(0, c - 1)` bảo đảm kết quả không nhỏ hơn `0`.

### Kiểm tra kết quả

1. Mở ứng dụng: giá trị bằng `0`, Decrement và Reset bị khóa.
2. Nhấn Increment hai lần: giá trị bằng `2`, hai nút được bật.
3. Nhấn Decrement: giá trị bằng `1`.
4. Nhấn Reset: trở về `0`, Decrement và Reset bị khóa trở lại.

## 7. Thực hành Todo List

PDF yêu cầu xây dựng Todo List. Ví dụ dưới đây bổ sung các chức năng thêm, đánh dấu hoàn thành và xóa công việc để luyện cập nhật state array và truyền callback qua props.

### Yêu cầu

- Nhập tên công việc và thêm bằng nút **Thêm** hoặc phím Enter.
- Bỏ qua nội dung rỗng hoặc chỉ có khoảng trắng.
- Dùng checkbox để đánh dấu hoàn thành.
- Xóa từng công việc.

### Code thực hành

Thay nội dung `src/App.jsx` bằng đoạn sau:

```jsx
import { useState } from 'react';

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
  const [text, setText] = useState('');
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

    setTodos(items => [...items, newTodo]);
    setText('');
  }

  function toggleTodo(id) {
    setTodos(items => items.map(item => (
      item.id === id ? { ...item, done: !item.done } : item
    )));
  }

  function deleteTodo(id) {
    setTodos(items => items.filter(item => item.id !== id));
  }

  return (
    <main>
      <h1>Todo List</h1>
      <form onSubmit={addTodo}>
        <label htmlFor="todo-title">Tên công việc</label>
        <input
          id="todo-title"
          value={text}
          onChange={event => setText(event.target.value)}
        />
        <button type="submit">Thêm</button>
      </form>
      <ul>
        {todos.map(todo => (
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

### Giải thích các phần chính

| Phần code | Vai trò |
| --- | --- |
| `text` và `setText` | Quản lý nội dung ô nhập. |
| `todos` và `setTodos` | Quản lý danh sách công việc. |
| `value` và `onChange` | Giữ nội dung input đồng bộ với state. |
| `event.preventDefault()` | Ngăn form tải lại trang khi submit. |
| `[...items, newTodo]` | Tạo mảng mới có thêm công việc. |
| `map` và `{ ...item, done: !item.done }` | Tạo mảng mới và object mới cho công việc cần đổi trạng thái. |
| `filter` | Tạo mảng mới không chứa công việc cần xóa. |
| `key={todo.id}` | Giúp React nhận diện từng công việc khi danh sách thay đổi. |
| `todo`, `onToggle`, `onDelete` | Props truyền từ `App` xuống `TodoItem`. |

`TodoItem` gọi callback để yêu cầu cha cập nhật dữ liệu; không sửa trực tiếp `todo`. `key` được React sử dụng riêng và không được truyền vào component như một prop thông thường.

`crypto.randomUUID()` tạo ID khi thêm công việc. Chạy ví dụ trên trình duyệt hỗ trợ API này qua `localhost` của Vite hoặc HTTPS. Không tạo ID mới ngay trong mỗi lần render.

Danh sách chỉ được lưu trong state nên sẽ mất khi tải lại trang. Có thể bổ sung lưu trữ ở bài học sau.

### Kiểm tra kết quả

1. Nhập `Học props` rồi nhấn Enter: danh sách có công việc mới và ô nhập được xóa.
2. Nhập toàn dấu cách rồi nhấn Thêm: danh sách không thay đổi.
3. Thêm công việc thứ hai; đánh dấu công việc đầu tiên và kiểm tra chỉ tên của nó được gạch ngang.
4. Bỏ chọn checkbox để đưa công việc về trạng thái chưa hoàn thành.
5. Xóa một công việc và kiểm tra các công việc khác vẫn còn.

## 8. Ôn tập và bài tập thêm

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
4. Xem [video của bài thực hành 3 trong PDF](https://youtu.be/mhM5ZwYm-gM) để thực hành thêm.

Các ví dụ đầy đủ có `export default function App()` là các phương án thay thế nhau cho `src/App.jsx`; không dán tất cả vào cùng một file. Các đoạn minh họa riêng cho `Greeting`, `setCount` và `handleClick` cần được đặt vào component tương ứng.

## Tài liệu tham khảo

- Tài liệu `ReactJS_state_props.pdf` do người học cung cấp: Props, State và các bài thực hành.

[← Bài 1: Nhập môn ReactJS](./lesson1.md) | [Quay về roadmap →](./README.md)
