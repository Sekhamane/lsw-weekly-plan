# Placeholder for audit log routes

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from models.models import User, AuditLog
from routes.auth import get_current_user
from typing import List

router = APIRouter(prefix="/audit", tags=["audit"])

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# Admin views audit logs
@router.get("/logs")
def get_audit_logs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	if current_user.role != "admin":
		raise HTTPException(status_code=403, detail="Only admin can view audit logs")
	logs = db.query(AuditLog).order_by(AuditLog.timestamp.desc()).all()
	return [
		{
			"id": log.id,
			"action": log.action,
			"user_id": log.user_id,
			"target_type": log.target_type,
			"target_id": log.target_id,
			"timestamp": log.timestamp,
			"details": log.details
		}
		for log in logs
	]
