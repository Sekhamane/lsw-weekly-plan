#!/bin/bash
# Capacitor Mobile Build Script for LSW App

echo "🚀 Building LSW Mobile App with Capacitor..."

# Step 1: Build React frontend
echo "📦 Building React frontend..."
cd frontend
npm run build

# Step 2: Install Capacitor CLI globally (if not already installed)
echo "📥 Installing Capacitor CLI..."
npm install -g @capacitor/cli

# Step 3: Install Capacitor packages
echo "📥 Installing Capacitor packages..."
npm install @capacitor/core @capacitor/cli

# Step 4: Add iOS platform
echo "🍎 Adding iOS platform..."
npx cap add ios

# Step 5: Add Android platform
echo "🤖 Adding Android platform..."
npx cap add android

# Step 6: Sync native platforms
echo "🔄 Syncing native platforms..."
npx cap sync

echo "✅ Mobile app build complete!"
echo ""
echo "Next steps:"
echo "1. For iOS: npx cap open ios (requires Xcode)"
echo "2. For Android: npx cap open android (requires Android Studio)"
echo ""
echo "Configure API URL in each platform before building!"
