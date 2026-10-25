# Lộ trình học ReactJS trong 12 tuần

Tài liệu tự học Frontend với React, [GitHub HIT ReactJS 2026](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory) và [ReactJS Learning Roadmap](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap).

## Bắt đầu và cách sử dụng

1. Bắt đầu từ [W01 / Day01 — Theory](./W01/Day01/Theory.md), sau đó làm [Exercises](./W01/Day01/Exercises.md).
2. Học theo thứ tự tuần và ngày. Đọc mục chuẩn bị để biết dự án, thư mục chạy lệnh và phiên bản thư viện.
3. Tự chạy ví dụ, làm bài tập rồi đối chiếu kết quả mong đợi và tiêu chí hoàn thành.
4. Khi học, tự tạo `notes.md` hoặc `review.md` trong thư mục Day để lưu cách giải thích, lỗi đã gặp và bằng chứng kiểm tra.
5. Dùng ngày cuối tuần để tổng hợp, sửa bài còn thiếu và tự đánh giá trước khi chuyển tuần.

Điều kiện đầu vào: HTML, CSS và JavaScript cơ bản. W01 ôn JavaScript cần cho React; nếu vẫn khó khăn với hàm, object, array và async/await, dành thêm thời gian củng cố trước khi học Hooks.

## Tổng quan 12 tuần

