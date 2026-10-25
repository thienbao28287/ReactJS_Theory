from pathlib import Path
import json, re, textwrap

ROOT=Path(__file__).resolve().parents[2]
TEMP=ROOT/'tmp'/'course30'
FILES={}; CHANGES={}; REMOVED={}; NOTES={}; CMDS={}
def put(day,path,text):
    FILES[path]=textwrap.dedent(text).strip()+'\n'
    CHANGES.setdefault(day,{})[path]=FILES[path]
def change(day,path,old,new):
    text=FILES[path]
    if old not in text:
        pattern=r'\n\s*'.join(re.escape(x.strip()) for x in old.splitlines())
        text,count=re.subn(pattern,lambda _:new,text)
        assert count,(day,path,old[:60])
    else: text=text.replace(old,new)
    put(day,path,text)
def remove(day,path):
    FILES.pop(path); REMOVED.setdefault(day,[]).append(path)
def package(day,deps=None,dev=None):
    p=json.loads(FILES['package.json'])
    p['dependencies'].update(deps or {}); p['devDependencies'].update(dev or {})
    put(day,'package.json',json.dumps(p,ensure_ascii=False,indent=2))
    CMDS[day]='npm install\nnpm run dev'
def snap(day):
    base=TEMP/'checkpoints'/f'lesson{day:02d}'
    for path,text in FILES.items():
        target=base/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text,encoding='utf-8')
def routes(day,imports='',extra=''):
    put(day,'src/App.jsx',f'''
    import {{ BrowserRouter, Route, Routes }} from 'react-router-dom';
    import Layout from './components/Layout';
    import Catalog from './pages/Catalog';
    import ProductDetail from './pages/ProductDetail';
    import Home from './pages/Home';
    {imports}
    export default function App() {{
      return <BrowserRouter><Routes><Route element={{<Layout />}}>
        <Route index element={{<Home />}} />
        <Route path="products" element={{<Catalog />}} />
        <Route path="about" element={{<h1>Về cửa hàng</h1>}} />
        <Route path="products/:id" element={{<ProductDetail />}} />
        {extra}
        <Route path="*" element={{<h1>404 Không tìm thấy trang</h1>}} />
      </Route></Routes></BrowserRouter>;
    }}
    ''')

