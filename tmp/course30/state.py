from project import *

def state_lessons():
    put(18,'src/cart/reducer.js','''
    export function cartReducer(items, action) {
      switch (action.type) {
        case 'add': {
          const p = action.product;
          if (!p || !Number.isInteger(p.id) || !Number.isFinite(p.price) || p.price < 0 || !Number.isInteger(p.stock) || p.stock <= 0) return items;
          const exists = items.find(item => item.id === p.id);
          if (exists) return items.map(item => item.id === p.id ? { ...item, quantity: Math.min(item.quantity + 1, item.stock) } : item);
          return [...items, { id: p.id, title: p.title, price: p.price, stock: p.stock, quantity: 1 }];
        }
        case 'quantity':
          if (!Number.isInteger(action.quantity) || action.quantity < 1) return items;
          return items.map(item => item.id === action.id ? { ...item, quantity: Math.min(action.quantity, item.stock) } : item);
        case 'remove': return items.filter(item => item.id !== action.id);
        case 'clear': return [];
        case 'replace': return action.items;
        default: return items;
      }
    }
    export const totalCents = items => items.reduce((sum, item) => sum + Math.round(item.price * 100) * item.quantity, 0);
    ''')
    put(18,'src/pages/Cart.jsx','''
    import { useReducer } from 'react';
    import { cartReducer, totalCents } from '../cart/reducer';
    import QuantityPicker from '../components/QuantityPicker';
    const sample = { id: 100, title: 'Sản phẩm thử reducer', price: 1.1, stock: 3 };
    export default function Cart() {
      const [items, dispatch] = useReducer(cartReducer, []);
      return <section><h1>Giỏ hàng cục bộ</h1><button onClick={() => dispatch({ type: 'add', product: sample })}>Thêm sản phẩm thử</button>
        {!items.length && <p>Giỏ hàng rỗng.</p>}<ul>{items.map(item => <li key={item.id}>{item.title}
          <QuantityPicker value={item.quantity} max={item.stock} onChange={quantity => dispatch({ type: 'quantity', id: item.id, quantity })} />
          <button onClick={() => dispatch({ type: 'remove', id: item.id })}>Xóa</button></li>)}</ul>
        <p>Tổng: {(totalCents(items) / 100).toFixed(2)} USD</p>
      </section>;
    }
    ''')
    routes(18,"import ShippingForm from './components/ShippingForm';\nimport Cart from './pages/Cart';",'<Route path="shipping" element={<ShippingForm />} /><Route path="cart" element={<Cart />} />')
    change(18,'src/components/Header.jsx','</nav>','<NavLink to="/cart">Giỏ hàng</NavLink></nav>');snap(18)
    put(19,'src/cart/CartContext.jsx','''
    import { createContext, useContext, useReducer } from 'react';
    import { cartReducer, totalCents } from './reducer';
    const CartContext = createContext(null);
    export function CartProvider({ children }) {
      const [items, dispatch] = useReducer(cartReducer, []);
      const value = { items, count: items.reduce((n, item) => n + item.quantity, 0), total: totalCents(items) / 100,
        add: product => dispatch({ type: 'add', product }), remove: id => dispatch({ type: 'remove', id }),
        setQuantity: (id, quantity) => dispatch({ type: 'quantity', id, quantity }), clear: () => dispatch({ type: 'clear' }) };
      return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
    }
    export function useCart() { const cart = useContext(CartContext); if (!cart) throw new Error('Thiếu CartProvider'); return cart; }
    ''')
    put(19,'src/main.jsx',"import { StrictMode } from 'react';\nimport { createRoot } from 'react-dom/client';\nimport App from './App';\nimport { CartProvider } from './cart/CartContext';\nimport './index.css';\ncreateRoot(document.getElementById('root')).render(<StrictMode><CartProvider><App /></CartProvider></StrictMode>);")
    put(19,'src/pages/Cart.jsx','''
    import { Link } from 'react-router-dom';
    import { useCart } from '../cart/CartContext';
    import QuantityPicker from '../components/QuantityPicker';
    export default function Cart() {
      const cart = useCart();
      if (!cart.items.length) return <section><h1>Giỏ hàng</h1><p>Giỏ hàng rỗng.</p><Link to="/products">Chọn sản phẩm</Link></section>;
      return <section><h1>Giỏ hàng</h1><ul>{cart.items.map(item => <li key={item.id}><h2>{item.title}</h2><p>{item.price} USD</p>
        <QuantityPicker value={item.quantity} max={item.stock} onChange={quantity => cart.setQuantity(item.id, quantity)} />
        <button onClick={() => cart.remove(item.id)}>Xóa {item.title}</button></li>)}</ul>
        <p>Tổng: {cart.total.toFixed(2)} USD</p><Link to="/shipping">Thông tin giao hàng</Link>
      </section>;
    }
    ''')
    change(19,'src/components/ProductCard.jsx',"import styles", "import { useCart } from '../cart/CartContext';\nimport styles")
    change(19,'src/components/ProductCard.jsx','return <article','const cart = useCart();\n  return <article')
    change(19,'src/components/ProductCard.jsx','{children}</article>','<button disabled={product.stock <= 0} onClick={() => cart.add(product)}>Thêm vào giỏ</button>{children}</article>')
    change(19,'src/components/Header.jsx',"import { NavLink }", "import { useCart } from '../cart/CartContext';\nimport { NavLink }")
    change(19,'src/components/Header.jsx','return <header>','const cart = useCart(); return <header>')
    change(19,'src/components/Header.jsx','>Giỏ hàng</NavLink>','>Giỏ hàng ({cart.count})</NavLink>')
    snap(19)
    put(20,'src/auth/AuthContext.jsx','''
    import { createContext, useContext, useEffect, useState } from 'react';
    import { http } from '../services/http';
    const AuthContext = createContext(null);
    export function AuthProvider({ children }) {
      const [user, setUser] = useState(null); const [loading, setLoading] = useState(true);
      useEffect(() => {
        const c = new AbortController();
        async function restore() {
          try { const token = sessionStorage.getItem('shop:token');
            if (token) { const me = await http.get('/auth/me', { signal: c.signal }); if (!c.signal.aborted) setUser(me); }
          } catch { if (!c.signal.aborted) { sessionStorage.removeItem('shop:token'); setUser(null); } }
          finally { if (!c.signal.aborted) setLoading(false); }
        }
        restore(); return () => c.abort();
      }, []);
      useEffect(() => {
        function expired() { sessionStorage.removeItem('shop:token'); setUser(null); }
        window.addEventListener('shop:unauthorized', expired); return () => window.removeEventListener('shop:unauthorized', expired);
      }, []);
      async function login(values) { const data = await http.post('/auth/login', { ...values, expiresInMins: 30 }); sessionStorage.setItem('shop:token', data.accessToken); setUser(data); }
      function logout() { sessionStorage.removeItem('shop:token'); setUser(null); }
      return <AuthContext.Provider value={{ user, loading, login, logout }}>{children}</AuthContext.Provider>;
    }
    export function useAuth() { const auth = useContext(AuthContext); if (!auth) throw new Error('Thiếu AuthProvider'); return auth; }
    ''')
    change(20,'src/services/http.js',"http.interceptors.response.use(response => response.data, error => Promise.reject(error));", "http.interceptors.request.use(config => { const token = sessionStorage.getItem('shop:token'); if (token) config.headers.Authorization = `Bearer ${token}`; return config; });\nhttp.interceptors.response.use(response => response.data, error => {\n  if (error.response?.status === 401 && error.config?.url !== '/auth/login') window.dispatchEvent(new Event('shop:unauthorized'));\n  return Promise.reject(error);\n});")
    put(20,'src/auth/ProtectedRoute.jsx','''
    import { Navigate, useLocation } from 'react-router-dom';
    import { useAuth } from './AuthContext';
    export default function ProtectedRoute({ children }) {
      const { user, loading } = useAuth(); const location = useLocation();
      if (loading) return <p role="status">Đang kiểm tra phiên...</p>;
      return user ? children : <Navigate to="/login" replace state={{ from: location.pathname + location.search }} />;
    }
    ''')
    put(20,'src/pages/Login.jsx','''
    import { useState } from 'react';
    import { Navigate, useLocation } from 'react-router-dom';
    import { useAuth } from '../auth/AuthContext';
    export default function Login() {
      const auth = useAuth(), location = useLocation();
      const [error, setError] = useState(''), [busy, setBusy] = useState(false);
      const from = typeof location.state?.from === 'string' && location.state.from.startsWith('/') && !location.state.from.startsWith('//') ? location.state.from : '/products';
      if (auth.loading) return <p role="status">Đang kiểm tra phiên...</p>;
      if (auth.user) return <Navigate to={from} replace />;
      async function submit(event) {
        event.preventDefault(); setBusy(true); setError('');
        const data = new FormData(event.currentTarget);
        try { await auth.login({ username: data.get('username'), password: data.get('password') }); }
        catch { setError('Đăng nhập thất bại. Kiểm tra tài khoản demo hoặc kết nối.'); }
        finally { setBusy(false); }
      }
      return <form onSubmit={submit}><h1>Đăng nhập thử nghiệm</h1>
        <label>Tên đăng nhập<input name="username" autoComplete="username" required /></label>
        <label>Mật khẩu<input type="password" name="password" autoComplete="current-password" required /></label>
        {error && <p role="alert">{error}</p>}<button disabled={busy}>{busy ? 'Đang đăng nhập...' : 'Đăng nhập'}</button>
      </form>;
    }
    ''')
    change(20,'src/main.jsx',"import App", "import { AuthProvider } from './auth/AuthContext';\nimport App")
    change(20,'src/main.jsx','<CartProvider><App /></CartProvider>','<AuthProvider><CartProvider><App /></CartProvider></AuthProvider>')
    # Memory cart resets explicitly on identity change; storage is added in lesson 21.
    change(20,'src/cart/CartContext.jsx',"createContext, useContext, useReducer", "createContext, useContext, useEffect, useReducer, useState")
    change(20,'src/cart/CartContext.jsx',"const CartContext", "import { useAuth } from '../auth/AuthContext';\nconst CartContext")
    change(20,'src/cart/CartContext.jsx','const [items, dispatch] = useReducer(cartReducer, []);',"const { user, loading } = useAuth();\n  const key = `shop:cart:${user?.id ?? 'guest'}`;\n  const [readyKey, setReadyKey] = useState(null);\n  const [items, dispatch] = useReducer(cartReducer, []);\n  useEffect(() => { if (!loading) { dispatch({ type: 'clear' }); setReadyKey(key); } }, [key, loading]);")
    change(20,'src/cart/CartContext.jsx','return <CartContext.Provider','if (loading || readyKey !== key) return <p role="status">Đang chuẩn bị giỏ hàng...</p>;\n  return <CartContext.Provider')
    change(20,'src/components/Header.jsx',"import { useCart }", "import { useAuth } from '../auth/AuthContext';\nimport { useCart }")
    change(20,'src/components/Header.jsx','const cart = useCart();','const cart = useCart(); const auth = useAuth();')
    change(20,'src/components/Header.jsx','</nav>','<NavLink to="/login">{auth.user ? auth.user.username : \'Đăng nhập\'}</NavLink>{auth.user && <button onClick={auth.logout}>Đăng xuất</button>}</nav>')
    imports="import Cart from './pages/Cart';\nimport ShippingForm from './components/ShippingForm';\nimport Login from './pages/Login';\nimport ProtectedRoute from './auth/ProtectedRoute';"
    extra='<Route path="cart" element={<Cart />} /><Route path="login" element={<Login />} /><Route path="shipping" element={<ProtectedRoute><ShippingForm /></ProtectedRoute>} />'
    routes(20,imports,extra);snap(20)
    put(21,'src/cart/storage.js','''
    export function readCart(key) {
      try {
        const value = JSON.parse(localStorage.getItem(key) || '[]');
        if (!Array.isArray(value)) return [];
        const seen = new Set();
        return value.filter(item => {
          const valid = item && Number.isInteger(item.id) && !seen.has(item.id) && typeof item.title === 'string'
            && Number.isFinite(item.price) && item.price >= 0 && Number.isInteger(item.stock) && item.stock > 0
            && Number.isInteger(item.quantity) && item.quantity >= 1 && item.quantity <= item.stock;
          if (valid) seen.add(item.id); return valid;
        });
      } catch { return []; }
    }
    export function writeCart(key, items) { try { localStorage.setItem(key, JSON.stringify(items)); return true; } catch { return false; } }
    ''')
    change(21,'src/cart/CartContext.jsx',"const CartContext", "import { readCart, writeCart } from './storage';\nconst CartContext")
    change(21,'src/cart/CartContext.jsx',"dispatch({ type: 'clear' }); setReadyKey(key);", "dispatch({ type: 'replace', items: readCart(key) }); setReadyKey(key);")
    change(21,'src/cart/CartContext.jsx',"const value = {", "const [saveFailed, setSaveFailed] = useState(false);\n  useEffect(() => { if (!loading && readyKey === key) setSaveFailed(!writeCart(key, items)); }, [items, key, readyKey, loading]);\n  const value = {")
    change(21,'src/cart/CartContext.jsx','{children}</CartContext.Provider>','{saveFailed && <p role="alert">Không lưu được giỏ; dữ liệu hiện chỉ nằm trong bộ nhớ.</p>}{children}</CartContext.Provider>')
    put(21,'src/services/orders.js','''
    const key = userId => `shop:orders:${userId}`;
    export function readOrders(userId) {
      try {
        const parsed = JSON.parse(localStorage.getItem(key(userId)) || '[]');
        if (!Array.isArray(parsed)) return [];
        return parsed.filter(order => order && order.userId === userId && typeof order.id === 'string'
          && Number.isFinite(order.total) && order.shipping && typeof order.shipping.name === 'string'
          && Array.isArray(order.items) && order.items.every(p => p && typeof p.title === 'string' && Number.isInteger(p.quantity) && p.quantity > 0 && Number.isFinite(p.price)));
      } catch { return []; }
    }
    export function placeOrder(userId, shipping, items) {
      if (!userId || !items.length) throw new Error('Cần đăng nhập và có sản phẩm');
      const order = { id: crypto.randomUUID(), userId, shipping: { ...shipping }, items: items.map(p => ({ ...p })), createdAt: new Date().toISOString(),
        total: items.reduce((sum, p) => sum + Math.round(p.price * 100) * p.quantity, 0) / 100 };
      localStorage.setItem(key(userId), JSON.stringify([order, ...readOrders(userId)]));
      return order;
    }
    ''')
    put(21,'src/pages/Checkout.jsx','''
    import { useRef } from 'react';
    import { Link, useNavigate } from 'react-router-dom';
    import { useAuth } from '../auth/AuthContext';
    import { useCart } from '../cart/CartContext';
    import { placeOrder } from '../services/orders';
    import ShippingForm from '../components/ShippingForm';
    export default function Checkout() {
      const { user } = useAuth(); const cart = useCart(); const navigate = useNavigate(); const locked = useRef(false);
      async function submit(values) {
        if (locked.current) return;
        locked.current = true;
        try { placeOrder(user.id, values, cart.items); cart.clear(); navigate('/orders', { replace: true }); }
        catch (error) { locked.current = false; throw error; }
      }
      if (!cart.items.length) return <p>Giỏ hàng rỗng. <Link to="/products">Chọn sản phẩm</Link></p>;
      return <section><h1>Checkout mô phỏng</h1><p>Tổng: {cart.total.toFixed(2)} USD. Chưa thanh toán thật.</p><ShippingForm onSubmit={submit} /></section>;
    }
    ''')
    put(21,'src/pages/Orders.jsx','''
    import { useAuth } from '../auth/AuthContext';
    import { readOrders } from '../services/orders';
    export default function Orders() {
      const { user } = useAuth(); const orders = readOrders(user.id);
      return <section><h1>Lịch sử đơn mô phỏng</h1>{!orders.length && <p>Chưa có đơn hàng.</p>}
        {orders.map(order => <details key={order.id}><summary>{order.id} · {order.total.toFixed(2)} USD</summary>
          <p>{order.shipping.name} · {order.shipping.address}</p><ul>{order.items.map(p => <li key={p.id}>{p.title} × {p.quantity} · {p.price} USD</li>)}</ul>
          <p>Thời điểm: {new Date(order.createdAt).toLocaleString('vi-VN')}</p>
        </details>)}
      </section>;
    }
    ''')
    routes(21,imports+"\nimport Checkout from './pages/Checkout';\nimport Orders from './pages/Orders';",extra+'<Route path="checkout" element={<ProtectedRoute><Checkout /></ProtectedRoute>} /><Route path="orders" element={<ProtectedRoute><Orders /></ProtectedRoute>} />')
    change(21,'src/pages/Cart.jsx','to="/shipping"','to="/checkout"')
    change(21,'src/components/Header.jsx','</nav>','<NavLink to="/orders">Đơn hàng</NavLink></nav>');snap(21)
    package(22,{'@reduxjs/toolkit':'2.11.0','react-redux':'9.2.0'})
    put(22,'src/cart/slice.js','''
    import { createSlice } from '@reduxjs/toolkit';
    import { cartReducer, totalCents } from './reducer';
    const slice = createSlice({ name: 'cart', initialState: [], reducers: {
      add: (state, action) => cartReducer(state, { type: 'add', product: action.payload }),
      remove: (state, action) => cartReducer(state, { type: 'remove', id: action.payload }),
      quantity: (state, action) => cartReducer(state, { type: 'quantity', ...action.payload }),
      clear: () => [], replace: (_state, action) => action.payload,
    } });
    export const cartActions = slice.actions;
    export default slice.reducer;
    export const selectItems = state => state.cart;
    export const selectCount = state => state.cart.reduce((n, p) => n + p.quantity, 0);
    export const selectTotal = state => totalCents(state.cart) / 100;
    ''')
    put(22,'src/app/store.js',"import { configureStore } from '@reduxjs/toolkit';\nimport cart from '../cart/slice';\nexport const store = configureStore({ reducer: { cart } });")
    put(22,'src/labs/reduxProbe.js','''
    import { store } from '../app/store';
    import { cartActions, selectCount } from '../cart/slice';
    store.dispatch(cartActions.add({ id: 1, title: 'Probe', price: 2, stock: 2 }));
    console.log('Redux probe count:', selectCount(store.getState()));
    store.dispatch(cartActions.clear());
    ''')
    NOTES[22]='Store mới chưa gắn vào UI. Khi Vite đang chạy, mở Console của trang và chạy import("/src/labs/reduxProbe.js"). Kết quả count=1, sau đó probe clear store. Giỏ thật vẫn là Context đến bài 23. Không gọi probe trên store đã gắn UI ở các bài sau vì probe có action clear.'
    snap(22)
    put(23,'src/cart/CartContext.jsx','''
    import { useEffect, useState } from 'react';
    import { Provider, useDispatch, useSelector } from 'react-redux';
    import { useAuth } from '../auth/AuthContext';
    import { store } from '../app/store';
    import { cartActions, selectItems, selectCount, selectTotal } from './slice';
    import { readCart, writeCart } from './storage';
    function StorageBridge({ children }) {
      const { user, loading } = useAuth(); const key = `shop:cart:${user?.id ?? 'guest'}`;
      const [readyKey, setReadyKey] = useState(null), [failed, setFailed] = useState(false);
      const items = useSelector(selectItems); const dispatch = useDispatch();
      useEffect(() => { if (!loading) { dispatch(cartActions.replace(readCart(key))); setReadyKey(key); } }, [key, loading, dispatch]);
      useEffect(() => { if (!loading && readyKey === key) setFailed(!writeCart(key, items)); }, [items, key, readyKey, loading]);
      if (loading || readyKey !== key) return <p role="status">Đang khôi phục giỏ...</p>;
      return <>{failed && <p role="alert">Không lưu được giỏ hàng trên trình duyệt.</p>}{children}</>;
    }
    export function CartProvider({ children }) { return <Provider store={store}><StorageBridge>{children}</StorageBridge></Provider>; }
    export function useCart() {
      const items = useSelector(selectItems), count = useSelector(selectCount), total = useSelector(selectTotal); const dispatch = useDispatch();
      return { items, count, total, add: p => dispatch(cartActions.add(p)), remove: id => dispatch(cartActions.remove(id)),
        setQuantity: (id, quantity) => dispatch(cartActions.quantity({ id, quantity })), clear: () => dispatch(cartActions.clear()) };
    }
    ''');snap(23)
