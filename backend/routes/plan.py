# Placeholder for weekly plan routes

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import SessionLocal
from models.models import User, WeeklyPlan
from schemas import WeeklyPlanCreate, WeeklyPlanOut
from routes.auth import get_current_user
from typing import List
from datetime import datetime

router = APIRouter(prefix="/plans", tags=["plans"])

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# Admin assigns a weekly plan
@router.post("/assign", response_model=WeeklyPlanOut)
def assign_plan(plan: WeeklyPlanCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	if current_user.role != "admin":
		raise HTTPException(status_code=403, detail="Only admin can assign plans")
	# Validation rules
	if plan.work_type == "Repair" and not plan.receipt_number:
		raise HTTPException(status_code=400, detail="Repair must include Receipt Number")
	if plan.work_type == "Custom Order" and not plan.order_number:
		raise HTTPException(status_code=400, detail="Custom Order must include Order/Invoice Number")
	if plan.work_type == "Stock Production" and not plan.for_stock:
		raise HTTPException(status_code=400, detail="Stock Production must be marked as FOR STOCK")
	if not plan.product_type or not plan.target_quantity:
		raise HTTPException(status_code=400, detail="Product type and target quantity required")
	new_plan = WeeklyPlan(
		assigned_by=current_user.id,
		assigned_to=plan.assigned_to,
		work_type=plan.work_type,
		receipt_number=plan.receipt_number,
		order_number=plan.order_number,
		for_stock=plan.for_stock,
		product_type=plan.product_type,
		task_description=plan.task_description,
		target_quantity=plan.target_quantity,
		deadline=plan.deadline,
		status="Assigned",
		created_at=datetime.utcnow()
	)
	db.add(new_plan)
	db.commit()
	db.refresh(new_plan)
	return new_plan

# Employee accepts assigned plan
@router.post("/{plan_id}/accept", response_model=WeeklyPlanOut)
def accept_plan(plan_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	plan = db.query(WeeklyPlan).filter(WeeklyPlan.id == plan_id, WeeklyPlan.assigned_to == current_user.id).first()
	if not plan:
		raise HTTPException(status_code=404, detail="Plan not found or not assigned to you")
	if plan.status != "Assigned":
		raise HTTPException(status_code=400, detail="Plan already accepted or in progress")
	plan.status = "Accepted"
	plan.accepted_at = datetime.utcnow()
	db.commit()
	db.refresh(plan)
	return plan

# View all plans (Admin)
@router.get("/", response_model=List[WeeklyPlanOut])
def get_all_plans(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	if current_user.role != "admin":
		raise HTTPException(status_code=403, detail="Only admin can view all plans")
	return db.query(WeeklyPlan).all()

# Employee views assigned plans
@router.get("/assigned", response_model=List[WeeklyPlanOut])
def get_assigned_plans(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	return db.query(WeeklyPlan).filter(WeeklyPlan.assigned_to == current_user.id).all()