def early():
    put(1,'package.json',json.dumps({'name':'react-shop','private':True,'version':'1.0.0','type':'module','scripts':{'dev':'vite','build':'vite build','preview':'vite preview'},'dependencies':{'react':'19.2.0','react-dom':'19.2.0'},'devDependencies':{'vite':'7.2.2','@vitejs/plugin-react':'5.1.0'}},indent=2))
    put(1,'index.html','''
    <!doctype html>
    <html lang="vi"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>React Shop</title></head><body><div id="root"></div><script type="module" src="/src/main.jsx"></script></body></html>
    ''')
    put(1,'vite.config.js',"import { defineConfig } from 'vite';\nimport react from '@vitejs/plugin-react';\nexport default defineConfig({ plugins: [react()] });")
    put(1,'src/main.jsx',"import { StrictMode } from 'react';\nimport { createRoot } from 'react-dom/client';\nimport App from './App';\nimport './index.css';\ncreateRoot(document.getElementById('root')).render(<StrictMode><App /></StrictMode>);")
    put(1,'src/index.css','body { margin: 0; font-family: system-ui, sans-serif; }\nmain, header, footer { padding: 20px; }\nbutton, input, select { font: inherit; margin: 4px; }')
    put(1,'src/App.jsx',"export default function App() { return <main><h1>React Shop</h1><p>Cửa hàng thực hành đã chạy.</p></main>; }")
    put(1,'.gitignore','node_modules/\ndist/\n.env\n.env.local\ncoverage/\n')
    CMDS[1]='npm install\nnpm run dev';snap(1)
    put(2,'src/components/Header.jsx',"export default function Header() { return <header><strong>React Shop</strong><p>Mua sắm có lựa chọn</p></header>; }")
    put(2,'src/components/Footer.jsx',"export default function Footer() { return <footer>Website học tập · Không thanh toán thật</footer>; }")
    put(2,'src/components/Banner.jsx',"export default function Banner() { return <section><h2>Khám phá bộ sưu tập</h2><p>Sản phẩm làm đẹp, đồ gia dụng và thực phẩm.</p></section>; }")
    put(2,'src/App.jsx',"import Header from './components/Header';\nimport Footer from './components/Footer';\nimport Banner from './components/Banner';\nexport default function App() { return <><Header /><main><h1>Trang chủ</h1><Banner /></main><Footer /></>; }");snap(2)
    put(3,'src/components/ProductCard.jsx','''
    export default function ProductCard({ product, children }) {
      return <article><h2>{product.title}</h2><p>{product.price} USD</p>{children}</article>;
    }
    ''')
    put(3,'src/pages/Catalog.jsx','''
    import ProductCard from '../components/ProductCard';
    export default function Catalog() {
      return <section><h1>Sản phẩm</h1>
        <ProductCard product={{ id: 1, title: 'Cà phê', price: 12 }}><p>Giao hàng minh họa</p></ProductCard>
        <ProductCard product={{ id: 2, title: 'Trà', price: 8 }} />
      </section>;
    }
    ''')
    put(3,'src/App.jsx',"import Header from './components/Header';\nimport Footer from './components/Footer';\nimport Catalog from './pages/Catalog';\nexport default function App() { return <><Header /><main><Catalog /></main><Footer /></>; }");snap(3)
    put(4,'src/components/QuantityPicker.jsx','''
    export default function QuantityPicker({ value, max, onChange }) {
      return <div><button type="button" disabled={value <= 1} onClick={() => onChange(value - 1)}>Giảm số lượng</button>
        <output aria-live="polite">{value}</output>
        <button type="button" disabled={value >= max} onClick={() => onChange(value + 1)}>Tăng số lượng</button></div>;
    }
    ''')
    put(4,'src/pages/Catalog.jsx','''
    import { useState } from 'react';
    import QuantityPicker from '../components/QuantityPicker';
    import ProductCard from '../components/ProductCard';
    export default function Catalog() {
      const [query, setQuery] = useState(''); const [quantity, setQuantity] = useState(1);
      return <section><h1>Sản phẩm</h1><label>Từ khóa<input value={query} onChange={e => setQuery(e.target.value)} /></label>
        <p>Bạn đang nhập: {query}</p><ProductCard product={{ id: 1, title: 'Cà phê', price: 12 }}>
        <QuantityPicker value={quantity} max={5} onChange={setQuantity} /></ProductCard>
      </section>;
    }
    ''');snap(4)
    put(5,'src/data/products.js',"export const products = [{ id: 1, title: 'Cà phê', price: 12, stock: 5, discountPercentage: 0 }, { id: 2, title: 'Trà', price: 8, stock: 0, discountPercentage: 10 }, { id: 3, title: 'Bánh', price: 4, stock: 3, discountPercentage: 0 }];")
    put(5,'src/components/ProductList.jsx','''
    import { useState } from 'react';
    import ProductCard from './ProductCard';
    export default function ProductList({ products }) {
      const [favorites, setFavorites] = useState([]);
      function toggle(id) { setFavorites(ids => ids.includes(id) ? ids.filter(x => x !== id) : [...ids, id]); }
      if (!products.length) return <p>Không có sản phẩm phù hợp.</p>;
      return <div className="product-grid">{products.map(product => <ProductCard key={product.id} product={product}>
        <p>{product.stock > 0 ? `Còn ${product.stock} sản phẩm` : 'Hết hàng'}</p>
        <button aria-pressed={favorites.includes(product.id)} onClick={() => toggle(product.id)}>{favorites.includes(product.id) ? 'Bỏ yêu thích' : 'Yêu thích'}</button>
      </ProductCard>)}</div>;
    }
    ''')
    put(5,'src/pages/Catalog.jsx','''
    import { useState } from 'react';
    import { products } from '../data/products';
    import ProductList from '../components/ProductList';
    export default function Catalog() {
      const [query, setQuery] = useState('');
      const visible = products.filter(p => p.title.toLocaleLowerCase('vi').includes(query.trim().toLocaleLowerCase('vi')));
      return <section><h1>Sản phẩm</h1><label>Tìm sản phẩm<input value={query} onChange={e => setQuery(e.target.value)} /></label><ProductList products={visible} /></section>;
    }
    ''');snap(5)
    put(6,'src/index.css','''
    * { box-sizing: border-box; }
    body { margin: 0; font-family: system-ui, sans-serif; background: #f5f7fa; color: #172033; line-height: 1.6; }
    main, header, footer { max-width: 1100px; margin: auto; padding: 20px; }
    header { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px; border-bottom: 1px solid #ccd5e0; }
    button, input, select { font: inherit; margin: 4px; padding: 8px 12px; max-width: 100%; }
    button { cursor: pointer; border: 1px solid #8090a5; border-radius: 6px; background: white; }
    button:disabled { opacity: .5; cursor: not-allowed; }
    a { color: #174cb4; }
    :focus-visible { outline: 3px solid #2563eb; outline-offset: 3px; }
    .product-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
    .product-grid article { padding: 16px; border: 1px solid #d6dde6; border-radius: 10px; background: white; min-width: 0; }
    img { max-width: 100%; object-fit: contain; }
    form { max-width: 560px; }
    label { display: block; }
    nav { display: flex; flex-wrap: wrap; align-items: center; gap: 12px; }
    @media (max-width: 700px) { .product-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    @media (max-width: 430px) { .product-grid { grid-template-columns: 1fr; } }
    ''');snap(6)
    put(7,'src/components/ProductCard.module.css','''
    .card { display: flex; flex-direction: column; gap: 8px; padding: 16px; background: white; border: 1px solid #d6dde6; border-radius: 10px; }
    .title { font-size: 1.15rem; margin: 0; }
    .price { font-weight: 600; color: #174cb4; }
    .image { width: 100%; height: 160px; object-fit: contain; }
    ''')
    put(7,'src/components/ProductCard.jsx','''
    import styles from './ProductCard.module.css';
    export default function ProductCard({ product, children }) {
      return <article className={styles.card}><h2 className={styles.title}>{product.title}</h2>
        {product.thumbnail && <img className={styles.image} src={product.thumbnail} alt={product.title} width="240" height="160" loading="lazy" />}
        <p className={styles.price}>{product.price} USD</p>{children}</article>;
    }
    ''');snap(7)
    change(8,'src/pages/Catalog.jsx',"import { products }", "import { useEffect } from 'react';\nimport { products }")
    change(8,'src/pages/Catalog.jsx',"const [query, setQuery] = useState('');", "const [query, setQuery] = useState('');\n  useEffect(() => { const previous = document.title; document.title = query ? `Tìm: ${query}` : 'React Shop'; return () => { document.title = previous; }; }, [query]);\n  useEffect(() => { const handler = () => console.log('Chiều rộng:', window.innerWidth); window.addEventListener('resize', handler); return () => window.removeEventListener('resize', handler); }, []);")
    snap(8)
    put(9,'src/pages/Catalog.jsx','''
    import { useEffect, useState } from 'react';
    import ProductList from '../components/ProductList';
    export default function Catalog() {
      const [products, setProducts] = useState([]); const [status, setStatus] = useState('loading');
      useEffect(() => {
        const c = new AbortController();
        async function load() {
          try {
            const r = await fetch('https://dummyjson.com/products?limit=12', { signal: c.signal });
            if (!r.ok) throw new Error(`HTTP ${r.status}`);
            const data = await r.json();
            if (!Array.isArray(data.products)) throw new Error('Sai cấu trúc dữ liệu');
            if (!c.signal.aborted) { setProducts(data.products); setStatus('success'); }
          } catch { if (!c.signal.aborted) setStatus('error'); }
        }
        load(); return () => c.abort();
      }, []);
      if (status === 'loading') return <p role="status">Đang tải sản phẩm...</p>;
      if (status === 'error') return <p role="alert">Không tải được sản phẩm. Hãy tải lại trang.</p>;
      return <section><h1>Sản phẩm</h1><ProductList products={products} /></section>;
    }
    ''');snap(9)
    package(10,{'react-router-dom':'6.30.1'})
    put(10,'src/components/Layout.jsx',"import { Outlet } from 'react-router-dom';\nimport Header from './Header';\nimport Footer from './Footer';\nexport default function Layout() { return <><Header /><main id=\"main-content\"><Outlet /></main><Footer /></>; }")
    put(10,'src/components/Header.jsx',"import { NavLink } from 'react-router-dom';\nexport default function Header() { return <header><strong>React Shop</strong><nav aria-label=\"Chính\"><NavLink to=\"/\" end>Trang chủ</NavLink><NavLink to=\"/products\">Sản phẩm</NavLink><NavLink to=\"/about\">Giới thiệu</NavLink></nav></header>; }")
    put(10,'src/pages/Home.jsx',"import { useNavigate } from 'react-router-dom';\nimport Banner from '../components/Banner';\nexport default function Home() { const navigate = useNavigate(); return <><h1>React Shop</h1><Banner /><button onClick={() => navigate('/products')}>Khám phá sản phẩm</button></>; }")
    put(10,'src/App.jsx',"import { BrowserRouter, Routes, Route } from 'react-router-dom';\nimport Layout from './components/Layout';\nimport Home from './pages/Home';\nimport Catalog from './pages/Catalog';\nexport default function App() { return <BrowserRouter><Routes><Route element={<Layout />}><Route index element={<Home />} /><Route path=\"products\" element={<Catalog />} /><Route path=\"about\" element={<h1>Về cửa hàng</h1>} /></Route></Routes></BrowserRouter>; }");snap(10)
    change(11,'src/components/ProductCard.jsx',"import styles", "import { Link } from 'react-router-dom';\nimport styles")
    change(11,'src/components/ProductCard.jsx','{product.title}</h2>','<Link to={`/products/${product.id}`}>{product.title}</Link></h2>')
    put(11,'src/pages/ProductDetail.jsx','''
    import { useEffect, useState } from 'react';
    import { useParams } from 'react-router-dom';
    export default function ProductDetail() {
      const { id } = useParams(); const [state, setState] = useState({ data: null, error: '' });
      useEffect(() => {
        const c = new AbortController(); setState({ data: null, error: '' });
        async function load() {
          try { const r = await fetch(`https://dummyjson.com/products/${encodeURIComponent(id)}`, { signal: c.signal });
            if (!r.ok) throw new Error('Không tìm thấy hoặc không tải được sản phẩm');
            const data = await r.json(); if (!c.signal.aborted) setState({ data, error: '' });
          } catch (err) { if (!c.signal.aborted) setState({ data: null, error: err.message }); }
        }
        load(); return () => c.abort();
      }, [id]);
      if (state.error) return <p role="alert">{state.error}</p>;
      if (!state.data) return <p role="status">Đang tải chi tiết...</p>;
      const p = state.data;
      return <article><h1>{p.title}</h1><img src={p.thumbnail} alt={p.title} width="240" height="240" /><p>{p.description}</p><p>{p.price} USD</p></article>;
    }
    ''')
    put(11,'src/pages/Catalog.jsx','''
    import { useEffect, useState } from 'react';
    import { useLocation, useSearchParams } from 'react-router-dom';
    import ProductList from '../components/ProductList';
    export default function Catalog() {
      const [params, setParams] = useSearchParams(); const q = params.get('q') || '';
      const location = useLocation(); const [state, setState] = useState({ data: null, error: '' });
      useEffect(() => {
        const c = new AbortController(); setState({ data: null, error: '' });
        async function load() {
          try { const r = await fetch(`https://dummyjson.com/products/search?q=${encodeURIComponent(q)}&limit=12`, { signal: c.signal });
            if (!r.ok) throw new Error('Không tải được sản phẩm');
            const data = await r.json(); if (!c.signal.aborted) setState({ data, error: '' });
          } catch (err) { if (!c.signal.aborted) setState({ data: null, error: err.message }); }
        }
        load(); return () => c.abort();
      }, [q]);
      return <section><h1>Sản phẩm</h1><label>Tìm sản phẩm<input value={q} onChange={e => { const next = new URLSearchParams(params); next.set('q', e.target.value); setParams(next); }} /></label>
        <p>URL: {location.pathname}{location.search}</p>
        {state.error ? <p role="alert">{state.error}</p> : !state.data ? <p role="status">Đang tải...</p> : <ProductList products={state.data.products} />}
      </section>;
    }
    ''')
    routes(11);snap(11)
    package(12,{'axios':'1.13.2'})
    put(12,'src/services/http.js',"import axios from 'axios';\nexport const http = axios.create({ baseURL: 'https://dummyjson.com', timeout: 8000 });")
    put(12,'src/services/products.js','''
    import { http } from './http';
    export const productService = {
      list: ({ q = '', limit = 12, skip = 0, signal } = {}) => http.get('/products/search', { params: { q, limit, skip }, signal }).then(response => response.data),
      detail: (id, signal) => http.get(`/products/${encodeURIComponent(id)}`, { signal }).then(response => response.data),
    };
    ''')
    change(12,'src/pages/Catalog.jsx',"import ProductList", "import { productService } from '../services/products';\nimport ProductList")
    change(12,'src/pages/Catalog.jsx',"const r = await fetch(`https://dummyjson.com/products/search?q=${encodeURIComponent(q)}&limit=12`, { signal: c.signal });\n            if (!r.ok) throw new Error('Không tải được sản phẩm');\n            const data = await r.json();", "const data = await productService.list({ q, signal: c.signal });")
    change(12,'src/pages/ProductDetail.jsx',"import { useParams }", "import { productService } from '../services/products';\nimport { useParams }")
    change(12,'src/pages/ProductDetail.jsx',"const r = await fetch(`https://dummyjson.com/products/${encodeURIComponent(id)}`, { signal: c.signal });\n            if (!r.ok) throw new Error('Không tìm thấy hoặc không tải được sản phẩm');\n            const data = await r.json();", "const data = await productService.detail(id, c.signal);")
    snap(12)
    put(13,'src/services/http.js','''
    import axios from 'axios';
    export const http = axios.create({ baseURL: 'https://dummyjson.com', timeout: 8000 });
    http.interceptors.response.use(response => response.data, error => Promise.reject(error));
    export function requestMessage(error) {
      if (error.code === 'ECONNABORTED') return 'Máy chủ phản hồi quá chậm. Hãy thử lại.';
      if (error.response?.status === 404) return 'Không tìm thấy dữ liệu.';
      return 'Không tải được dữ liệu. Kiểm tra kết nối và thử lại.';
    }
    ''')
    change(13,'src/services/products.js','.then(response => response.data)','')
    change(13,'src/pages/Catalog.jsx',"import { productService }", "import { requestMessage } from '../services/http';\nimport { productService }")
    change(13,'src/pages/Catalog.jsx',"const location = useLocation();", "const [retry, setRetry] = useState(0);\n  const location = useLocation();")
    change(13,'src/pages/Catalog.jsx','error: err.message','error: requestMessage(err)')
    change(13,'src/pages/Catalog.jsx','}, [q]);','}, [q, retry]);')
    change(13,'src/pages/Catalog.jsx','<p role="alert">{state.error}</p>','<p role="alert">{state.error}<button onClick={() => setRetry(n => n + 1)}>Thử lại</button></p>')
    snap(13)
    change(14,'src/pages/Catalog.jsx',"import { useEffect, useState }", "import { useEffect, useRef, useState }")
    change(14,'src/pages/Catalog.jsx',"const [params, setParams]", "const inputRef = useRef(null);\n  const [params, setParams]")
    change(14,'src/pages/Catalog.jsx','<label>Tìm sản phẩm<input','<button onClick={() => inputRef.current?.focus()}>Focus tìm kiếm</button><label>Tìm sản phẩm<input ref={inputRef}')
    snap(14)
    put(15,'src/hooks/useToggle.js',"import { useState } from 'react';\nexport function useToggle(initial = false) { const [open, setOpen] = useState(initial); return [open, () => setOpen(v => !v)]; }")
    put(15,'src/hooks/useDebounce.js',"import { useEffect, useState } from 'react';\nexport function useDebounce(value, delay = 400) { const [result, setResult] = useState(value); useEffect(() => { const id = setTimeout(() => setResult(value), delay); return () => clearTimeout(id); }, [value, delay]); return result; }")
    put(15,'src/hooks/useProducts.js','''
    import { useEffect, useState } from 'react';
    import { productService } from '../services/products';
    import { requestMessage } from '../services/http';
    export function useProducts(q) {
      const [state, setState] = useState({ data: null, error: '' }); const [attempt, setAttempt] = useState(0);
      useEffect(() => { const c = new AbortController(); setState({ data: null, error: '' });
        productService.list({ q, signal: c.signal }).then(data => { if (!c.signal.aborted) setState({ data, error: '' }); })
          .catch(error => { if (!c.signal.aborted) setState({ data: null, error: requestMessage(error) }); });
        return () => c.abort();
      }, [q, attempt]);
      return { ...state, retry: () => setAttempt(n => n + 1) };
    }
    ''')
    put(15,'src/pages/Catalog.jsx','''
    import { useRef } from 'react';
    import { useSearchParams } from 'react-router-dom';
    import { useToggle } from '../hooks/useToggle';
    import { useDebounce } from '../hooks/useDebounce';
    import { useProducts } from '../hooks/useProducts';
    import ProductList from '../components/ProductList';
    export default function Catalog() {
      const [params, setParams] = useSearchParams(); const q = params.get('q') || '';
      const inputRef = useRef(null); const [open, toggle] = useToggle();
      const debounced = useDebounce(q); const { data, error, retry } = useProducts(debounced);
      return <section><h1>Sản phẩm</h1><button onClick={() => inputRef.current?.focus()}>Focus tìm kiếm</button>
        <label>Tìm sản phẩm<input ref={inputRef} value={q} onChange={e => setParams({ q: e.target.value })} /></label>
        <button onClick={toggle} aria-expanded={open}>Gợi ý tìm kiếm</button>{open && <p>Dữ liệu API dùng tên tiếng Anh, ví dụ phone.</p>}
        {error ? <p role="alert">{error}<button onClick={retry}>Thử lại</button></p> : !data ? <p role="status">Đang tải...</p> : <ProductList products={data.products} />}
      </section>;
    }
    ''');snap(15)
    package(16,{'react-hook-form':'7.66.0'})
    put(16,'src/components/ShippingForm.jsx','''
    import { useState } from 'react';
    import { useForm } from 'react-hook-form';
    export default function ShippingForm({ onSubmit }) {
      const [message, setMessage] = useState('');
      const { register, handleSubmit, watch, reset, setValue, formState: { errors, isSubmitting } } = useForm({ defaultValues: { name: '', phone: '', address: '' } });
      async function submit(values) { setMessage(''); if (onSubmit) await onSubmit(values); else setMessage('Đã nhận thông tin thử nghiệm, chưa đặt hàng.'); }
      return <form onSubmit={handleSubmit(submit)} noValidate><h2>Thông tin giao hàng</h2>
        <label htmlFor="name">Họ tên</label><input id="name" {...register('name', { required: 'Cần nhập tên' })} />{errors.name && <p role="alert">{errors.name.message}</p>}
        <label htmlFor="phone">Số điện thoại</label><input id="phone" {...register('phone', { required: 'Cần nhập số điện thoại' })} />{errors.phone && <p role="alert">{errors.phone.message}</p>}
        <label htmlFor="address">Địa chỉ</label><input id="address" {...register('address', { required: 'Cần nhập địa chỉ' })} />{errors.address && <p role="alert">{errors.address.message}</p>}
        <p>Người nhận: {watch('name')}</p><button type="button" onClick={() => setValue('address', '123 đường thử nghiệm', { shouldDirty: true, shouldValidate: true })}>Địa chỉ mẫu</button>
        <button type="button" onClick={() => { reset(); setMessage(''); }}>Nhập lại</button><button disabled={isSubmitting}>Xác nhận</button>
        {message && <p role="status">{message}</p>}
      </form>;
    }
    ''')
    routes(16,"import ShippingForm from './components/ShippingForm';",'<Route path="shipping" element={<ShippingForm />} />')
    change(16,'src/components/Header.jsx','</nav>',"<NavLink to=\"/shipping\">Giao hàng</NavLink></nav>");snap(16)
    package(17,{'zod':'4.1.12','@hookform/resolvers':'5.2.2'})
    put(17,'src/schemas/shipping.js','''
    import { z } from 'zod';
    export const shippingSchema = z.object({
      name: z.string().trim().min(2, 'Tên cần ít nhất 2 ký tự'),
      phone: z.string().regex(/^0[0-9]{9}$/, 'Số điện thoại phải có 10 chữ số, bắt đầu bằng 0'),
      address: z.string().trim().min(10, 'Địa chỉ cần ít nhất 10 ký tự'),
    });
    ''')
    put(17,'src/components/ShippingForm.jsx','''
    import { useState } from 'react';
    import { useForm } from 'react-hook-form';
    import { zodResolver } from '@hookform/resolvers/zod';
    import { shippingSchema } from '../schemas/shipping';
    export default function ShippingForm({ onSubmit }) {
      const [message, setMessage] = useState('');
      const form = useForm({ resolver: zodResolver(shippingSchema), defaultValues: { name: '', phone: '', address: '' } });
      async function submit(values) {
        setMessage('');
        try { if (onSubmit) await onSubmit(values); else setMessage('Thông tin hợp lệ. Chưa tạo đơn hàng.'); }
        catch { form.setError('root', { message: 'Không lưu được dữ liệu. Hãy thử lại.' }); }
      }
      const labels = { name: 'Họ tên', phone: 'Số điện thoại', address: 'Địa chỉ' };
      return <form onSubmit={form.handleSubmit(submit)} noValidate><h2>Thông tin giao hàng</h2>
        {Object.keys(labels).map(field => <div key={field}><label htmlFor={field}>{labels[field]}</label>
          <input id={field} {...form.register(field)} aria-invalid={!!form.formState.errors[field]} aria-describedby={form.formState.errors[field] ? `${field}-error` : undefined} />
          {form.formState.errors[field] && <p id={`${field}-error`} role="alert">{form.formState.errors[field].message}</p>}
        </div>)}
        <p>Người nhận: {form.watch('name')}</p><button type="button" onClick={() => form.setValue('address', '123 đường thử nghiệm', { shouldValidate: true })}>Địa chỉ mẫu</button>
        <button type="button" onClick={() => { form.reset(); setMessage(''); }}>Nhập lại</button><button disabled={form.formState.isSubmitting}>{form.formState.isSubmitting ? 'Đang xử lý...' : 'Xác nhận'}</button>
        {form.formState.errors.root && <p role="alert">{form.formState.errors.root.message}</p>}{message && <p role="status">{message}</p>}
      </form>;
    }
    ''');snap(17)
