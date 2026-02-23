# ⚡ LSW DEPLOYMENT - Step-by-Step (Real Quick!)

## PART 1: Push to GitHub (2 minutes)

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `lsw-weekly-plan`
3. Description: "Leather Sole Works Production Management System"
4. Choose Public or Private
5. Click "Create repository"
6. Copy the HTTPS URL (e.g., https://github.com/YOUR-USERNAME/lsw-weekly-plan.git)

### Step 2: Initialize Git & Push (Run these commands)

**Open PowerShell in project root and run:**

```powershell
# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: LSW Production Management System"

# Add remote (replace with YOUR GitHub URL)
git remote add origin https://github.com/YOUR-USERNAME/lsw-weekly-plan.git

# Push to GitHub
git branch -M main
git push -u origin main
```

✅ **Your code is now on GitHub!**

---

## PART 2: Deploy Backend on Railway.app (5 minutes)

### Step 1: Create Railway Account
1. Go to https://railway.app
2. Click "Login" → "Continue with GitHub"
3. Authorize Railway
4. You're logged in!

### Step 2: Create New Project
1. Click "New Project" 
2. Select "Deploy from GitHub repo"
3. Search for `lsw-weekly-plan`
4. Click to connect
5. Railway auto-detects Python ✅

### Step 3: Add Environment Variable
1. In Railway Dashboard, find your project
2. Click "Variables" tab
3. Click "New Variable"
4. Paste:
   ```
   SUPABASE_DB_URL=postgresql://postgres:Sekhamane@2026@db.kxhlapnxgtrsexcjtvfs.supabase.co:5432/postgres
   ```
5. Click Add
6. **Railway auto-deploys with fixes!** 🚀

**If build still fails, wait 2-3 minutes and check Railway logs for any remaining issues.**

### Step 4: Get Your Backend URL
1. Go to "Deployments" tab
2. Wait for green ✅ status
3. Click on deployment
4. Copy domain (e.g., `railway-prod-xxxx.up.railway.app`)
5. **SAVE THIS URL** - you'll need it for frontend

✅ **Backend is LIVE!**

---

## PART 3: Deploy Frontend on Netlify (5 minutes)

### Step 1: Create Netlify Account & Connect
1. Go to https://netlify.com
2. Click "Sign up" → Choose "GitHub"
3. Authorize Netlify
4. You're in!

### Step 2: Create New Site
1. Click "Add new site" → "Import an existing project"
2. Select GitHub
3. Search for `lsw-weekly-plan`
4. Click to connect
5. Click "Authorize Netlify App" (GitHub popup)

### Step 3: Configure Build Settings
**Netlify shows build configuration:**
- **Base directory**: `frontend`
- **Build command**: `npm run build`
- **Publish directory**: `build`

✅ This is already correct! Click "Deploy site"

### Step 4: Add Environment Variable
1. After deploy starts, go to "Site settings"
2. Click "Build & deploy" → "Environment"
3. Click "Edit variables"
4. Add new variable:
   - Key: `REACT_APP_API_URL`
   - Value: `https://YOUR-RAILWAY-BACKEND-URL` (paste your Railway domain)
5. Save
6. Go to "Deployments" → "Trigger deploy" → "Deploy site"

### Step 5: Get Your Frontend URL
1. Wait for "Published" status ✅
2. Click on site name or domain
3. **Your app is LIVE!** 🎉

✅ **Frontend is LIVE!**

---

## 🎯 VERIFY EVERYTHING WORKS

### Test Login
1. Open your Netlify frontend URL
2. Try login with test user
3. Check that API calls work (check browser console for errors)

### Troubleshooting
- **No login button?** → Check browser console for JS errors
- **API errors?** → Verify `REACT_APP_API_URL` is set correctly in Netlify
- **Backend issues?** → Check Railway logs (click deployment)
- **Railway build fails?** → Check if all dependencies are in `backend/requirements.txt` and `runtime.txt` specifies Python version

---

## ✅ SUCCESS CHECKLIST

- [x] Code on GitHub
- [x] Backend on Railway.app (live at your Railway URL)
- [x] Frontend on Netlify (live at your Netlify domain)
- [x] Both apps connected with correct API URL
- [x] Test login works
- [x] Dashboard displays correctly

---

## NEXT: Mobile Apps (Optional)

When ready to deploy as iOS/Android apps:

```powershell
cd frontend
npm install
npm run build
npx cap add ios
npx cap add android
npm run build
npx cap sync
npx cap open ios         # Opens Xcode
npx cap open android     # Opens Android Studio
```

Then submit to App Store & Google Play.

---

## 📝 SAVE YOUR URLS

**Backend API**: https://______________________ (from Railway)

**Frontend Web**: https://______________________ (from Netlify)

---

**YOUR APP IS LIVE IN THE CLOUD!** 🚀
