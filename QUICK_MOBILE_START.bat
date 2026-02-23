@echo off
REM 🚀 LSW Mobile App - Quick Start (Windows)

echo ================================================
echo 📱 LEATHER SOLE WORKS - CAPACITOR MOBILE BUILD
echo ================================================
echo.

REM Install frontend dependencies
echo 📥 Step 1: Installing frontend dependencies...
cd frontend
call npm install
cd ..

REM Build frontend
echo 📦 Step 2: Building optimized frontend...
cd frontend
call npm run build
if errorlevel 1 (
    echo ❌ Build failed! Check npm logs above.
    pause
    exit /b 1
)
cd ..

REM Install Capacitor CLI globally
echo 📥 Step 3: Installing Capacitor CLI...
call npm install -g @capacitor/cli

REM Setup Capacitor
echo 🔧 Step 4: Setting up Capacitor...
cd frontend

REM Check if capacitor is already initialized
if exist "capacitor.config.json" (
    echo ✅ Capacitor already initialized
) else (
    echo Initializing Capacitor...
    call npx @capacitor/cli@latest init
)

REM Add platforms
echo 🍎 Step 5: Adding iOS platform...
call npx cap add ios

echo 🤖 Step 6: Adding Android platform...
call npx cap add android

REM Sync
echo 🔄 Step 7: Syncing platforms...
call npx cap sync

cd ..

echo.
echo ================================================
echo ✅ SETUP COMPLETE!
echo ================================================
echo.
echo Next steps:
echo.
echo 1️⃣  For ANDROID (requires Android Studio):
echo    cd frontend
echo    npx cap open android
echo.
echo 2️⃣  For iOS (requires macOS + Xcode - NOT available on Windows):
echo    cd frontend
echo    npx cap open ios
echo.
echo 3️⃣  To test locally with backend:
echo    cd backend
echo    python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
echo.
echo 📱 Then deploy to Android Studio emulator or physical device!
echo.

pause
