# Bài 9: Quản lý form bằng React Hook Form

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn tạo form nhận thông tin giao hàng, kiểm tra đầu vào và hiển thị kết quả gửi. Bạn sẽ chuyển việc theo dõi các ô nhập sang React Hook Form, dùng trạng thái form để báo lỗi và chặn gửi lặp khi đang xử lý.

### Kiến thức cần có và chuẩn bị

Bạn cần biết form HTML, sự kiện submit và `useState` ở bài 2. Mở project Vite, giữ `src/main.jsx` render `<App />`. Trong terminal tại project, chạy:

```bash
npm install react-hook-form@7
npm run dev
```

Ví dụ chỉ mô phỏng xử lý dữ liệu trong trình duyệt, không gửi thông tin cá nhân lên server. Dùng tên, email và địa chỉ thử nghiệm khi thực hành.

### Kết quả sau bài học

- Đăng ký input bằng `register` và xử lý submit bằng `handleSubmit`.
- Hiển thị lỗi gắn với đúng trường nhập liệu.
- Dùng `isSubmitting`, `isDirty`, `reset`, `watch` và `setValue`.
- Phân biệt kết quả gửi thành công với việc người dùng vừa sửa lại form.

## 1. Vì sao dùng thư viện form?

Ở bài 2, mỗi input có `value` và `onChange` cập nhật state. Cách này vẫn phù hợp với form nhỏ. Khi có nhiều trường, bạn cần quản lý thêm lỗi, giá trị ban đầu, ô đã sửa và trạng thái gửi.

**React Hook Form** cung cấp Hook `useForm` để quản lý các việc đó. Với input HTML thông thường, thư viện có thể theo dõi input qua ref mà không yêu cầu bạn viết một state riêng cho từng lần gõ. Các phần đăng ký theo dõi giá trị hoặc trạng thái vẫn có thể render lại.

| API | Vai trò |
| --- | --- |
| `register` | Kết nối input và khai báo quy tắc kiểm tra. |
| `handleSubmit` | Kiểm tra form rồi gọi hàm thành công hoặc hàm báo lỗi. |
| `formState.errors` | Lỗi của từng trường. |
| `formState.isSubmitting` | Cho biết callback submit đang xử lý. |
| `reset` | Đặt lại giá trị và trạng thái form. |
| `watch` | Đọc và theo dõi giá trị phục vụ giao diện. |
| `setValue` | Cập nhật một trường bằng code. |

## 2. Tạo form giao hàng

### Bước 1 Thay App.jsx

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import { useState } from "react";
import { useForm } from "react-hook-form";

const defaultValues = {
  fullName: "", email: "", address: "", note: "", express: false,
};

async function saveDemo(values) {
  await new Promise((resolve) => setTimeout(resolve, 600));
  return { ...values, id: crypto.randomUUID() };
}

