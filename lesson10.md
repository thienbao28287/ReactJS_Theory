# Bài 10: Kiểm tra dữ liệu form bằng Zod

[Quay về roadmap](./README.md)

Bài này hướng dẫn bạn chuyển quy tắc kiểm tra dữ liệu thành schema dùng lại được. Bạn sẽ tạo form đăng ký thử nghiệm, kiểm tra hai ô mật khẩu và phân biệt lỗi đầu vào với lỗi từ bước gửi dữ liệu.

### Kiến thức cần có và chuẩn bị

Hoàn thành [bài 9](./lesson9.md) để hiểu `useForm`, `register`, `handleSubmit` và `errors`. Trong project Vite, chạy:

```bash
npm install react-hook-form@7 zod@4 @hookform/resolvers@5
```

Ví dụ dùng Zod v4 và resolver v5. Giữ JavaScript với đuôi `.js`/`.jsx`, không cần chuyển project sang TypeScript. Chỉ dùng tài khoản và mật khẩu mẫu; form không tạo tài khoản thật.

### Kết quả sau bài học

- Khai báo schema cho chuỗi, số và object.
- Dùng `safeParse` để kiểm tra dữ liệu ngoài form.
- Kết nối schema vào React Hook Form bằng `zodResolver`.
- Hiển thị lỗi xác nhận mật khẩu và lỗi gửi dữ liệu riêng biệt.

## 1. Schema là gì?

**Schema** mô tả hình dạng và các điều kiện dữ liệu phải thỏa mãn. Zod nhận một giá trị, kiểm tra và trả dữ liệu hợp lệ hoặc thông tin lỗi. Việc kiểm tra này chạy trong JavaScript; không thay thế kiểm tra ở backend.

```js
import { z } from "zod";

const productSchema = z.object({
  title: z.string().trim().min(2, "Tên quá ngắn."),
  price: z.number().finite().positive("Giá phải lớn hơn 0."),
});

const result = productSchema.safeParse({ title: "Tai nghe", price: 350000 });
if (result.success) {
  console.log(result.data);
} else {
  console.log(result.error.issues);
}
```

Đây là ví dụ độc lập để thử trong module hoặc Console có hỗ trợ import qua project. `parse` ném lỗi nếu không hợp lệ; `safeParse` trả object có `success` để rẽ nhánh. Khi schema có `.trim()`, dùng `result.data` để nhận dữ liệu đã xử lý.

Input HTML thường cung cấp chuỗi. Với input số, có thể dùng `register("age", { valueAsNumber: true })` rồi schema `z.number()`. Input số rỗng có thể trở thành `NaN` và phải bị báo lỗi. `z.coerce.number()` dùng quy tắc chuyển kiểu của JavaScript; chuỗi rỗng có thể thành `0`, cần cân nhắc trước khi dùng.

## 2. Tạo schema đăng ký

Tạo thư mục `src/schemas` và file `src/schemas/registerSchema.js`:

```js
import { z } from "zod";

export const registerSchema = z.object({
  fullName: z.string().trim().min(2, "Họ tên cần ít nhất 2 ký tự."),
  email: z.string().trim().pipe(z.email("Email chưa đúng định dạng.")),
  age: z.number("Nhập tuổi bằng số.").int("Tuổi phải là số nguyên.")
    .min(18, "Ví dụ này yêu cầu từ 18 tuổi.").max(120, "Tuổi chưa hợp lệ."),
  password: z.string().min(8, "Mật khẩu cần ít nhất 8 ký tự."),
  confirmPassword: z.string().min(1, "Nhập lại mật khẩu."),
}).refine((data) => data.password === data.confirmPassword, {
  message: "Hai mật khẩu chưa khớp.",
  path: ["confirmPassword"],
});
```

`z.object` gom các trường vào một schema. `pipe` chuyển chuỗi đã trim sang bước kiểm tra email. `refine` đọc cả object để so sánh hai trường; `path` đặt thông báo vào đúng ô xác nhận. Không trim mật khẩu vì sẽ tự thay đổi ký tự người dùng nhập.

## 3. Kết nối schema với form

### Bước 1 Viết App.jsx

Thay toàn bộ `src/App.jsx` bằng:

