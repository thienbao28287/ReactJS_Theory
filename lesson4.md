# Bài 4: useEffect và useReducer trong ReactJS

[Quay về roadmap](./README.md)

Trong bài này, bạn sẽ dùng `useEffect` để cập nhật tiêu đề trang, tạo đồng hồ và tải danh sách người dùng. Sau đó, bạn sẽ dùng `useReducer` để tổ chức logic của bộ đếm có nhiều hành động. Mỗi phần gồm cách thực hiện, giải thích luồng chạy và kết quả cần kiểm tra.

### Kiến thức cần có và chuẩn bị

Bạn cần biết cách tạo component, xử lý sự kiện và dùng `useState` trong [bài 2](./lesson2.md). Dùng project React với Vite đã tạo ở bài 1, mở terminal tại thư mục có `package.json`, rồi chạy:

```bash
npm install
npm run dev
```

Mở địa chỉ Local do terminal hiển thị. Giữ server chạy trong lúc thực hành; khi lưu code, Vite sẽ cập nhật trang. Nếu project đã cài dependencies, có thể bắt đầu bằng `npm run dev`.

Các ví dụ hoàn chỉnh trong bài thay thế nhau trong `src/App.jsx`. Với mỗi ví dụ, hãy thay toàn bộ nội dung file, lưu và kiểm tra kết quả trước khi chuyển sang phần tiếp theo. Giữ `src/main.jsx` render `<App />`; nếu đã thiết lập router ở đó trong bài trước, đưa điểm khởi động về render `<App />` cho bài thực hành này.

### Kết quả sau bài học

- Chọn được khi nào cần Effect và khai báo dependencies đúng với dữ liệu sử dụng.
- Dọn dẹp interval, sự kiện và yêu cầu mạng khi component không còn dùng chúng.
- Hiển thị trạng thái đang tải, dữ liệu hoặc lỗi khi lấy dữ liệu.
- Viết reducer nhận action và trả về state mới mà không sửa state cũ.

## 1. Tổng quan về Hooks

**Hooks** là các hàm như `useState`, `useEffect` và `useReducer`, cho phép function component sử dụng các khả năng của React. Những Hook trong bài được import trực tiếp từ `react`, không cần cài thêm package.

| Hook         | Vai trò                                                                 |
| ------------ | ----------------------------------------------------------------------- |
| `useState`   | Quản lý state, đã học trong bài 2.                                      |
| `useEffect`  | Đồng bộ với hệ thống bên ngoài như timer, sự kiện trình duyệt hoặc API. |
| `useReducer` | Quản lý state bằng logic cập nhật tập trung trong một reducer.          |

Một **custom Hook** là hàm tự viết có tên bắt đầu bằng `use` để tái sử dụng logic dùng Hook; bài này thực hành trực tiếp trong component. Gọi các Hook này ở cấp cao nhất của function component hoặc custom Hook. Không gọi trong vòng lặp, điều kiện hay hàm xử lý sự kiện. Đặt Hook trước những lệnh `return` có điều kiện để thứ tự gọi ổn định giữa các lần render.

## 2. useEffect là gì?

Trong khi render tính toán JSX, **Effect** thực hiện việc đồng bộ với thứ nằm ngoài React sau khi giao diện được commit. Ví dụ: kết nối sự kiện trình duyệt, tạo interval hoặc lấy dữ liệu qua mạng.

Trong bài này, **mount** nghĩa là component được đưa vào cây giao diện; **unmount** là component bị gỡ khỏi cây. **Commit** là bước React áp dụng kết quả render lên DOM. Hiểu các thời điểm này giúp bạn xác định lúc bắt đầu và lúc kết thúc một công việc như chạy đồng hồ.

Không phải mọi đoạn code ngoài JSX đều cần Effect. Tính tổng từ dữ liệu hiện có có thể làm ngay khi render; xử lý một lần bấm nút thường đặt trong event handler.

### Cấu trúc cơ bản

```jsx
useEffect(() => {
  // Thiết lập việc đồng bộ.

  return () => {
    // Dọn dẹp tài nguyên do lần thiết lập này tạo ra, nếu có.
  };
}, [dependency]);
```

Đây là mẫu cú pháp, không phải component hoàn chỉnh. `dependency` đại diện cho giá trị phản ứng được Effect sử dụng. Danh sách dependencies cần chứa các props, state và giá trị hoặc hàm khai báo trong component mà Effect đọc.

### Ba cách truyền dependencies

