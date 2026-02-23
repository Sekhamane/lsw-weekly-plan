# 🏢 Leather Sole Works - Production Management System
## Mobile Application Ready

A complete role-based Production Planning, Material Control, and Audit Logging system for Leather Sole Works, styled with brand colors and ready for deployment as a mobile app.

---

## ⚡ Quick Start

### Prerequisites
- Python 3.13+
- Node.js 18+
- Docker (for containerized deployment)
- Git

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
# Create .env with Supabase DB URL
echo "SUPABASE_DB_URL=postgresql://..." > .env
```

### 2. Frontend Setup
```bash
cd frontend
npm install
```

### 3. Run Locally
**Terminal 1 - Backend:**
```bash
cd backend
python -m uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

Access at: http://localhost:3000

---

## 📱 Mobile Deployment

### Build as Native iOS/Android App

**Install Capacitor:**
```bash
cd frontend
npm install @capacitor/core @capacitor/cli
```

**Add Platforms:**
```bash
npx cap add ios
npx cap add android
npm run build
npx cap sync
```

**Open in IDE:**
- iOS: `npx cap open ios` → Xcode → Build & Sign
- Android: `npx cap open android` → Android Studio → Build APK/AAB

---

## ☁️ Cloud Deployment

### Backend (FastAPI)
1. **Railway.app** (Recommended):
   - Connect GitHub repo
   - Add environment variable: `SUPABASE_DB_URL`
   - Auto-deploys on push

2. **Render.com**:
   - Create Web Service
   - Build command: `pip install -r backend/requirements.txt`
   - Start command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Docker**:
   ```bash
   docker build -t lsw-backend .
   docker run -e SUPABASE_DB_URL=... lsw-backend
   ```

### Frontend (React PWA)
1. **Netlify**:
   - Connect GitHub
   - Build: `cd frontend && npm run build`
   - Publish: `frontend/build`

2. **Vercel**:
   - Push to GitHub
   - Import project
   - Auto-deploys

3. **Firebase Hosting**:
   ```bash
   firebase init hosting
   firebase deploy
   ```

---

## 🎨 Design System

**Brand Colors** (from leathersoleworks.co.ls):
- Primary: #4B2E19 (Deep Brown)
- Accent: #D4B06A (Gold)
- Background: #F8F5F0 (Cream)
- Text: #222 (Dark)

**Logo**: kemeli_logo.png (auto-linked)

---

## 🔐 Role-Based Access

### Admin
- Create & assign weekly plans
- Approve/reject daily reports
- View analytics & inventory
- Access full audit logs

### Supervisor
- Review daily reports
- Confirm/reject work
- Monitor team performance

### Employee
- Accept assigned plans
- Submit daily reports
- Track progress & materials

---

## 📊 Key Features

✅ Workflow Control & Status Tracking
✅ Material Inventory Management
✅ Complete Audit Logging
✅ Role-Based Dashboards
✅ Mobile Responsive Design
✅ PWA Ready
✅ Database: Supabase PostgreSQL
✅ Authentication: JWT Tokens

---

## 📁 Project Structure

```
lsw-weekly-plan/
├── backend/
│   ├── main.py              # FastAPI entry point
│   ├── db.py                # Database config
│   ├── models/
│   │   └── models.py        # SQLAlchemy models
│   ├── routes/              # API endpoints
│   ├── schemas.py           # Pydantic schemas
│   ├── utils.py             # Auth & utilities
│   └── requirements.txt
├── frontend/
│   ├── public/              # Static assets
│   ├── src/                 # React components
│   ├── App.js               # Main app
│   ├── styles.css           # Brand styling
│   ├── package.json
│   └── capacitor.config.json # Mobile config
├── Dockerfile
├── docker-compose.yml
├── Procfile                 # Heroku/Railway config
├── deploy.sh / deploy.bat   # Deployment script
└── DEPLOYMENT.md            # Detailed guide
```

---

## 🚀 Deployment Checklist

- [ ] Backend deployed (Railway/Render/Docker)
- [ ] Frontend deployed (Netlify/Vercel)
- [ ] Environment variables configured
- [ ] CORS enabled for API
- [ ] Database migrations applied
- [ ] Test admin/supervisor/employee logins
- [ ] Mobile app built & tested
- [ ] App submitted to App Store/Play Store

---

## 🔗 APIs

**Base URL**: https://your-backend-url/

### Public Endpoints
- `POST /auth/login` - User login
- `POST /auth/register` - User registration
- `GET /auth/me` - Current user info

### Protected Endpoints
- `POST /plans/assign` - Create weekly plan (Admin)
- `GET /plans` - View all plans (Admin)
- `GET /plans/assigned` - View assigned plans (Employee)
- `POST /reports/submit` - Submit daily report (Employee)
- `GET /materials/inventory` - View inventory (All)
- `GET /audit/logs` - View audit logs (Admin)

---

## 📞 Support

For issues or deployment help, refer to DEPLOYMENT.md or contact the development team.

---

**Built with** ❤️ **for Leather Sole Works - Est. 2016**
