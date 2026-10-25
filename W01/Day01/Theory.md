# W01 · Day01 — JavaScript cần cho React

## Mục tiêu và thời lượng

Sau buổi này, bạn đọc được arrow function, destructuring, spread và module; viết được hàm biến đổi dữ liệu mà không sửa dữ liệu gốc.

Lịch 120 phút: 10 phút kiểm tra đầu vào, 35 phút đọc và chạy ví dụ, 65 phút làm [bài tập](./Exercises.md), 10 phút ghi chú.

Điều kiện đầu vào: biết HTML, CSS cơ bản, biến, điều kiện và hàm JavaScript. Nếu chưa viết được hàm nhận một số rồi trả về bình phương của số đó, hãy dành thêm thời gian cho JavaScript trước khi chuyển sang React.

## 1. `const` và `let`

Dùng `const` khi không gán lại biến; dùng `let` khi cần gán lại. Cả hai có phạm vi theo block. `const` không làm object hay array trở thành bất biến.

```js
const learner = { name: 'Bao', level: 'beginner' };
learner.level = 'learning';
let completedLessons = 0;
completedLessons += 1;
console.log(learner.level, completedLessons);
```

Ví dụ chạy được trong Console của trình duyệt. Việc sửa object trên hợp lệ trong JavaScript, nhưng khi học React State bạn thường cần tạo object mới thay vì sửa trực tiếp object hiện có.

## 2. Hàm và arrow function

Hàm nhận đầu vào qua tham số, trả kết quả bằng `return`. Arrow function không tự động trả về nếu thân hàm dùng `{}`.

```js
function double(value) {
  return value * 2;
}
const triple = (value) => value * 3;
const createLearner = (name) => ({ name, active: true });
console.log(double(4), triple(4), createLearner('Bao'));
```

Kết quả đầu là `8`, `12`. Dấu `()` ở `({ name, active: true })` giúp trả về object. Trong React, component cũng thường là một hàm, nhưng trả về mô tả giao diện thay vì một con số.

## 3. Destructuring và giá trị mặc định

Destructuring lấy dữ liệu ra khỏi object/array theo cấu trúc.

```js
const profile = { name: 'Bao', city: 'Ha Noi' };
const { name, city, role = 'Student' } = profile;
const [firstSkill, secondSkill] = ['HTML', 'CSS'];
console.log(`${name} — ${city} — ${role}`);
console.log(firstSkill, secondSkill);
```

Giá trị mặc định áp dụng khi giá trị là `undefined`, không thay thế `null`. Với object, tên thuộc tính có ý nghĩa; với array, vị trí có ý nghĩa.

## 4. Spread và rest

Spread mở rộng dữ liệu; rest gom các giá trị còn lại. Cùng ký hiệu `...`, nhưng vai trò phụ thuộc vị trí.

```js
const original = { name: 'Bao', city: 'Ha Noi' };
const updated = { ...original, city: 'Da Nang' };
const skills = ['HTML', 'CSS'];
const nextSkills = [...skills, 'JavaScript'];
const { name, ...otherInfo } = updated;
console.log(original.city, updated.city);
console.log(nextSkills, name, otherInfo);
```

Thuộc tính viết sau ghi đè thuộc tính viết trước. Spread chỉ sao chép nông: object lồng nhau vẫn có thể được dùng chung tham chiếu.

```js
const oldProfile = { address: { city: 'Ha Noi' } };
const newProfile = {
  ...oldProfile,
  address: { ...oldProfile.address, city: 'Hue' },
};
console.log(oldProfile.address.city, newProfile.address.city);
```

## 5. Template literal và modules

Template literal dùng dấu backtick và `${expression}`. Module cho phép tách chức năng sang nhiều file.

`helpers.js`:

```js
export const courseName = 'React Fundamentals';
export function formatGreeting(name) {
  return `Xin chào ${name}!`;
}
export default function add(a, b) {
  return a + b;
}
```

`main.js`:

```js
import add, { courseName, formatGreeting } from './helpers.js';
console.log(courseName, formatGreeting('Bao'), add(2, 3));
```

Named import khớp tên export; default import có thể đặt tên khác. Hai file module không chạy bằng cách dán cả hai vào Console. Day02 sẽ chạy chúng bằng Node; trong Vite, module được hỗ trợ sẵn.

## Lỗi thường gặp

- Arrow function có `{}` nhưng quên `return` nên trả về `undefined`.
- Nghĩ spread sao chép sâu mọi cấp dữ liệu.
- Nhầm named import với default import.
- Dùng `const` rồi gán lại toàn bộ biến.

## Tự kiểm tra

Bạn cần giải thích được vì sao `const` vẫn cho sửa thuộc tính và vì sao `{ ...old, city: 'Hue' }` tạo phiên bản mới của object.

## Nguồn và phạm vi

Đây là phần JavaScript bổ trợ để đọc JSX/Component trong tài liệu gốc, không phải một chương riêng trong PDF. Đối chiếu [roadmap](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap), mục JSX và Components; đọc thêm [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide).

Tiếp theo: [Day02 — Array, async và môi trường](../Day02/Theory.md).
