# Placeholder for material and inventory routes

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from models.models import User, Material, MaterialUsage, DailyReport
from schemas import MaterialCreate, MaterialOut
from routes.auth import get_current_user
from typing import List

router = APIRouter(prefix="/materials", tags=["materials"])

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# Admin adds new material or restocks
@router.post("/add", response_model=MaterialOut)
def add_material(material: MaterialCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	if current_user.role != "admin":
		raise HTTPException(status_code=403, detail="Only admin can add materials")
	db_material = db.query(Material).filter(Material.name == material.name).first()
	if db_material:
		db_material.current_stock += material.current_stock
		db.commit()
		db.refresh(db_material)
		return db_material
	new_material = Material(
		name=material.name,
		unit=material.unit,
		current_stock=material.current_stock
	)
	db.add(new_material)
	db.commit()
	db.refresh(new_material)
	return new_material

# Admin updates material info
@router.put("/{material_id}/update", response_model=MaterialOut)
def update_material(material_id: int, material: MaterialCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	if current_user.role != "admin":
		raise HTTPException(status_code=403, detail="Only admin can update materials")
	db_material = db.query(Material).filter(Material.id == material_id).first()
	if not db_material:
		raise HTTPException(status_code=404, detail="Material not found")
	db_material.name = material.name
	db_material.unit = material.unit
	db_material.current_stock = material.current_stock
	db.commit()
	db.refresh(db_material)
	return db_material

# View inventory levels (all roles)
@router.get("/inventory", response_model=List[MaterialOut])
def get_inventory(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	return db.query(Material).all()

# Material usage summary (all roles, filtered by role)
@router.get("/usage-summary")
def material_usage_summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	# For admin: all usage, for supervisor: their employees, for employee: own
	query = db.query(MaterialUsage, DailyReport, Material)
	query = query.join(DailyReport, MaterialUsage.daily_report_id == DailyReport.id)
	query = query.join(Material, MaterialUsage.material_id == Material.id)
	if current_user.role == "employee":
		query = query.filter(DailyReport.user_id == current_user.id)
	elif current_user.role == "supervisor":
		employees = db.query(User).filter(User.supervisor_id == current_user.id).all()
		employee_ids = [e.id for e in employees]
		query = query.filter(DailyReport.user_id.in_(employee_ids))
	# else admin: no filter
	usage = [
		{
			"material": m.name,
			"unit": m.unit,
			"quantity_used": mu.quantity_used,
			"report_id": dr.id,
			"employee_id": dr.user_id
		}
		for mu, dr, m in query.all()
	]
	return usage
