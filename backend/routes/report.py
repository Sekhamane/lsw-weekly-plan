# Placeholder for daily report routes

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import SessionLocal
from models.models import User, DailyReport, WeeklyPlan, MaterialUsage
from schemas import DailyReportCreate, DailyReportOut
from routes.auth import get_current_user
from typing import List
from datetime import datetime

router = APIRouter(prefix="/reports", tags=["reports"])

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# Employee submits daily report
@router.post("/submit", response_model=DailyReportOut)
def submit_report(report: DailyReportCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	# Validate plan ownership
	plan = db.query(WeeklyPlan).filter(WeeklyPlan.id == report.weekly_plan_id, WeeklyPlan.assigned_to == current_user.id).first()
	if not plan:
		raise HTTPException(status_code=404, detail="Weekly plan not found or not assigned to you")
	# Validate quantity
	if report.quantity_completed > plan.target_quantity:
		raise HTTPException(status_code=400, detail="Quantity exceeds target")
	new_report = DailyReport(
		user_id=current_user.id,
		weekly_plan_id=report.weekly_plan_id,
		task_worked_on=report.task_worked_on,
		quantity_completed=report.quantity_completed,
		progress_percent=report.progress_percent,
		issues=report.issues,
		status="Pending Supervisor",
		date=datetime.utcnow()
	)
	db.add(new_report)
	db.commit()
	db.refresh(new_report)
	# Material usage (simplified, assumes list of dicts with material_id and quantity_used)
	for mu in report.materials_used:
		db.add(MaterialUsage(
			material_id=mu["material_id"],
			quantity_used=mu["quantity_used"],
			daily_report_id=new_report.id
		))
	db.commit()
	return new_report

# Supervisor confirms report
@router.post("/{report_id}/confirm", response_model=DailyReportOut)
def confirm_report(report_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	report = db.query(DailyReport).filter(DailyReport.id == report_id).first()
	if not report:
		raise HTTPException(status_code=404, detail="Report not found")
	# Only supervisor of employee can confirm
	employee = db.query(User).filter(User.id == report.user_id).first()
	if not employee or employee.supervisor_id != current_user.id:
		raise HTTPException(status_code=403, detail="Not authorized to confirm this report")
	report.status = "Pending Admin Approval"
	report.supervisor_id = current_user.id
	db.commit()
	db.refresh(report)
	return report

# Supervisor rejects report
@router.post("/{report_id}/reject", response_model=DailyReportOut)
def reject_report(report_id: int, comment: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	report = db.query(DailyReport).filter(DailyReport.id == report_id).first()
	if not report:
		raise HTTPException(status_code=404, detail="Report not found")
	employee = db.query(User).filter(User.id == report.user_id).first()
	if not employee or employee.supervisor_id != current_user.id:
		raise HTTPException(status_code=403, detail="Not authorized to reject this report")
	report.status = "Rejected by Supervisor"
	report.supervisor_id = current_user.id
	report.supervisor_comment = comment
	db.commit()
	db.refresh(report)
	return report


# Admin approves report
@router.post("/{report_id}/approve", response_model=DailyReportOut)
def approve_report(report_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	if current_user.role != "admin":
		raise HTTPException(status_code=403, detail="Only admin can approve reports")
	report = db.query(DailyReport).filter(DailyReport.id == report_id).first()
	if not report:
		raise HTTPException(status_code=404, detail="Report not found")
	report.status = "Fully Approved"
	report.admin_id = current_user.id
	db.commit()
	db.refresh(report)
	# Deduct materials from inventory
	usages = db.query(MaterialUsage).filter(MaterialUsage.daily_report_id == report.id).all()
	for usage in usages:
		material = db.query(Material).filter(Material.id == usage.material_id).first()
		if material:
			material.current_stock -= usage.quantity_used
			db.commit()
	# Audit log
	db.add(AuditLog(
		action="Admin Approved Report",
		user_id=current_user.id,
		target_type="DailyReport",
		target_id=report.id,
		details=f"Materials deducted: {[{'material_id': u.material_id, 'qty': u.quantity_used} for u in usages]}"
	))
	db.commit()
	return report

# Admin rejects report
@router.post("/{report_id}/admin_reject", response_model=DailyReportOut)
def admin_reject_report(report_id: int, comment: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	if current_user.role != "admin":
		raise HTTPException(status_code=403, detail="Only admin can reject reports")
	report = db.query(DailyReport).filter(DailyReport.id == report_id).first()
	if not report:
		raise HTTPException(status_code=404, detail="Report not found")
	report.status = "Rejected by Admin"
	report.admin_id = current_user.id
	report.admin_comment = comment
	db.commit()
	db.refresh(report)
	return report

# Employee views own reports
@router.get("/mine", response_model=List[DailyReportOut])
def get_my_reports(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	return db.query(DailyReport).filter(DailyReport.user_id == current_user.id).all()

# Supervisor views reports pending confirmation
@router.get("/pending", response_model=List[DailyReportOut])
def get_pending_reports(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	# Reports for employees under this supervisor
	employees = db.query(User).filter(User.supervisor_id == current_user.id).all()
	employee_ids = [e.id for e in employees]
	return db.query(DailyReport).filter(DailyReport.user_id.in_(employee_ids), DailyReport.status == "Pending Supervisor").all()

# Admin views reports pending approval
@router.get("/for-approval", response_model=List[DailyReportOut])
def get_reports_for_approval(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	if current_user.role != "admin":
		raise HTTPException(status_code=403, detail="Only admin can view reports for approval")
	return db.query(DailyReport).filter(DailyReport.status == "Pending Admin Approval").all()