| Tuần        | Trọng tâm                            | Kết quả / phạm vi                                                          |
| ----------- | ------------------------------------ | -------------------------------------------------------------------------- |
| [W01](#w01) | Nền tảng JavaScript, React và JSX    | Khởi tạo Vite, hiểu cấu trúc dự án và xây trang hồ sơ bằng Component.      |
| [W02](#w02) | Props, State và tương tác            | Truyền dữ liệu, xử lý sự kiện và hoàn thiện Todo CRUD.                     |
| [W03](#w03) | useEffect và API                     | Dependencies, cleanup, fetch, loading/error, hủy request và localStorage.  |
| [W04](#w04) | Custom Hooks, Axios và service layer | useRef, useToggle, useFetch, Axios, Interceptors và khởi tạo mini-shop.    |
| [W05](#w05) | React Router                         | Routes, navigation, URL params, nested routes, query, guard và 404.        |
| [W06](#w06) | Styling, form và validation          | Tailwind CSS, React Hook Form, Zod và checkout mô phỏng.                   |
| [W07](#w07) | Context API và useReducer            | Phân chia State, AuthProvider, CartProvider và persistence.                |
| [W08](#w08) | Redux Toolkit                        | Store, slice, selectors, async thunk, RTK Query và giới thiệu typed hooks. |
| [W09](#w09) | Hiệu năng và re-render               | Profiler, React.memo, useMemo, useCallback và tối ưu có đo lường.          |
| [W10](#w10) | Kiểm thử                             | Jest lab, Vitest, React Testing Library và Cypress E2E.                    |
| [W11](#w11) | Tổ chức dự án và triển khai          | Cấu trúc feature, env, Vercel, Gitflow, conflict, Docker và CI/CD.         |
| [W12](#w12) | Nâng cao và tổng kết                 | Data Router, Hooks React 18/19, Zustand, Redux Saga và hoàn thiện dự án.   |

## Cấu trúc tài liệu

```text
ReactJS/
  README.md
  W01/
    Day01/
      Theory.md
      Exercises.md
    Day02/
      Theory.md
      Exercises.md
  W02/
    Day01/
      Theory.md
      Exercises.md
```

Mỗi tuần từ `W01` đến `W12` có đủ `Day01` đến `Day07`. Cây trên minh họa quy ước đặt tên; danh mục bên dưới liên kết đầy đủ từng ngày.

## Dự án thực hành xuyên suốt

| Giai đoạn   | Thư mục được tạo khi thực hành | Mục đích                                                                  |
| ----------- | ------------------------------ | ------------------------------------------------------------------------- |
| W01–W02     | `W01/react-profile`            | Hồ sơ cá nhân, Component, Props/State và Todo                             |
| W03         | `W03/api-lab`                  | Effects, request lifecycle và xử lý lỗi API                               |
| W04–W12     | `W04/mini-shop`                | Dự án chính: sản phẩm, điều hướng, giỏ hàng, form, kiểm thử và triển khai |
| W10 / Day01 | `W10/jest-lab`                 | Lab Jest độc lập; dự án chính dùng Vitest                                 |
| W11 / Day05 | `W11/git-conflict-lab`         | Repository lab riêng để luyện conflict                                    |

Các thư mục dự án/lab được **bạn tạo theo hướng dẫn khi học**. Không khởi tạo lại mini-shop ở mỗi tuần; tiếp tục phát triển cùng dự án và lưu mốc Git trước các thay đổi lớn.

Bộ bài học dùng React Router v6 để khớp PDF, Tailwind CSS v4, React Hook Form v7 và Zod v4. Bài React 19 yêu cầu React và React DOM cùng major 19. Xem hướng dẫn từng ngày, lưu lockfile và kiểm tra yêu cầu Node của công cụ trước khi cài.

Auth, checkout và một số tác vụ async là **mô phỏng học tập**; fixture không thay việc kiểm tra API thật. Các bài Docker, CI/CD, Saga, Zustand và Hooks mới có phạm vi làm quen rõ trong từng ngày.

## Danh mục bài học theo ngày

<a id="w01"></a>

### W01 — Nền tảng JavaScript, React và JSX

Khởi tạo Vite, hiểu cấu trúc dự án và xây trang hồ sơ bằng Component.

| Ngày  | Bài học                                | Lý thuyết                       | Bài tập                               |
| ----- | -------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | JavaScript cần cho React               | [Theory](./W01/Day01/Theory.md) | [Exercises](./W01/Day01/Exercises.md) |
| Day02 | Xử lý dữ liệu, async và khởi tạo Vite  | [Theory](./W01/Day02/Theory.md) | [Exercises](./W01/Day02/Exercises.md) |
| Day03 | React, SPA và cấu trúc dự án           | [Theory](./W01/Day03/Theory.md) | [Exercises](./W01/Day03/Exercises.md) |
| Day04 | Viết giao diện bằng JSX                | [Theory](./W01/Day04/Theory.md) | [Exercises](./W01/Day04/Exercises.md) |
| Day05 | Functional Component và ghép giao diện | [Theory](./W01/Day05/Theory.md) | [Exercises](./W01/Day05/Exercises.md) |
| Day06 | Xây trang hồ sơ học tập                | [Theory](./W01/Day06/Theory.md) | [Exercises](./W01/Day06/Exercises.md) |
| Day07 | Ôn tập, tự đánh giá và lưu kết quả     | [Theory](./W01/Day07/Theory.md) | [Exercises](./W01/Day07/Exercises.md) |

<a id="w02"></a>

### W02 — Props, State và tương tác

Truyền dữ liệu, xử lý sự kiện và hoàn thiện Todo CRUD.

| Ngày  | Bài học                               | Lý thuyết                       | Bài tập                               |
| ----- | ------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | Props và children                     | [Theory](./W02/Day01/Theory.md) | [Exercises](./W02/Day01/Exercises.md) |
| Day02 | Sự kiện và callback Props             | [Theory](./W02/Day02/Theory.md) | [Exercises](./W02/Day02/Exercises.md) |
| Day03 | useState và cập nhật theo state trước | [Theory](./W02/Day03/Theory.md) | [Exercises](./W02/Day03/Exercises.md) |
| Day04 | State object và array bất biến        | [Theory](./W02/Day04/Theory.md) | [Exercises](./W02/Day04/Exercises.md) |
| Day05 | Điều kiện, lists và key               | [Theory](./W02/Day05/Theory.md) | [Exercises](./W02/Day05/Exercises.md) |
| Day06 | Controlled input và Todo CRUD         | [Theory](./W02/Day06/Theory.md) | [Exercises](./W02/Day06/Exercises.md) |
| Day07 | Tổng kết Props–State và Todo          | [Theory](./W02/Day07/Theory.md) | [Exercises](./W02/Day07/Exercises.md) |

<a id="w03"></a>

### W03 — useEffect và API

Dependencies, cleanup, fetch, loading/error, hủy request và localStorage.

| Ngày  | Bài học                              | Lý thuyết                       | Bài tập                               |
| ----- | ------------------------------------ | ------------------------------- | ------------------------------------- |
| Day01 | Render, vòng đời và side effects     | [Theory](./W03/Day01/Theory.md) | [Exercises](./W03/Day01/Exercises.md) |
| Day02 | Dependency array và stale closure    | [Theory](./W03/Day02/Theory.md) | [Exercises](./W03/Day02/Exercises.md) |
| Day03 | Cleanup timer và event listener      | [Theory](./W03/Day03/Theory.md) | [Exercises](./W03/Day03/Exercises.md) |
| Day04 | fetch và HTTP cơ bản                 | [Theory](./W03/Day04/Theory.md) | [Exercises](./W03/Day04/Exercises.md) |
| Day05 | Loading, error, empty và retry       | [Theory](./W03/Day05/Theory.md) | [Exercises](./W03/Day05/Exercises.md) |
| Day06 | Tìm kiếm API và hủy request          | [Theory](./W03/Day06/Theory.md) | [Exercises](./W03/Day06/Exercises.md) |
| Day07 | Lưu localStorage và tổng kết effects | [Theory](./W03/Day07/Theory.md) | [Exercises](./W03/Day07/Exercises.md) |

<a id="w04"></a>

### W04 — Custom Hooks, Axios và service layer

useRef, useToggle, useFetch, Axios, Interceptors và khởi tạo mini-shop.

| Ngày  | Bài học                                   | Lý thuyết                       | Bài tập                               |
| ----- | ----------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | useRef: DOM và giá trị không gây render   | [Theory](./W04/Day01/Theory.md) | [Exercises](./W04/Day01/Exercises.md) |
| Day02 | Custom Hook useToggle                     | [Theory](./W04/Day02/Theory.md) | [Exercises](./W04/Day02/Exercises.md) |
| Day03 | Custom Hook useFetch có cleanup           | [Theory](./W04/Day03/Theory.md) | [Exercises](./W04/Day03/Exercises.md) |
| Day04 | Axios và Axios Instance                   | [Theory](./W04/Day04/Theory.md) | [Exercises](./W04/Day04/Exercises.md) |
| Day05 | Interceptors, Swagger và Postman          | [Theory](./W04/Day05/Theory.md) | [Exercises](./W04/Day05/Exercises.md) |
| Day06 | Service layer và khung mini-shop          | [Theory](./W04/Day06/Theory.md) | [Exercises](./W04/Day06/Exercises.md) |
| Day07 | Tổng kết custom Hooks và API architecture | [Theory](./W04/Day07/Theory.md) | [Exercises](./W04/Day07/Exercises.md) |

<a id="w05"></a>

### W05 — React Router

Routes, navigation, URL params, nested routes, query, guard và 404.

| Ngày  | Bài học                           | Lý thuyết                       | Bài tập                               |
| ----- | --------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | Router, Routes và Route           | [Theory](./W05/Day01/Theory.md) | [Exercises](./W05/Day01/Exercises.md) |
| Day02 | Link, NavLink và useNavigate      | [Theory](./W05/Day02/Theory.md) | [Exercises](./W05/Day02/Exercises.md) |
| Day03 | Dynamic routes và useParams       | [Theory](./W05/Day03/Theory.md) | [Exercises](./W05/Day03/Exercises.md) |
| Day04 | Nested routes, layout và Outlet   | [Theory](./W05/Day04/Theory.md) | [Exercises](./W05/Day04/Exercises.md) |
| Day05 | Query params và useLocation       | [Theory](./W05/Day05/Theory.md) | [Exercises](./W05/Day05/Exercises.md) |
| Day06 | Protected route và 404            | [Theory](./W05/Day06/Theory.md) | [Exercises](./W05/Day06/Exercises.md) |
| Day07 | Tổng kết navigation của mini-shop | [Theory](./W05/Day07/Theory.md) | [Exercises](./W05/Day07/Exercises.md) |

<a id="w06"></a>

### W06 — Styling, form và validation

Tailwind CSS, React Hook Form, Zod và checkout mô phỏng.

| Ngày  | Bài học                                   | Lý thuyết                       | Bài tập                               |
| ----- | ----------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | Form có kiểm soát và UX nhập liệu         | [Theory](./W06/Day01/Theory.md) | [Exercises](./W06/Day01/Exercises.md) |
| Day02 | Tailwind CSS v4 và responsive             | [Theory](./W06/Day02/Theory.md) | [Exercises](./W06/Day02/Exercises.md) |
| Day03 | React Hook Form: register và handleSubmit | [Theory](./W06/Day03/Theory.md) | [Exercises](./W06/Day03/Exercises.md) |
| Day04 | formState, reset, watch và setValue       | [Theory](./W06/Day04/Theory.md) | [Exercises](./W06/Day04/Exercises.md) |
| Day05 | Zod: schema và validation                 | [Theory](./W06/Day05/Theory.md) | [Exercises](./W06/Day05/Exercises.md) |
| Day06 | Kết hợp RHF và Zod cho checkout           | [Theory](./W06/Day06/Theory.md) | [Exercises](./W06/Day06/Exercises.md) |
| Day07 | Tổng kết form và giao diện                | [Theory](./W06/Day07/Theory.md) | [Exercises](./W06/Day07/Exercises.md) |

<a id="w07"></a>

### W07 — Context API và useReducer

Phân chia State, AuthProvider, CartProvider và persistence.

| Ngày  | Bài học                                   | Lý thuyết                       | Bài tập                               |
| ----- | ----------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | State cục bộ, nâng State và prop drilling | [Theory](./W07/Day01/Theory.md) | [Exercises](./W07/Day01/Exercises.md) |
| Day02 | Context API và useContext                 | [Theory](./W07/Day02/Theory.md) | [Exercises](./W07/Day02/Exercises.md) |
| Day03 | AuthProvider mô phỏng                     | [Theory](./W07/Day03/Theory.md) | [Exercises](./W07/Day03/Exercises.md) |
| Day04 | useReducer: action và reducer thuần       | [Theory](./W07/Day04/Theory.md) | [Exercises](./W07/Day04/Exercises.md) |
| Day05 | Context + reducer cho giỏ hàng            | [Theory](./W07/Day05/Theory.md) | [Exercises](./W07/Day05/Exercises.md) |
| Day06 | Persist giỏ hàng và derived data          | [Theory](./W07/Day06/Theory.md) | [Exercises](./W07/Day06/Exercises.md) |
| Day07 | Tổng kết kiến trúc Context và reducer     | [Theory](./W07/Day07/Theory.md) | [Exercises](./W07/Day07/Exercises.md) |

<a id="w08"></a>

### W08 — Redux Toolkit

Store, slice, selectors, async thunk, RTK Query và giới thiệu typed hooks.

| Ngày  | Bài học                                     | Lý thuyết                       | Bài tập                               |
| ----- | ------------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | Redux Core và luồng một chiều               | [Theory](./W08/Day01/Theory.md) | [Exercises](./W08/Day01/Exercises.md) |
| Day02 | configureStore, createSlice và Provider     | [Theory](./W08/Day02/Theory.md) | [Exercises](./W08/Day02/Exercises.md) |
| Day03 | useSelector, useDispatch và chuyển giỏ hàng | [Theory](./W08/Day03/Theory.md) | [Exercises](./W08/Day03/Exercises.md) |
| Day04 | State structure, selectors và DevTools      | [Theory](./W08/Day04/Theory.md) | [Exercises](./W08/Day04/Exercises.md) |
| Day05 | createAsyncThunk và request lifecycle       | [Theory](./W08/Day05/Theory.md) | [Exercises](./W08/Day05/Exercises.md) |
| Day06 | RTK Query và giới thiệu typed hooks         | [Theory](./W08/Day06/Theory.md) | [Exercises](./W08/Day06/Exercises.md) |
| Day07 | Tổng kết Redux và kiến trúc dữ liệu         | [Theory](./W08/Day07/Theory.md) | [Exercises](./W08/Day07/Exercises.md) |

<a id="w09"></a>

### W09 — Hiệu năng và re-render

Profiler, React.memo, useMemo, useCallback và tối ưu có đo lường.

| Ngày  | Bài học                                  | Lý thuyết                       | Bài tập                               |
| ----- | ---------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | Nguồn gốc re-render                      | [Theory](./W09/Day01/Theory.md) | [Exercises](./W09/Day01/Exercises.md) |
| Day02 | Profiler và phương pháp đo               | [Theory](./W09/Day02/Theory.md) | [Exercises](./W09/Day02/Exercises.md) |
| Day03 | React.memo và tham chiếu Props           | [Theory](./W09/Day03/Theory.md) | [Exercises](./W09/Day03/Exercises.md) |
| Day04 | useMemo cho tính toán suy ra             | [Theory](./W09/Day04/Theory.md) | [Exercises](./W09/Day04/Exercises.md) |
| Day05 | useCallback và callback Props            | [Theory](./W09/Day05/Theory.md) | [Exercises](./W09/Day05/Exercises.md) |
| Day06 | Tối ưu catalog bằng một thay đổi đo được | [Theory](./W09/Day06/Theory.md) | [Exercises](./W09/Day06/Exercises.md) |
| Day07 | Tổng kết performance và rà soát effects  | [Theory](./W09/Day07/Theory.md) | [Exercises](./W09/Day07/Exercises.md) |

<a id="w10"></a>

### W10 — Kiểm thử

Jest lab, Vitest, React Testing Library và Cypress E2E.

| Ngày  | Bài học                                | Lý thuyết                       | Bài tập                               |
| ----- | -------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | Testing pyramid và Jest cơ bản         | [Theory](./W10/Day01/Theory.md) | [Exercises](./W10/Day01/Exercises.md) |
| Day02 | Vitest và test reducer/selector        | [Theory](./W10/Day02/Theory.md) | [Exercises](./W10/Day02/Exercises.md) |
| Day03 | React Testing Library: render và query | [Theory](./W10/Day03/Theory.md) | [Exercises](./W10/Day03/Exercises.md) |
| Day04 | userEvent và giỏ hàng tích hợp         | [Theory](./W10/Day04/Theory.md) | [Exercises](./W10/Day04/Exercises.md) |
| Day05 | Test validation và loading/error       | [Theory](./W10/Day05/Theory.md) | [Exercises](./W10/Day05/Exercises.md) |
| Day06 | Cypress E2E cho luồng sản phẩm–giỏ     | [Theory](./W10/Day06/Theory.md) | [Exercises](./W10/Day06/Exercises.md) |
| Day07 | Tổng kết test và sửa lỗi hồi quy       | [Theory](./W10/Day07/Theory.md) | [Exercises](./W10/Day07/Exercises.md) |

<a id="w11"></a>

### W11 — Tổ chức dự án và triển khai

Cấu trúc feature, env, Vercel, Gitflow, conflict, Docker và CI/CD.

| Ngày  | Bài học                                   | Lý thuyết                       | Bài tập                               |
| ----- | ----------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | Cấu trúc dự án theo tính năng             | [Theory](./W11/Day01/Theory.md) | [Exercises](./W11/Day01/Exercises.md) |
| Day02 | Biến môi trường Vite và cấu hình API      | [Theory](./W11/Day02/Theory.md) | [Exercises](./W11/Day02/Exercises.md) |
| Day03 | Build, preview và deploy Vercel           | [Theory](./W11/Day03/Theory.md) | [Exercises](./W11/Day03/Exercises.md) |
| Day04 | Gitflow thực hành và Pull Request         | [Theory](./W11/Day04/Theory.md) | [Exercises](./W11/Day04/Exercises.md) |
| Day05 | Conflict, README và bàn giao              | [Theory](./W11/Day05/Theory.md) | [Exercises](./W11/Day05/Exercises.md) |
| Day06 | Docker nhiều giai đoạn và Nginx           | [Theory](./W11/Day06/Theory.md) | [Exercises](./W11/Day06/Exercises.md) |
| Day07 | CI/CD tổng quan và kiểm tra bản phát hành | [Theory](./W11/Day07/Theory.md) | [Exercises](./W11/Day07/Exercises.md) |

<a id="w12"></a>

### W12 — Nâng cao và tổng kết

Data Router, Hooks React 18/19, Zustand, Redux Saga và hoàn thiện dự án.

| Ngày  | Bài học                                             | Lý thuyết                       | Bài tập                               |
| ----- | --------------------------------------------------- | ------------------------------- | ------------------------------------- |
| Day01 | Data Router: loader, pending và lỗi                 | [Theory](./W12/Day01/Theory.md) | [Exercises](./W12/Day01/Exercises.md) |
| Day02 | Hooks React 18: useId, transition và deferred value | [Theory](./W12/Day02/Theory.md) | [Exercises](./W12/Day02/Exercises.md) |
| Day03 | React 19 Actions và optimistic UI                   | [Theory](./W12/Day03/Theory.md) | [Exercises](./W12/Day03/Exercises.md) |
| Day04 | Zustand: store nhỏ và selectors                     | [Theory](./W12/Day04/Theory.md) | [Exercises](./W12/Day04/Exercises.md) |
| Day05 | Redux Saga: generator và quản lý side effects       | [Theory](./W12/Day05/Theory.md) | [Exercises](./W12/Day05/Exercises.md) |
| Day06 | Hoàn thiện sản phẩm và bản phát hành học tập        | [Theory](./W12/Day06/Theory.md) | [Exercises](./W12/Day06/Exercises.md) |
| Day07 | Tự đánh giá 12 tuần và hướng phát triển             | [Theory](./W12/Day07/Theory.md) | [Exercises](./W12/Day07/Exercises.md) |

## Tiêu chí hoàn thành

- Hoàn thành tiêu chí cụ thể trong từng bài; tự giải thích được dữ liệu, luồng cập nhật và cách tổ chức code.
- Lưu kết quả kiểm tra thực tế cho ca bình thường và ca lỗi/biên; chỉ đánh dấu đã chạy khi thực sự thực hiện.
- Với bài có thang điểm, đạt từ 8/10 và không còn lỗi ngăn chạy phần cốt lõi trước khi chuyển bài.
- Kết thúc lộ trình, có mini-shop chạy được, tài liệu cách chạy, kiểm thử quan trọng và kết quả build/triển khai đúng với phạm vi đã thực hiện.

## Nguồn tài liệu gốc

- [GitHub Theory](https://github.com/nguyenlehoainam/HIT_ReactJs_2026/tree/main/Theory) và [roadmap](https://v0-reactjs-learning-roadmap-yt.vercel.app/roadmap): lộ trình và các phần mở rộng.

Mỗi file Theory có mục nguồn và tài liệu chính thức để đối chiếu API. Ví dụ, dữ liệu mẫu, bài tập và cách phân bổ thời gian được biên soạn bổ sung cho lịch 2 tiếng/ngày.
