# 🚀 Deploy to Railway.app - Complete Guide

Railway.app is the EASIEST way to deploy this app. You get:
- Free tier with $5/month credit
- PostgreSQL included (uses Supabase instead)
- Auto-deploys on git push
- Built-in monitoring & logs

---

## Step 1: Prepare GitHub Repository

```bash
git init
git add .
git commit -m "LSW Production Management System"
git remote add origin https://github.com/YOUR-USERNAME/lsw-weekly-plan.git
git push -u origin main
```

---

## Step 2: Sign Up & Create Project on Railway

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Authorize & select your `lsw-weekly-plan` repo

---

## Step 3: Add Environment Variables

After creating project:
1. Go to "Variables" tab
2. Add:
   ```
   SUPABASE_DB_URL = postgresql://postgres:Sekhamane@2026@db.kxhlapnxgtrsexcjtvfs.supabase.co:5432/postgres
   ```

---

## Step 4: Configure Build & Start

Railway will auto-detect Python/Node.js.

**For Backend Service:**
- Build Command: (leave blank, auto-detect)
- Start Command: `cd backend && python -m uvicorn main:app --host 0.0.0.0 --port $PORT`

---

## Step 5: Deploy Frontend on Netlify

1. Go to https://netlify.com
2. Connect GitHub repo
3. Set Build Command: `cd frontend && npm run build`
4. Set Publish Directory: `frontend/build`
5. Add environment variable:
   ```
   REACT_APP_API_URL = https://your-railway-backend-url
   ```

To get Railway URL:
- Go to Railway Dashboard
- Click your project
- Go to "Settings"
- Copy domain (e.g., `lsw-railway-prod.up.railway.app`)

Update Netlify envvar with full URL:
```
REACT_APP_API_URL = https://lsw-railway-prod.up.railway.app
```

---

## Step 6: Update Frontend API Endpoint

Update `frontend/utils/auth.js`:
```javascript
const API_BASE = process.env.REACT_APP_API_URL || "http://localhost:8000";

export function buildApiUrl(path) {
  return `${API_BASE}${path}`;
}
```

Update all axios calls:
```javascript
axios.post(`${API_BASE}/auth/login`, ...)
```

---

## Step 7: Build & Deploy Mobile App

After frontend is live on Netlify:

```bash
cd frontend
npm install
npm run build
npx cap add ios
npx cap add android
npx cap sync

# For iOS
npx cap open ios
# In Xcode: Set signing team, Build & Archive

# For Android
npx cap open android  
# In Android Studio: Build > Build Bundle(s) / APK(s)
```

---

## Step 8: Submit to App Stores

**iOS App Store:**
1. Create Apple Developer Account
2. Create App ID & App
3. Archive in Xcode
4. Submit via Xcode

**Google Play Store:**
1. Create Google Play Developer Account
2. Create App
3. Upload AAB or APK
4. Fill metadata, screenshots, description
5. Submit for review

---

## Live URLs (After Deployment)

- **Backend API**: `https://your-project-name.up.railway.app`
- **Web Frontend**: `https://your-site.netlify.app`
- **iOS App**: Apple App Store
- **Android App**: Google Play Store

---

## Troubleshooting

### Backend won't deploy
Check Railway logs:
```
Railway Dashboard → Your Project → Logs
```

Common issues:
- Missing SUPABASE_DB_URL
- Python version (need 3.10+)
- Missing `requirements.txt`

### Frontend build fails
Check Netlify logs:
- Verify `npm run build` works locally
- Ensure REACT_APP_API_URL is set
- Check frontend/package.json is valid

### API calls fail on mobile
- CORS issue: Add to backend FastAPI:
```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Monitor & Manage

**Railway Dashboard:**
- View logs in real-time
- Monitor database usage
- Scale instances
- View deployments

**Netlify Dashboard:**
- View build logs
- Monitor performance
- Configure domain
- Set cache & redirects

---

✅ **You're live! Your app is now accessible worldwide**

Next steps:
1. Create test user accounts
2. Test all workflows
3. Promote to app stores
4. Monitor analytics