export default function App() {
  const [receipt, setReceipt] = useState(null);
  const {
    register, handleSubmit, reset, watch, setValue,
    formState: { errors, isSubmitting, isDirty },
  } = useForm({ defaultValues, mode: "onSubmit" });

  const express = watch("express");
  const note = watch("note");

  async function onSubmit(values) {
    setReceipt(null);
    const saved = await saveDemo({
      ...values,
      fullName: values.fullName.trim(),
      email: values.email.trim(),
      address: values.address.trim(),
      note: values.note.trim(),
    });
    setReceipt(saved);
    reset(defaultValues);
  }

  return (
    <main>
      <h1>Thông tin giao hàng</h1>
      <form noValidate onSubmit={handleSubmit(onSubmit, () => setReceipt(null))}>
        <fieldset disabled={isSubmitting}>
          <legend>Thông tin người nhận</legend>
          <div>
            <label htmlFor="fullName">Họ tên</label>
            <input
              id="fullName" autoComplete="name"
              aria-invalid={Boolean(errors.fullName)}
              aria-describedby={errors.fullName ? "name-error" : undefined}
              {...register("fullName", {
                validate: (value) => value.trim().length >= 2 || "Nhập ít nhất 2 ký tự.",
              })}
            />
            {errors.fullName && <p id="name-error" role="alert">{errors.fullName.message}</p>}
          </div>
          <div>
            <label htmlFor="email">Email</label>
            <input
              id="email" type="email" autoComplete="email"
              aria-invalid={Boolean(errors.email)}
              aria-describedby={errors.email ? "email-error" : undefined}
              {...register("email", {
                required: "Vui lòng nhập email.",
                pattern: { value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, message: "Email chưa đúng định dạng." },
              })}
            />
            {errors.email && <p id="email-error" role="alert">{errors.email.message}</p>}
          </div>
          <div>
            <label htmlFor="address">Địa chỉ</label>
            <textarea
              id="address" autoComplete="street-address"
              aria-invalid={Boolean(errors.address)}
              aria-describedby={errors.address ? "address-error" : undefined}
              {...register("address", {
                validate: (value) => value.trim().length >= 10 || "Nhập địa chỉ ít nhất 10 ký tự.",
              })}
            />
            {errors.address && <p id="address-error" role="alert">{errors.address.message}</p>}
          </div>
          <label>
            <input type="checkbox" {...register("express")} /> Giao nhanh
          </label>
          <p>Hình thức: {express ? "Giao nhanh" : "Giao tiêu chuẩn"}</p>
          <div>
            <label htmlFor="note">Ghi chú, tối đa 200 ký tự</label>
            <textarea
              id="note" aria-describedby="note-help"
              {...register("note", { maxLength: { value: 200, message: "Ghi chú quá dài." } })}
            />
            <p id="note-help">Đã nhập {note.length}/200 ký tự.</p>
            {errors.note && <p role="alert">{errors.note.message}</p>}
          </div>
          <button type="button" onClick={() => setValue("note", "Gọi trước khi giao", {
            shouldDirty: true, shouldValidate: true,
          })}>Điền ghi chú mẫu</button>
          <button type="button" onClick={() => { reset(defaultValues); setReceipt(null); }}>
            Nhập lại
          </button>
          <button type="submit">{isSubmitting ? "Đang lưu..." : "Lưu thông tin"}</button>
        </fieldset>
      </form>
      <p>{isDirty ? "Form có thay đổi chưa lưu." : "Form đang ở giá trị mặc định."}</p>
      {receipt && (
        <section aria-live="polite">
          <h2>Đã lưu bản mô phỏng</h2>
          <p>{receipt.fullName} - {receipt.email}</p>
          <p>{receipt.address}</p>
        </section>
      )}
    </main>
  );
}
```

### Bước 2 Hiểu cách kết nối input

`register("fullName")` cung cấp `name`, `ref`, `onChange` và `onBlur`. Spread kết quả lên input để thư viện theo dõi trường. Không gán thêm một `value` cố định khiến input không gõ được; không ghi đè `onChange` mà quên gọi handler đã đăng ký.

`handleSubmit` trả một event handler cho `onSubmit`. Thư viện xử lý submit và validation trước khi gọi `onSubmit(values)`. `noValidate` tắt hộp báo lỗi mặc định của trình duyệt để bạn quan sát thông báo trong React.

Regex email trong bài chỉ kiểm tra hình thức cơ bản. Email đúng định dạng chưa chứng minh hộp thư tồn tại. Backend vẫn phải xác thực và kiểm tra dữ liệu.

### Bước 3 Hiểu trạng thái và thao tác

- `isSubmitting` giữ giá trị true trong lúc Promise của `onSubmit` chưa kết thúc. Vì callback `await saveDemo`, trạng thái chờ kéo dài đủ để quan sát.
- `fieldset disabled` khóa các trường khi đang lưu. Dữ liệu đã được nhận vào callback trước khi khóa.
- `watch("express")` và `watch("note")` cập nhật phần xem trước; chúng tạo nhu cầu render cho các giá trị được theo dõi.
- `setValue` điền một trường. `shouldDirty` và `shouldValidate` yêu cầu cập nhật trạng thái sửa và kiểm tra lại trường đó.
- `reset(defaultValues)` xóa dữ liệu đang nhập sau thành công. `receipt` là bản sao lần lưu trước, không phải giá trị hiện tại của form.

Ví dụ không có request thật nên chưa có lỗi mạng. Khi thay `saveDemo` bằng service, cần `try/catch`, hiển thị lỗi và chỉ reset sau khi server báo thành công; bài 10 minh họa nhánh thất bại.

## 3. Kiểm tra kết quả

1. Gửi form trống: tên, email và địa chỉ có thông báo; không có bản lưu.
2. Nhập toàn dấu cách ở tên/địa chỉ: vẫn bị từ chối.
3. Nhập email sai; sửa lại để thấy lỗi được cập nhật sau lượt gửi đầu.
4. Bật Giao nhanh và điền ghi chú mẫu: phần xem trước thay đổi, form được đánh dấu có sửa.
5. Gửi dữ liệu hợp lệ: trong khoảng chờ các nút bị khóa; sau đó có bản lưu và input được đặt lại.
6. Nhấn Nhập lại: dữ liệu và bản lưu được xóa. Tải lại trang: bản mô phỏng mất vì chưa lưu lâu dài.

## 4. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Trường không nằm trong dữ liệu submit | Kiểm tra tên và spread `register`. |
| Bấm Nhập lại lại gửi form | Nút phụ cần `type="button"`. |
| Form tải lại toàn trang | Gắn `onSubmit={handleSubmit(onSubmit)}` vào form. |
| Không thấy lỗi đúng chỗ | Tên `errors` phải khớp tên đăng ký. |
| Trạng thái gửi kết thúc quá sớm | Callback phải return hoặc await Promise xử lý. |

## 5. Ôn tập và bài tập thêm

1. `register` kết nối những thuộc tính nào của input?
2. `reset` khác `setValue` khi cập nhật trạng thái dirty như thế nào?
3. Thêm ô số điện thoại thử nghiệm; thông báo rõ định dạng mà form chấp nhận.
4. Tách một trường thành component riêng và truyền kết quả register cùng thông báo lỗi qua props.
5. Đổi `mode` sang `onBlur`, so sánh thời điểm báo lỗi trước lượt submit đầu tiên.

## Tài liệu tham khảo

- [React Hook Form: useForm](https://react-hook-form.com/docs/useform).
- [React Hook Form: register](https://react-hook-form.com/docs/useform/register).
- [React Hook Form: formState](https://react-hook-form.com/docs/useform/formstate).

[Bài 8: Custom Hooks](./lesson8.md) | [Bài 10: Zod](./lesson10.md) | [Quay về roadmap](./README.md)
