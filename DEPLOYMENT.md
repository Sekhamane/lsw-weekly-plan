# Leather Sole Works - Production Deployment Guide

## Backend Deployment

### Option 1: Deploy on Railway.app (Recommended for Ease)
1. Push code to GitHub
2. Create account on railway.app
3. Connect GitHub repository
4. Add environment variables:
   - `SUPABASE_DB_URL`: Your Supabase PostgreSQL connection string
5. Railway auto-deploys on push

### Option 2: Deploy on Render.com
1. Connect GitHub repo to Render
2. Create Web Service (Python/pip)
3. Set build command: `pip install -r backend/requirements.txt`
4. Set start command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables

### Option 3: Deploy using Docker on AWS/Azure/GCP
```bash
docker build -t lsw-backend .
docker tag lsw-backend YOUR_REGISTRY/lsw-backend:latest
docker push YOUR_REGISTRY/lsw-backend:latest
# Deploy container to your cloud platform
```

## Frontend Deployment

### Option 1: Deploy on Netlify
1. Connect GitHub repo to Netlify
2. Build command: `cd frontend && npm run build`
3. Publish directory: `frontend/build`
4. Add environment variable: `REACT_APP_API_URL=<your-backend-url>`

### Option 2: Deploy on Vercel
1. `npm install -g vercel`
2. `vercel --prod`
3. Configure build settings

### Option 3: Deploy on Firebase Hosting
```bash
npm install -g firebase-tools
firebase init hosting
firebase deploy
```

## Mobile App Deployment (Using Capacitor)

### Prerequisites
- Capacitor installed: `npm install @capacitor/core @capacitor/cli`
- iOS: Xcode, CocoaPods
- Android: Android Studio, SDK

### Build for iOS
```bash
cd frontend
npm install
npm run build
npx cap add ios
npx cap sync ios
npx cap open ios
# In Xcode: Select signing team and build
```

### Build for Android
```bash
cd frontend
npm install
npm run build
npx cap add android
npx cap sync android
npx cap open android
# In Android Studio: Build APK or AAB
```

##Environment Variables

Create `.env` files:

**Backend (.env)**:
```
SUPABASE_DB_URL=postgresql://postgres:PASSWORD@db.kxhlapnxgtrsexcjtvfs.supabase.co:5432/postgres
```

**Frontend (.env)**:
```
REACT_APP_API_URL=https://your-backend-url.com
```

## CI/CD Pipeline Setup

GitHub Actions can auto-deploy on push. Create `.github/workflows/deploy.yml` for automated deployments.

## Live URLs (Update after deployment)
- Backend API: `https://lsw-api.railway.app` (or your hosted URL)
- Frontend: `https://lsw-app.netlify.app` (or your hosted URL)
- Mobile Apps: Available on App Store and Google Play
