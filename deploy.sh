#!/bin/bash
echo "================================"
echo "LSW Production Deployment Setup"
echo "================================"
echo

# Check if .env.production exists
if [ ! -f ".env.production" ]; then
    echo "Creating .env.production file..."
    cat > .env.production << EOL
SUPABASE_DB_URL=postgresql://postgres:Sekhamane@2026@db.kxhlapnxgtrsexcjtvfs.supabase.co:5432/postgres
EOL
else
    echo ".env.production already exists"
fi

echo
echo "================================"
echo "Build Frontend"
echo "================================"
cd frontend
npm install
npm run build
cd ..

echo
echo "================================"
echo "Docker Build"
echo "================================"
docker build -t lsw-app:latest .

echo
echo "================================"
echo "Deployment Ready!"
echo "================================"
echo
echo "Next steps:"
echo "1. Backend: Deploy using Railway.app, Render, or Docker"
echo "2. Frontend: Deploy build/ to Netlify or Vercel"
echo "3. Mobile: Use 'npx cap add ios' and 'npx cap add android' in frontend/"
echo
echo "See DEPLOYMENT.md for detailed instructions"
