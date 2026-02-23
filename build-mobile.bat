@echo off
REM Capacitor Mobile Build Script for LSW App (Windows)

echo 🚀 Building LSW Mobile App with Capacitor...

REM Step 1: Build React frontend
echo 📦 Building React frontend...
cd frontend
call npm run build
cd ..

REM Step 2: Install Capacitor CLI globally (if not already installed)
echo 📥 Installing Capacitor CLI...
call npm install -g @capacitor/cli

REM Step 3: Install Capacitor packages in frontend
echo 📥 Installing Capacitor packages...
cd frontend
call npm install @capacitor/core @capacitor/cli

REM Step 4: Add iOS platform
echo 🍎 Adding iOS platform...
call npx cap add ios

REM Step 5: Add Android platform
echo 🤖 Adding Android platform...
call npx cap add android

REM Step 6: Sync native platforms
echo 🔄 Syncing native platforms...
call npx cap sync

echo ✅ Mobile app build complete!
echo.
echo Next steps:
echo 1. For iOS: npx cap open ios (requires Xcode on macOS)
echo 2. For Android: npx cap open android (requires Android Studio)
echo.
echo Configure API URL in each platform before building!

pause