| Cách viết                   | Khi nào Effect chạy?                                                  |
| --------------------------- | --------------------------------------------------------------------- |
| `useEffect(setup)`          | Sau mỗi lần commit của component.                                     |
| `useEffect(setup, [])`      | Sau lần mount; không chạy lại do props hoặc state đổi.                |
| `useEffect(setup, [count])` | Sau lần mount và sau commit khi `count` đổi theo so sánh `Object.is`. |

Trong Strict Mode ở môi trường phát triển, React có thể chạy thêm chu kỳ **setup → cleanup → setup** khi mount để kiểm tra khả năng dọn dẹp. Vì vậy, `[]` không có nghĩa là cam kết chạy đúng một lần trong mọi hoàn cảnh; component được mount lại cũng tạo Effect mới.

## 3. Thực hành đồng bộ tiêu đề trang

### Bước 1 Tạo bộ đếm và Effect

Mục tiêu là khi nhấn Tăng, cả số trên trang và tiêu đề tab trình duyệt đều cập nhật. Mở `src/App.jsx`, thay toàn bộ nội dung bằng code dưới đây rồi lưu:

```jsx
import { useEffect, useState } from "react";

export default function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const previousTitle = document.title;
    document.title = `Bộ đếm: ${count}`;

    return () => {
      document.title = previousTitle;
    };
  }, [count]);

  return (
    <main>
      <h1>Bộ đếm: {count}</h1>
      <button onClick={() => setCount((c) => c + 1)}>Tăng</button>
    </main>
  );
}
```

### Bước 2 Hiểu luồng cập nhật

Khi mở trang, `count` bằng `0`. React hiển thị JSX rồi chạy Effect để đặt tiêu đề tab thành `Bộ đếm: 0`. `document.title` là thuộc tính của trình duyệt, nên việc đồng bộ nó với state được đặt trong Effect.

Khi bạn nhấn Tăng, setter yêu cầu render với `count` mới. React nhận thấy dependency `count` đổi, chạy cleanup của lần trước để khôi phục tiêu đề cũ, rồi chạy setup để ghi tiêu đề theo giá trị mới. Nếu component bị gỡ, cleanup khôi phục tiêu đề đã có trước khi component quản lý nó.

### Kiểm tra kết quả

1. Mở ứng dụng và xem tiêu đề tab trình duyệt có giá trị `0`.
2. Nhấn Tăng: giá trị trên trang và tiêu đề tab cùng thay đổi.
3. Không bỏ `count` khỏi dependencies để ngăn Effect chạy; làm như vậy khiến tiêu đề không còn đồng bộ.

## 4. Cleanup với interval và sự kiện

**Cleanup** chạy trước khi Effect thiết lập lại do dependencies đổi và khi component unmount. Nó cần đảo ngược công việc đã thiết lập, chẳng hạn `clearInterval` cho `setInterval`, `removeEventListener` cho `addEventListener`.

### Bước 1 Tạo đồng hồ có thể ẩn và hiện

Mục tiêu là chỉ chạy interval khi đồng hồ đang hiển thị. Thay nội dung `src/App.jsx` bằng ví dụ sau và lưu:

```jsx
import { useEffect, useState } from "react";

function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setSeconds((value) => value + 1);
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return <p>Đã chạy: {seconds} giây</p>;
}

export default function App() {
  const [visible, setVisible] = useState(true);

  return (
    <main>
      <button onClick={() => setVisible((value) => !value)}>
        {visible ? "Ẩn đồng hồ" : "Hiện đồng hồ"}
      </button>
      {visible && <Timer />}
    </main>
  );
}
```

### Bước 2 Theo dõi tài nguyên của component

`App` quản lý việc hiện hoặc ẩn bằng state `visible`. Khi `visible` là `true`, React tạo `Timer`; Effect của `Timer` đăng ký interval và giữ ID trong `intervalId`. Mỗi khoảng 1000 mili giây, callback yêu cầu tăng số đếm.

Hàm cập nhật `setSeconds(value => value + 1)` đọc giá trị đang chờ cập nhật thay vì giữ giá trị `seconds` của lần render đầu. Effect này không đọc `seconds` nên không cần thêm nó vào dependencies.

Khi ẩn, `Timer` unmount và interval bị hủy. Khi hiện lại, một `Timer` mới bắt đầu từ `0`. Interval chỉ mô phỏng số giây; trình duyệt có thể trì hoãn timer nên không dùng cách đếm tick này để đo thời gian chính xác.

### Bước 3 Kiểm tra việc dọn dẹp