```jsx
import { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { registerSchema } from "./schemas/registerSchema";

async function registerDemo(values) {
  await new Promise((resolve) => setTimeout(resolve, 500));
  if (values.email === "used@example.com") {
    throw new Error("Email thử nghiệm này đã được sử dụng.");
  }
  return { fullName: values.fullName, email: values.email };
}

function Field({ label, name, register, errors, type = "text", options }) {
  const error = errors[name];
  return (
    <div>
      <label htmlFor={name}>{label}</label>
      <input
        id={name} type={type}
        aria-invalid={Boolean(error)}
        aria-describedby={error ? `${name}-error` : undefined}
        {...register(name, options)}
      />
      {error && <p id={`${name}-error`} role="alert">{error.message}</p>}
    </div>
  );
}

export default function App() {
  const [account, setAccount] = useState(null);
  const {
    register, handleSubmit, reset, setError, clearErrors,
    formState: { errors, isSubmitting },
  } = useForm({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      fullName: "", email: "", age: "", password: "", confirmPassword: "",
    },
  });

  async function onSubmit(values) {
    setAccount(null);
    clearErrors("root.server");
    try {
      const { confirmPassword, ...payload } = values;
      // confirmPassword phục vụ kiểm tra trong form, không thuộc payload đăng ký.
      void confirmPassword;
      const saved = await registerDemo(payload);
      setAccount(saved);
      reset();
    } catch (error) {
      setError("root.server", { type: "server", message: error.message });
    }
  }

  return (
    <main>
      <h1>Đăng ký thử nghiệm</h1>
      <form noValidate onSubmit={handleSubmit(onSubmit, () => setAccount(null))}>
        <fieldset disabled={isSubmitting}>
          <legend>Thông tin tài khoản mẫu</legend>
          <Field label="Họ tên" name="fullName" register={register} errors={errors} />
          <Field label="Email" name="email" type="email" register={register} errors={errors} />
          <Field label="Tuổi" name="age" type="number" options={{ valueAsNumber: true }}
            register={register} errors={errors} />
          <Field label="Mật khẩu mẫu" name="password" type="password" register={register} errors={errors} />
          <Field label="Nhập lại mật khẩu" name="confirmPassword" type="password" register={register} errors={errors} />
          <button type="submit">{isSubmitting ? "Đang xử lý..." : "Đăng ký mẫu"}</button>
        </fieldset>
        {errors.root?.server && <p role="alert">{errors.root.server.message}</p>}
      </form>
      {account && <p role="status">Đã tạo bản mô phỏng cho {account.fullName} ({account.email}).</p>}
    </main>
  );
}
```

### Bước 2 Hiểu luồng kiểm tra

```text
Người dùng submit
  → React Hook Form lấy giá trị
  → zodResolver chạy schema
  → Nếu sai: đặt errors theo trường, không gọi onSubmit
  → Nếu đúng: gọi onSubmit với dữ liệu đã được schema xử lý
  → Mô phỏng gửi dữ liệu
  → Thành công: hiển thị kết quả và reset
  → Thất bại: giữ input, hiển thị root.server
```

`root.server` là lỗi cấp form vì request có thể thất bại dù dữ liệu hợp lệ theo schema. Trong ứng dụng thật, nếu backend chỉ rõ email bị trùng, có thể đặt lỗi vào `email` bằng `setError` theo hợp đồng API. Không tự lấy thông báo nội bộ của server để hiển thị cho người dùng.

## 4. Kiểm tra kết quả

1. Gửi form trống: có lỗi đầu vào, không có kết quả thành công.
2. Nhập tuổi 17, số thập phân và để rỗng để kiểm tra ba nhánh lỗi.
3. Nhập hai mật khẩu khác nhau: lỗi nằm ở ô xác nhận.
4. Điền dữ liệu hợp lệ với `used@example.com`: sau khoảng chờ hiện lỗi gửi, các trường vẫn giữ giá trị để sửa.
5. Đổi email thành `learner@example.com`, gửi lại: có bản mô phỏng và form được reset.
6. Nhập tên có khoảng trắng hai đầu: kết quả thành công nhận tên đã trim.

Mật khẩu không được lưu vào bản kết quả, localStorage hoặc Console của ví dụ. Đăng ký thật cần HTTPS, backend, chính sách mật khẩu và cơ chế xác thực riêng.

## 5. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Schema nhận chuỗi thay vì số | Dùng `valueAsNumber` cho trường số hoặc thiết kế bước chuyển kiểu rõ ràng. |
| Lỗi xác nhận không hiện cạnh input | Kiểm tra `path` trong refine và tên register. |
| Resolver không đọc được schema | Kiểm tra đúng major Zod và resolver đã cài trong bài. |
| Submit thất bại nhưng form bị xóa | Chỉ reset sau khi request thành công. |
| Bỏ qua validation trình duyệt để thử | `noValidate` chỉ tắt kiểm tra HTML, schema vẫn chạy. |

## 6. Ôn tập và bài tập thêm

1. `safeParse` và `parse` báo lỗi khác nhau như thế nào?
2. Vì sao không nên trim mọi trường một cách máy móc?
3. Tạo `productSchema` có tên, giá dương và số lượng nguyên không âm; thử với dữ liệu đúng và sai.
4. Thêm checkbox đồng ý điều khoản bằng `z.boolean().refine(value => value, ...)` và thông báo cụ thể.
5. Tách form đăng ký sang `src/components/RegisterForm.jsx`; App chỉ lắp ráp màn hình.

## Tài liệu tham khảo

- [Zod: Schema và validation](https://zod.dev/api).
- [React Hook Form Resolvers: Zod](https://github.com/react-hook-form/resolvers#zod).
- [React Hook Form: setError](https://react-hook-form.com/docs/useform/seterror).

[Bài 9: React Hook Form](./lesson9.md) | [Bài 11: Context và reducer](./lesson11.md) | [Quay về roadmap](./README.md)
