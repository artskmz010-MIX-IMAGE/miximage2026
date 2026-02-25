# ⚡ Checklist: ให้โปรเจกต์รันขึ้นใน 15 นาที

ใช้เช็กลิสต์นี้เพื่อให้โปรเจกต์ขึ้นหน้าเว็บได้เร็วที่สุดในเครื่องใหม่

## 0) เตรียมเครื่อง (ประมาณ 2 นาที)

- [ ] อยู่ในโฟลเดอร์โปรเจกต์
  ```bash
  cd /workspace/miximage2026
  ```
- [ ] ตรวจเวอร์ชัน Node.js (แนะนำ 18+)
  ```bash
  node -v
  npm -v
  ```

## 1) ติดตั้ง dependencies (ประมาณ 3-5 นาที)

- [ ] ล้างการติดตั้งที่ค้าง/ไม่สมบูรณ์ (ถ้ามี)
  ```bash
  rm -rf node_modules package-lock.json
  ```
- [ ] ติดตั้งใหม่
  ```bash
  npm install
  ```
- [ ] ยืนยันว่า Vite ถูกติดตั้งแล้ว
  ```bash
  npx vite --version
  ```

> ถ้า `npm install` ค้างนานผิดปกติ ให้ลองเปลี่ยน registry ชั่วคราว:
>
> ```bash
> npm config set registry https://registry.npmjs.org/
> npm install
> ```

## 2) ทำไฟล์เริ่มต้นให้ครบ (ประมาณ 3 นาที)

ปัจจุบัน `index.html` อ้างถึง `/src/main.tsx` ดังนั้นต้องมี `src/main.tsx` และ `src/App.tsx`

- [ ] สร้างโฟลเดอร์และไฟล์ขั้นต่ำ
  ```bash
  mkdir -p src
  cat > src/App.tsx <<'APP'
  export default function App() {
    return <h1>Miximage AI 2026 is running ✅</h1>;
  }
  APP

  cat > src/main.tsx <<'MAIN'
  import React from 'react'
  import ReactDOM from 'react-dom/client'
  import App from './App'

  ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
  )
  MAIN
  ```

## 3) ตั้งค่า env ขั้นต่ำ (ประมาณ 1 นาที)

- [ ] สร้าง `.env.local` ขั้นต่ำ (ถ้ายังไม่มี)
  ```bash
  cat > .env.local <<'ENV'
  VITE_APP_NAME=MIX IMAGE AI 2026
  VITE_ENV=development
  ENV
  ```

> ถ้าฟีเจอร์ AI/Supabase ต้องใช้จริง ให้เติมค่า `VITE_SUPABASE_URL` และ `VITE_SUPABASE_PUBLISHABLE_KEY` เพิ่ม

## 4) รันทดสอบพื้นฐาน (ประมาณ 2-3 นาที)

- [ ] Build ผ่าน
  ```bash
  npm run build
  ```
- [ ] Lint ผ่าน (ถ้าพร้อม)
  ```bash
  npm run lint
  ```
- [ ] เปิด dev server
  ```bash
  npm run dev
  ```
- [ ] เปิดในเบราว์เซอร์ที่ URL ที่แสดง (ปกติ `http://localhost:5173`)

## 5) Definition of Done

ถือว่า “รันขึ้นแล้ว” เมื่อครบทุกข้อ:

- [ ] `npm run build` จบโดยไม่ error
- [ ] `npm run dev` ขึ้นสำเร็จ
- [ ] หน้าเว็บแสดงข้อความ `Miximage AI 2026 is running ✅`

---

## ปัญหาที่เจอบ่อย + วิธีแก้เร็ว

1. **`vite: not found`**  
   แปลว่า dependencies ติดตั้งไม่ครบ → รัน `npm install` ใหม่

2. **หา `src/main.tsx` ไม่เจอ**  
   สร้างไฟล์ตามขั้นตอนข้อ 2 หรือแก้ entry ใน `index.html` ให้ชี้ไฟล์ที่มีจริง

3. **คำสั่งค้างตอนติดตั้ง**  
   ลองรีเซ็ต `node_modules`, เปลี่ยน npm registry, แล้วติดตั้งใหม่