1. Đợi khoảng ba giây và kiểm tra số đếm tăng.
2. Nhấn Ẩn đồng hồ, đợi thêm vài giây rồi nhấn Hiện đồng hồ.
3. Kiểm tra đồng hồ bắt đầu lại từ `0` và tăng theo từng tick, thay vì tiếp tục giá trị cũ.
4. Đọc dòng `return () => clearInterval(intervalId)`: đây là nơi hủy interval của lần setup đó. Đừng xóa cleanup để xử lý hiện tượng chạy thêm lần trong Strict Mode.

### Áp dụng cùng nguyên tắc cho sự kiện

Để thử sự kiện trình duyệt, giữ ví dụ đồng hồ và bổ sung Effect dưới đây vào `Timer`, trước lệnh `return`. `useEffect` đã được import ở đầu file nên không cần import thêm:

```jsx
useEffect(() => {
  function handleResize() {
    console.log("Chiều rộng:", window.innerWidth);
  }

  window.addEventListener("resize", handleResize);
  return () => window.removeEventListener("resize", handleResize);
}, []);
```

Lưu file, mở Console và kéo thay đổi chiều rộng cửa sổ: bạn sẽ thấy log chiều rộng. Ẩn đồng hồ rồi tiếp tục kéo: listener của `Timer` đã bị gỡ nên không còn ghi log mới. Hàm truyền vào `removeEventListener` phải khớp với hàm đã đăng ký. Không đăng ký một hàm mới ở mỗi lần render ngoài Effect.

## 5. Lấy dữ liệu bằng useEffect

Một màn hình lấy dữ liệu cần phân biệt ba tình huống: đang chờ phản hồi, đã nhận dữ liệu và gặp lỗi. Bạn sẽ tạo một file JSON được Vite phục vụ qua HTTP, sau đó dùng `fetch` để đọc nó khi component xuất hiện.

### Bước 1 Chuẩn bị dữ liệu

Tại thư mục gốc project, tạo thư mục `public` ngang cấp với `src` nếu chưa có. Tạo file `users.json` bên trong `public`, thành đường dẫn `public/users.json`. Nếu đã có file từ bài 3, thay nội dung bằng:

```json
[
  { "id": 1, "name": "Nguyễn An" },
  { "id": 2, "name": "Trần Bình" }
]
```

### Bước 2 Tải dữ liệu và hiển thị trạng thái

Thay nội dung `src/App.jsx` bằng:

```jsx
import { useEffect, useState } from "react";

export default function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    let active = true;

    async function loadUsers() {
      setLoading(true);
      setError("");

      try {
        const response = await fetch("/users.json", {
          signal: controller.signal,
        });
        if (!response.ok) {
          throw new Error(`Không tải được dữ liệu: ${response.status}`);
        }
        const data = await response.json();
        if (!Array.isArray(data)) {
          throw new Error("Dữ liệu phải là một danh sách.");
        }
        if (active) setUsers(data);
      } catch (err) {
        if (active) {
          setError(err instanceof Error ? err.message : "Đã xảy ra lỗi.");
        }
      } finally {
        if (active) setLoading(false);
      }
    }

    loadUsers();
    return () => {
      active = false;
      controller.abort();
    };
  }, []);

  if (loading) return <p role="status">Đang tải...</p>;
  if (error) return <p role="alert">{error}</p>;

  return (
    <main>
      <h1>Người dùng</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </main>
  );
}
```

### Bước 3 Đọc luồng xử lý

Ban đầu, `loading` bằng `true` nên màn hình hiển thị Đang tải. Effect gọi `loadUsers`, gửi yêu cầu đến `/users.json`, kiểm tra phản hồi rồi chuyển JSON thành dữ liệu JavaScript. Trong cấu trúc Vite đang dùng, `/users.json` trỏ tới file `public/users.json`, không phải một file trong `src`.

Nếu đọc dữ liệu thành công, `setUsers` lưu danh sách. Nếu có lỗi, `setError` lưu thông báo. Khối `finally` kết thúc trạng thái tải; lần render tiếp theo chọn hiển thị thông báo lỗi hoặc danh sách theo state hiện tại.

Callback của `useEffect` không được khai báo `async` vì React cần nhận hàm cleanup hoặc `undefined`, không phải Promise. Hàm bất đồng bộ được khai báo bên trong Effect rồi gọi.

Cleanup hủy yêu cầu đang chạy và đánh dấu kết quả của lần thiết lập cũ không còn được dùng. `response.ok` cần được kiểm tra vì phản hồi HTTP lỗi không tự khiến `fetch` ném exception. Ví dụ giả định mỗi phần tử có `id` duy nhất và `name` là chuỗi; API thật cần kiểm tra dữ liệu theo cấu trúc đã thỏa thuận.

