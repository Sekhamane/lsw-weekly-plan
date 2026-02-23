# Backend entry point for API server
# Framework: FastAPI (recommended for rapid development and role-based APIs)

from fastapi import FastAPI

# Load environment variables
from db import Base, engine
from routes import user, plan, report, material, audit, auth

app = FastAPI(title="Leather Sole Works Production Management System")

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(plan.router)
app.include_router(report.router)
app.include_router(material.router)
app.include_router(audit.router)

@app.get("/")
def root():
    return {"message": "Leather Sole Works Production Management System API"}
