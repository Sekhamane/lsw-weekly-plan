# Backend entry point for API server
# Framework: FastAPI (recommended for rapid development and role-based APIs)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

# Load environment variables
from db import Base, engine
from routes import user, plan, report, material, audit, auth

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Leather Sole Works Production Management System")

# Add CORS middleware for frontend communication
allowed_origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://localhost:3000",
    os.getenv("FRONTEND_URL", "https://lsw-app.netlify.app"),
    "*"  # Allow all origins in development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables with error handling
try:
    logger.info("Attempting to create database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully!")
except Exception as e:
    logger.error(f"Failed to create database tables: {str(e)}")
    logger.info("App will still start, but database operations may fail")

# Include routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(plan.router)
app.include_router(report.router)
app.include_router(material.router)
app.include_router(audit.router)

@app.get("/")
def root():
    return {"message": "Leather Sole Works Production Management System API", "status": "online"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