Ở [bài 3](./lesson3.md), Data Router có loader để tải dữ liệu theo route. Với màn hình đã dùng loader, thường không cần fetch lại cùng dữ liệu trong Effect.

### Bước 4 Kiểm tra thành công và lỗi

1. Mở trang, kiểm tra danh sách có Nguyễn An và Trần Bình.
2. Để thấy trạng thái tải, mở DevTools, chọn Network và bật chế độ mạng chậm rồi tải lại trang.
3. Tạm đổi nội dung `public/users.json` thành `{}` và tải lại trang. Bạn cần thấy thông báo Dữ liệu phải là một danh sách.
4. Khôi phục mảng JSON ban đầu, tải lại và kiểm tra danh sách xuất hiện.

Nếu không nhận được JSON, thử mở `/users.json` trên cùng địa chỉ Local của ứng dụng và kiểm tra vị trí file. URL phải trả nội dung JSON, không phải trang HTML.

### Lỗi dependencies thường gặp

- Effect cập nhật chính state trong dependencies sau mỗi lần chạy có thể tạo vòng lặp.
- Object hoặc hàm tạo mới trong thân component có tham chiếu mới mỗi lần render, có thể làm Effect chạy lại.
- Không tắt cảnh báo dependencies chỉ để ép Effect chạy ít hơn; hãy xem lại dữ liệu cần đồng bộ và vị trí tạo object hoặc hàm.
- Dữ liệu suy ra như `fullName` từ `firstName` và `lastName` thường tính trực tiếp khi render, không cần một Effect đặt state khác.

## 6. useReducer là gì?

**`useReducer`** quản lý state bằng một hàm reducer. Component gửi action qua `dispatch`; reducer nhận state hiện tại và action, sau đó trả về state tiếp theo.

```text
Người dùng tương tác
  → dispatch(action)
  → reducer(state, action)
  → trả về state tiếp theo
  → React render với state mới
```

### Cấu trúc

```jsx
const [state, dispatch] = useReducer(reducer, initialState);
```

| Thành phần               | Vai trò                                |
| ------------------------ | -------------------------------------- |
| `state`                  | Giá trị state của lần render hiện tại. |
| `dispatch(action)`       | Gửi yêu cầu cập nhật tới reducer.      |
| `reducer(state, action)` | Tính và trả về state tiếp theo.        |
| `initialState`           | State ban đầu trong cách gọi này.      |

Action thường được viết thành object có `type` và dữ liệu đi kèm như `payload`. Đây là quy ước giúp code dễ đọc; React không bắt buộc action phải có cấu trúc đó.

Reducer phải là **hàm thuần**: không sửa state đầu vào, không gọi API, không tạo timer và không thực hiện tác động bên ngoài. Nếu cần ID ngẫu nhiên hoặc thời điểm hiện tại, tạo trong event handler rồi gửi vào action.

## 7. Thực hành Counter bằng useReducer

### Bước 1 Xác định state và hành động

Bộ đếm cần lưu số hiện tại `count` và bước nhảy `step`. Người dùng có bốn hành động: tăng, giảm, đổi bước nhảy và đặt lại. Ta gom quy tắc cập nhật của cả bốn hành động vào một reducer để giao diện chỉ cần gửi action.

### Bước 2 Viết reducer và kết nối giao diện

Thay toàn bộ nội dung `src/App.jsx` bằng:

```jsx
import { useReducer } from "react";

const initialState = { count: 0, step: 1 };

function reducer(state, action) {
  switch (action.type) {
    case "increment":
      return { ...state, count: state.count + state.step };
    case "decrement":
      return { ...state, count: Math.max(0, state.count - state.step) };
    case "setStep":
      return { ...state, step: action.payload };
    case "reset":
      return initialState;
    default:
      throw new Error(`Action không được hỗ trợ: ${action.type}`);
  }
}

export default function App() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <main>
      <h1>Counter: {state.count}</h1>
      <label>
        Bước nhảy
        <select
          value={state.step}
          onChange={(event) =>
            dispatch({
              type: "setStep",
              payload: Number(event.target.value),
            })
          }
        >
          <option value={1}>1</option>
          <option value={5}>5</option>
          <option value={10}>10</option>
        </select>
      </label>
      <button onClick={() => dispatch({ type: "increment" })}>Tăng</button>
      <button
        onClick={() => dispatch({ type: "decrement" })}
        disabled={state.count === 0}
      >
        Giảm
      </button>
      <button onClick={() => dispatch({ type: "reset" })}>Đặt lại</button>
    </main>
  );
}
```

### Bước 3 Theo dõi một action từ giao diện đến state

