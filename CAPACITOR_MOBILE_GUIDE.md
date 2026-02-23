# 📱 LSW Capacitor Mobile App Guide

## Quick Start - Mobile App Build

### Prerequisites
- Node.js 14+ and npm
- For iOS: Xcode (macOS only)
- For Android: Android Studio + Android SDK

---

## Step 1: Build React Frontend

```powershell
cd frontend
npm run build
cd ..
```

This creates an optimized production build in `frontend/build/`

---

## Step 2: Add Capacitor Platforms

**Option A: Run automated script (EASIEST)**
```powershell
.\build-mobile.bat
```

**Option B: Manual commands**
```powershell
cd frontend

# Install Capacitor CLI globally
npm install -g @capacitor/cli

# Install Capacitor packages
npm install @capacitor/core @capacitor/cli

# Add iOS platform (macOS only)
npx cap add ios

# Add Android platform
npx cap add android

# Sync the platforms
npx cap sync
```

---

## Step 3: Configure API URL for Mobile

The mobile app needs to know where the backend API is located.

### For Local Backend Testing:
Edit `frontend/capacitor.config.json`:
```json
{
  "...": "...",
  "server": {
    "androidScheme": "https",
    "url": "http://192.168.x.x:8000"  // Your local machine IP
  }
}
```

### For Production (Railway):
```json
{
  "server": {
    "androidScheme": "https",
    "url": "https://your-railway-backend-url.up.railway.app"
  }
}
```

Then resync:
```powershell
cd frontend
npx cap sync
cd ..
```

---

## Step 4: Build for iOS

**Requirements:**
- macOS with Xcode installed
- Apple Developer Account (for App Store)

```powershell
cd frontend
npx cap open ios
```

This opens Xcode. In Xcode:
1. Select "LSW" project
2. Select your target device
3. Click "Play" to build & run
4. Or go to Product → Archive to create distribution build

**Troubleshooting iOS:**
- Make sure provisioning profile is configured
- Check Build Settings if you get signing errors
- Use simulator: Select iPhone simulator in Xcode

---

## Step 5: Build for Android

**Requirements:**
- Android Studio
- Android SDK (API 24+)
- Android Virtual Device (emulator) or connected device

```powershell
cd frontend
npx cap open android
```

This opens Android Studio. In Android Studio:
1. Select device/emulator
2. Click "Run" to build & deploy
3. Or Build → Build Bundle for Play Store upload

**Troubleshooting Android:**
- If emulator won't start: Android Studio → Tools → AVD Manager
- Check USB debugging enabled on physical device
- Make sure ANDROID_HOME environment variable is set

---

## Step 6: Build Production Releases

### iOS Release
```powershell
cd frontend
npm run build
npx cap sync ios
# Then in Xcode: Product → Archive
```

### Android Release
```powershell
cd frontend
npm run build
npx cap sync android
# Then in Android Studio: Build → Build Bundle(s)
```

---

## Local Backend Server (for testing)

While developing, run your backend locally on the same machine:

```powershell
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Get your local IP:**
```powershell
ipconfig
# Look for IPv4 Address (usually 192.168.x.x)
```

Then in `frontend/capacitor.config.json`:
```json
"server": {
  "url": "http://192.168.1.100:8000"  // Replace with your IP
}
```

Resync and rebuild:
```powershell
cd frontend
npx cap sync
npx cap open android  # or ios
```

---

## Testing the Mobile App

### Login Test
1. Open app on device/emulator
2. Default credentials:
   - Username: `admin`
   - Password: `admin123`

### Features by Role
- **Admin**: Create weekly plans, approve reports, view audit logs
- **Supervisor**: Review and confirm daily reports
- **Employee**: Accept plans, submit daily reports

---

## Deployment to App Stores

### Apple App Store
1. Create Apple Developer Account
2. In Xcode: Product → Archive
3. Upload to App Store Connect
4. Submit for review (48-72 hours)

### Google Play Store
1. Create Google Play Developer Account
2. In Android Studio: Build → Build Bundle(s)
3. Upload AAB/APK to Google Play Console
4. Submit for review (few hours typically)

---

## Environment Variables

Capacitor doesn't support .env files like web apps. Instead:

For Android (`android/app/build.gradle`):
```gradle
buildTypes {
    release {
        buildConfigField "String", "API_URL", '"https://your-api-url.com"'
    }
}
```

For iOS (`ios/LSW/Info.plist`):
```xml
<key>API_URL</key>
<string>https://your-api-url.com</string>
```

Or better - configure in `capacitor.config.json` (recommended).

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Module not found" | Run `npm install` in frontend directory |
| iOS build fails | Check Xcode version matches iOS target |
| Android build hangs | Close Android Studio and run `npx cap open android` again |
| App won't connect to API | Verify API_URL in capacitor.config.json, check firewall |
| Blank screen on launch | Check browser console in DevTools (F12 in Android Chrome) |
| Emulator too slow | Use Android Studio's performance settings or physical device |

---

## Quick Command Reference

```powershell
# Build frontend for mobile
cd frontend && npm run build && cd ..

# Open in Xcode
cd frontend && npx cap open ios && cd ..

# Open in Android Studio
cd frontend && npx cap open android && cd ..

# Sync after config changes
cd frontend && npx cap sync && cd ..

# Test locally
cd backend && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Build optimized production
cd frontend && npm run build && cd ..
```

---

## Next Steps

1. ✅ Run `.\build-mobile.bat` to set up both platforms
2. ✅ Configure API_URL in `capacitor.config.json`
3. ✅ Open in Xcode/Android Studio
4. ✅ Test on simulator/emulator
5. ✅ Test on physical device
6. ✅ Submit to App Stores

**Your Leather Sole Works mobile app will be live in the cloud!** 📱🚀
