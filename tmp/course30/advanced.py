from project import *

def advanced():
    put(24,'src/features/products/productsSlice.js','''
    import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
    import { productService } from '../../services/products';
    export const fetchProducts = createAsyncThunk('products/fetch', async (q, { signal }) => productService.list({ q, signal }));
    const slice = createSlice({ name: 'products', initialState: { data: null, status: 'idle', error: '', requestId: null }, reducers: {}, extraReducers: builder => {
      builder.addCase(fetchProducts.pending, (state, action) => { state.status = 'loading'; state.data = null; state.error = ''; state.requestId = action.meta.requestId; })
        .addCase(fetchProducts.fulfilled, (state, action) => { if (state.requestId === action.meta.requestId) { state.status = 'success'; state.data = action.payload; state.requestId = null; } })
        .addCase(fetchProducts.rejected, (state, action) => { if (state.requestId === action.meta.requestId) { state.status = action.meta.aborted ? 'idle' : 'error'; state.error = action.meta.aborted ? '' : 'Không tải được sản phẩm'; state.requestId = null; } });
    } });
    export default slice.reducer;
    ''')
    put(24,'src/app/store.js',"import { configureStore } from '@reduxjs/toolkit';\nimport cart from '../cart/slice';\nimport products from '../features/products/productsSlice';\nexport const store = configureStore({ reducer: { cart, products } });")
    put(24,'src/pages/Catalog.jsx','''
    import { useEffect, useRef, useState } from 'react';
    import { useDispatch, useSelector } from 'react-redux';
    import { useSearchParams } from 'react-router-dom';
    import { useDebounce } from '../hooks/useDebounce';
    import { fetchProducts } from '../features/products/productsSlice';
    import ProductList from '../components/ProductList';
    export default function Catalog() {
      const [params, setParams] = useSearchParams(); const q = params.get('q') || ''; const search = useDebounce(q);
      const inputRef = useRef(null), dispatch = useDispatch(); const state = useSelector(s => s.products); const [attempt, setAttempt] = useState(0);
      useEffect(() => { const task = dispatch(fetchProducts(search)); return () => task.abort(); }, [dispatch, search, attempt]);
      return <section><h1>Sản phẩm</h1><button onClick={() => inputRef.current?.focus()}>Focus tìm kiếm</button>
        <label>Tìm sản phẩm<input ref={inputRef} value={q} onChange={e => setParams({ q: e.target.value })} /></label>
        {state.status === 'error' ? <p role="alert">{state.error}<button onClick={() => setAttempt(n => n + 1)}>Thử lại</button></p>
          : !state.data ? <p role="status">Đang tải...</p> : <ProductList products={state.data.products} />}
      </section>;
    }
    ''')
    remove(24,'src/hooks/useProducts.js');snap(24)
    put(25,'src/features/products/productsApi.js','''
    import { createApi } from '@reduxjs/toolkit/query/react';
    import { http } from '../../services/http';
    const axiosBaseQuery = async (config, { signal }) => {
      try { return { data: await http({ ...config, signal }) }; }
      catch (error) { return { error: { status: error.response?.status || 'NETWORK_ERROR', data: error.response?.data || 'Không tải được dữ liệu' } }; }
    };
    export const productsApi = createApi({ reducerPath: 'productsApi', baseQuery: axiosBaseQuery, keepUnusedDataFor: 60,
      endpoints: builder => ({
        listProducts: builder.query({ query: ({ q = '', limit = 12, skip = 0, category = '' } = {}) => ({
          url: category ? `/products/category/${encodeURIComponent(category)}` : '/products/search', params: { q, limit, skip },
        }), transformResponse: data => { if (!Array.isArray(data.products)) throw new Error('Sai dữ liệu products'); return data; } }),
        getProduct: builder.query({ query: id => ({ url: `/products/${encodeURIComponent(id)}` }) }),
        getCategories: builder.query({ query: () => ({ url: '/products/categories' }) }),
      }),
    });
    export const { useListProductsQuery, useGetProductQuery, useGetCategoriesQuery } = productsApi;
    ''')
    put(25,'src/app/store.js','''
    import { configureStore } from '@reduxjs/toolkit';
    import { setupListeners } from '@reduxjs/toolkit/query';
    import cart from '../cart/slice';
    import { productsApi } from '../features/products/productsApi';
    export const store = configureStore({ reducer: { cart, [productsApi.reducerPath]: productsApi.reducer },
      middleware: getDefault => getDefault().concat(productsApi.middleware) });
    setupListeners(store.dispatch);
    ''')
    put(25,'src/pages/Catalog.jsx','''
    import { useRef } from 'react';
    import { useSearchParams } from 'react-router-dom';
    import { useDebounce } from '../hooks/useDebounce';
    import { useListProductsQuery } from '../features/products/productsApi';
    import ProductList from '../components/ProductList';
    export default function Catalog() {
      const [params, setParams] = useSearchParams(); const q = params.get('q') || ''; const search = useDebounce(q); const inputRef = useRef(null);
      const { currentData: data, isFetching, isError, refetch } = useListProductsQuery({ q: search });
      return <section><h1>Sản phẩm</h1><button onClick={() => inputRef.current?.focus()}>Focus tìm kiếm</button>
        <label>Tìm sản phẩm<input ref={inputRef} value={q} onChange={e => setParams({ q: e.target.value })} /></label>
        {isFetching && <p role="status">Đang cập nhật...</p>}
        {isError ? <p role="alert">Không tải được sản phẩm.<button disabled={isFetching} onClick={refetch}>Thử lại</button></p>
          : !data ? <p>Chưa có dữ liệu.</p> : <ProductList products={data.products} />}
      </section>;
    }
    ''')
    put(25,'src/pages/ProductDetail.jsx','''
    import { useParams } from 'react-router-dom';
    import { useGetProductQuery } from '../features/products/productsApi';
    import { useCart } from '../cart/CartContext';
    export default function ProductDetail() {
      const { id } = useParams(); const cart = useCart(); const { currentData: p, isFetching, isError } = useGetProductQuery(id);
      if (isError) return <p role="alert">Không tìm thấy hoặc không tải được sản phẩm.</p>;
      if (!p) return <p role="status">Đang tải chi tiết...</p>;
      return <article><h1>{p.title}</h1>{isFetching && <p role="status">Đang cập nhật...</p>}
        <img src={p.thumbnail} alt={p.title} width="240" height="240" /><p>{p.description}</p><p>{p.price} USD</p>
        <button disabled={p.stock <= 0} onClick={() => cart.add(p)}>Thêm vào giỏ</button>
      </article>;
    }
    ''')
    remove(25,'src/features/products/productsSlice.js');snap(25)
    put(26,'labs/router-lab/src/main.jsx','''
    import { StrictMode } from 'react';
    import { createRoot } from 'react-dom/client';
    import { createBrowserRouter, isRouteErrorResponse, Link, Outlet, RouterProvider, useLoaderData, useNavigation, useRouteError } from 'react-router-dom';
    function Layout() { const navigation = useNavigation(); return <main><h1>Data Router Lab</h1>
      <Link to="/">Bắt đầu</Link>{' | '}<Link to="/products/1">Sản phẩm 1</Link>{' | '}<Link to="/products/0">Thử lỗi</Link>
      {navigation.state === 'loading' && <p role="status">Đang tải route...</p>}<Outlet /></main>; }
    async function loader({ params, request }) {
      const response = await fetch(`https://dummyjson.com/products/${encodeURIComponent(params.id)}`, { signal: request.signal });
      if (!response.ok) throw new Response('Không tải được chi tiết', { status: response.status });
      return response.json();
    }
    function Product() { const p = useLoaderData(); return <article><h2>{p.title}</h2><p>{p.description}</p><p>{p.price} USD</p></article>; }
    function ErrorPage() { const error = useRouteError(); return <p role="alert">{isRouteErrorResponse(error) ? `HTTP ${error.status}: ${error.data}` : 'Lỗi route không xác định'}</p>; }
    const router = createBrowserRouter([{ path: '/', element: <Layout />, errorElement: <ErrorPage />, children: [
      { index: true, element: <p>Nhấn sản phẩm để quan sát loader.</p> },
      { path: 'products/:id', element: <Product />, loader, errorElement: <ErrorPage /> },
      { path: '*', element: <p>404 Lab</p> },
    ] }]);
    export default function DataRouterLab() { return <RouterProvider router={router} fallbackElement={<p role="status">Đang khởi tạo lab...</p>} />; }
    createRoot(document.getElementById('root')).render(<StrictMode><DataRouterLab /></StrictMode>);
    ''')
    put(26,'labs/router-lab/index.html','''
    <!doctype html>
    <html lang="vi"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>Data Router Lab</title></head><body><div id="root"></div><script type="module" src="/src/main.jsx"></script></body></html>
    ''')
    put(26,'labs/router-lab/vite.config.js',"import { defineConfig } from 'vite';\nimport react from '@vitejs/plugin-react';\nimport { fileURLToPath } from 'node:url';\nexport default defineConfig({ root: fileURLToPath(new URL('.', import.meta.url)), plugins: [react()], server: { port: 5174, strictPort: true }, build: { outDir: 'dist' } });")
    p=json.loads(FILES['package.json']);p['scripts']['lab:router']='vite --config labs/router-lab/vite.config.js';put(26,'package.json',json.dumps(p,indent=2))
    CMDS[26]='npm run lab:router'
    NOTES[26]='Lab chạy riêng trên http://localhost:5174 bằng script lab:router; cửa hàng chính vẫn dùng npm run dev ở cổng khác. Hai app không lồng router và không chia sẻ việc tải catalog. Có thể reload /products/1 trên cổng lab để thử loader lúc khởi tạo. Dừng lab sau khi thực hành, không thay main.jsx của cửa hàng.'
    snap(26)
    put(27,'src/labs/PerformanceDemo.jsx','''
    import { memo, Profiler, useCallback, useMemo, useState } from 'react';
    const products = Array.from({ length: 30000 }, (_, id) => ({ id, title: `Sản phẩm thử ${id}` }));
    const Summary = memo(function Summary({ total, onReset }) { return <p>{total} kết quả <button onClick={onReset}>Xóa từ khóa thử</button></p>; });
    export default function PerformanceDemo() {
      const [q, setQ] = useState(''), [note, setNote] = useState('');
      const filtered = useMemo(() => products.filter(p => p.title.includes(q)), [q]);
      const reset = useCallback(() => setQ(''), []);
      return <Profiler id="demo" onRender={(id, phase, actualDuration) => console.log({ id, phase, actualDuration })}><section>
        <h2>Phòng đo hiệu năng</h2><label>Từ khóa thử<input value={q} onChange={e => setQ(e.target.value)} /></label>
        <label>Ghi chú không ảnh hưởng bộ lọc<input value={note} onChange={e => setNote(e.target.value)} /></label>
        <Summary total={filtered.length} onReset={reset} />
      </section></Profiler>;
    }
    ''')
    change(27,'src/pages/Catalog.jsx',"import ProductList", "import PerformanceDemo from '../labs/PerformanceDemo';\nimport ProductList")
    change(27,'src/pages/Catalog.jsx','<section><h1>Sản phẩm</h1>','<section><h1>Sản phẩm</h1><PerformanceDemo />');snap(27)
    put(28,'.env.example','VITE_API_BASE_URL=https://dummyjson.com\n')
    change(28,'src/services/http.js',"baseURL: 'https://dummyjson.com'", "baseURL: import.meta.env.VITE_API_BASE_URL || 'https://dummyjson.com'")
    put(28,'src/pages/Catalog.jsx','''
    import { useRef } from 'react';
    import { useSearchParams } from 'react-router-dom';
    import { useDebounce } from '../hooks/useDebounce';
    import { useListProductsQuery, useGetCategoriesQuery } from '../features/products/productsApi';
    import ProductList from '../components/ProductList';
    export default function Catalog() {
      const [params, setParams] = useSearchParams(); const q = params.get('q') || '', category = params.get('category') || '';
      const candidate = Number(params.get('page') || 1), page = Number.isSafeInteger(candidate) && candidate > 0 ? Math.min(candidate, 10000) : 1;
      const search = useDebounce(q), inputRef = useRef(null), limit = 12;
      const { currentData: data, isFetching, isError, refetch } = useListProductsQuery({ q: search, category, skip: (page - 1) * limit, limit });
      const categories = useGetCategoriesQuery();
      function update(patch) { const next = new URLSearchParams(params); Object.entries(patch).forEach(([key, value]) => value ? next.set(key, String(value)) : next.delete(key)); setParams(next); }
      return <section><h1>Sản phẩm</h1><button onClick={() => inputRef.current?.focus()}>Focus tìm kiếm</button>
        <label>Tìm sản phẩm<input ref={inputRef} value={q} onChange={e => update({ q: e.target.value, category: '', page: 1 })} /></label>
        <label>Danh mục<select value={category} onChange={e => update({ category: e.target.value, q: '', page: 1 })}><option value="">Tất cả</option>
          {categories.data?.map(c => <option key={c.slug} value={c.slug}>{c.name}</option>)}
        </select></label><p>Tìm tên và chọn danh mục là hai chế độ riêng.</p>
        {categories.isError && <p role="alert">Không tải được danh mục; vẫn có thể tìm theo tên.</p>}
        {isFetching && <p role="status">Đang cập nhật...</p>}
        {isError ? <p role="alert">Không tải được sản phẩm.<button disabled={isFetching} onClick={refetch}>Thử lại</button></p> : !data ? <p>Chưa có dữ liệu.</p> : <>
          <ProductList products={data.products} /><nav aria-label="Phân trang"><button disabled={page === 1 || isFetching} onClick={() => update({ page: page - 1 })}>Trang trước</button>
          <span>Trang {page}</span><button disabled={page * limit >= data.total || isFetching} onClick={() => update({ page: page + 1 })}>Trang sau</button></nav>
        </>}
      </section>;
    }
    ''');snap(28)
    put(29,'src/components/RouteFocus.jsx','''
    import { useEffect } from 'react';
    import { useLocation } from 'react-router-dom';
    export default function RouteFocus() { const { pathname } = useLocation(); useEffect(() => { document.getElementById('main-content')?.focus(); window.scrollTo(0, 0); }, [pathname]); return null; }
    ''')
    change(29,'src/App.jsx',"import Layout", "import RouteFocus from './components/RouteFocus';\nimport Layout")
    change(29,'src/App.jsx','<BrowserRouter>','<BrowserRouter><RouteFocus />')
    change(29,'src/components/Layout.jsx','<><Header />','<><a href="#main-content">Đến nội dung chính</a><Header />')
    change(29,'src/components/Layout.jsx','id="main-content"','id="main-content" tabIndex={-1}')
    put(29,'ACCEPTANCE.md','''
    # Kiểm tra cửa hàng

    Ghi PASS/FAIL, trình duyệt và cách tái hiện. Không đánh dấu đạt khi chưa chạy.

    - Catalog: tìm kiếm, danh mục, phân trang, Back/Forward đúng URL.
    - Chi tiết: ID hợp lệ có dữ liệu, ID không tồn tại có lỗi, menu còn hoạt động.
    - Giỏ: thêm trùng không vượt stock, tổng đúng, giảm không âm, xóa hết có empty state.
    - Auth: guest không checkout, login trở lại đích, logout không thấy dữ liệu user trước.
    - Đơn: form sai không tạo đơn, lưu thất bại không xóa giỏ, giá đơn cũ không thay đổi theo catalog.
    - Responsive: 375px không tràn ngang, keyboard tới được mọi nút, focus nhìn thấy.
    - Offline: có lỗi và thử lại được, không trắng trang.
    ''');snap(29)
    put(30,'vercel.json','{ "rewrites": [{ "source": "/((?!assets/).*)", "destination": "/index.html" }] }')
    put(30,'README.md','''
    # React Shop

    Dự án học React: catalog, chi tiết, lọc, giỏ, đăng nhập demo và checkout cục bộ.

    ## Chạy
    Dùng Node.js 24 LTS hoặc 22 LTS từ 22.12. Có lockfile thì chạy npm ci, sau đó npm run dev.

    ## Kiểm tra
    Chạy npm run build rồi npm run preview; kiểm tra các luồng trong ACCEPTANCE.md. Build không thay kiểm tra API live và trình duyệt.

    ## Cấu hình
    Sao chép .env.example thành .env.local khi cần đổi API. VITE_API_BASE_URL là địa chỉ công khai, không chứa secret. Giữ .env.local ngoài Git.

    ## Giới hạn
    DummyJSON là API thử nghiệm. Giỏ và đơn lưu cục bộ, không đồng bộ thiết bị, không thanh toán thật. Protected route frontend không thay phân quyền backend. Chỉ dùng thông tin mẫu.

    ## Deploy
    Vercel: preset Vite, build npm run build, output dist. Giữ vercel.json cho SPA fallback. Sau deploy thử URL /products/1 và /checkout trực tiếp.

    ## Kết quả thực tế
    Người học bổ sung URL deploy, ảnh chụp và kết quả kiểm tra sau khi tự thực hiện, không ghi trước thành công.
    ''')
    CMDS[30]='npm run build\nnpm run preview';snap(30)