Khi chọn bước nhảy `5`, giá trị từ thẻ `select` là chuỗi. `Number(event.target.value)` chuyển nó thành số rồi gửi action `{ type: "setStep", payload: 5 }`. Reducer đi vào nhánh `setStep` và trả về object mới có `step` bằng `5`.

Khi nhấn Tăng, `dispatch({ type: "increment" })` gửi tên hành động. Reducer lấy `count` cộng `step` từ state hiện tại rồi trả về kết quả. React dùng kết quả đó để render lại số đếm.

Spread `...state` giữ các trường còn lại khi cập nhật. Nếu chỉ trả về `{ count: ... }`, bạn sẽ làm mất `step`. Nhánh giảm dùng `Math.max` để không có số âm; nhánh reset đưa cả bộ đếm về `0` và bước nhảy về `1`.

### Kiểm tra kết quả

1. Ban đầu: bộ đếm bằng `0`, bước nhảy bằng `1`.
2. Chọn bước nhảy `5`, nhấn Tăng hai lần: bộ đếm bằng `10`.
3. Nhấn Giảm: bộ đếm bằng `5`; tiếp tục giảm và kiểm tra không có số âm.
4. Nhấn Đặt lại: bộ đếm bằng `0`, bước nhảy bằng `1`.

`dispatch` yêu cầu cập nhật cho lần render tiếp theo; đọc `state` ngay sau dispatch vẫn nhận ảnh chụp của lần render hiện tại. Trong Strict Mode khi phát triển, React có thể gọi reducer thêm lần để kiểm tra tính thuần; reducer đúng không tạo tác động phụ dù được gọi lại.

## 8. Chọn useState hay useReducer

| Tình huống                                           | Lựa chọn thường phù hợp                                      |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| Một ô nhập, cờ bật tắt hoặc state ít hành động       | `useState`.                                                  |
| Nhiều hành động cùng cập nhật state liên quan        | `useReducer`.                                                |
| Logic chuyển trạng thái dài, cần tách khỏi giao diện | `useReducer`.                                                |
| Tải dữ liệu hoặc đăng ký sự kiện bên ngoài           | Effect hoặc cơ chế dữ liệu phù hợp; không làm trong reducer. |

`useReducer` không tự biến state thành toàn cục và không tự thay thế toàn bộ khả năng của Redux. Chọn dựa trên cách tổ chức logic, không chỉ vì state là object.

## 9. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Đồng hồ tăng nhanh hơn dự kiến sau khi hiện lại | Mỗi lần setup cần trả cleanup hủy đúng interval. |
| Effect liên tục gọi lại | Kiểm tra state được cập nhật và dependencies, nhất là object hoặc hàm tạo mới. |
| Effect chạy thêm lúc phát triển | Kiểm tra Strict Mode và cleanup trước khi coi đây là lỗi. |
| Reducer làm mất một trường state | Trả object mới có đủ trường, dùng spread khi cập nhật một phần. |
| Log state sau dispatch vẫn là giá trị cũ | State thuộc lần render hiện tại; quan sát giao diện sau lần render tiếp theo. |

## 10. Ôn tập và bài tập thêm

### Câu hỏi ôn tập

1. `useEffect` khác một hàm xử lý click ở điểm nào?
2. Không truyền dependencies khác truyền `[]` như thế nào?
3. Cleanup chạy ở những thời điểm nào?
4. Vì sao interval dùng hàm cập nhật state?
5. Vì sao callback của Effect không nên là hàm `async`?
6. Reducer nhận gì và trả về gì? Vì sao reducer phải thuần?

### Bài tập mở rộng

1. Thêm nút bật tắt đồng hồ và kiểm tra interval được dọn dẹp khi ẩn.
2. Đổi nguồn JSON thành dữ liệu không hợp lệ để kiểm tra thông báo lỗi, rồi khôi phục file.
3. Chuyển Todo List của bài 2 sang `useReducer` với action thêm, xóa và đổi trạng thái hoàn thành.
4. Tạo ID công việc trong event handler, truyền vào action; không tạo ID bên trong reducer.

Các ví dụ đầy đủ có `export default function App()` là các phương án thay thế nhau cho `src/App.jsx`; không dán tất cả vào một file. Các mẫu cú pháp riêng cần đặt trong component phù hợp.

## Tài liệu tham khảo

- [React: useEffect](https://react.dev/reference/react/useEffect).
- [React: useReducer](https://react.dev/reference/react/useReducer).

[Bài 3: React Router trong ReactJS](./lesson3.md) | [Bài 5: Ghi nhớ và tham chiếu](./lesson5.md) | [Quay về roadmap](./README.md)
