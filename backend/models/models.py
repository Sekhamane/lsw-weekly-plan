# SQLAlchemy ORM Models for Leather Sole Works Production Management System

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from db import Base


class RoleEnum(str, PyEnum):
    """User role enumeration"""
    ADMIN = "admin"
    SUPERVISOR = "supervisor"
    EMPLOYEE = "employee"


class User(Base):
    """User model for authentication and role-based access"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    password_hash = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.EMPLOYEE)
    supervisor_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    plans = relationship("WeeklyPlan", back_populates="assigned_to_user", foreign_keys="WeeklyPlan.assigned_to")
    reports = relationship("DailyReport", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")


class WeeklyPlan(Base):
    """Weekly production plan assigned by admin to employees"""
    __tablename__ = "weekly_plans"

    id = Column(Integer, primary_key=True, index=True)
    assigned_by = Column(Integer, ForeignKey("users.id"))  # Admin
    assigned_to = Column(Integer, ForeignKey("users.id"))  # Employee
    work_type = Column(String)  # Repair, Custom Order, Stock Production
    receipt_number = Column(String, nullable=True)
    order_number = Column(String, nullable=True)
    for_stock = Column(Boolean, default=False)
    product_type = Column(String, nullable=True)
    task_description = Column(Text)
    target_quantity = Column(Integer)
    deadline = Column(DateTime)
    status = Column(String, default="Assigned")  # Assigned, Accepted, In Progress, Completed, etc.
    created_at = Column(DateTime, default=datetime.utcnow)
    accepted_at = Column(DateTime, nullable=True)
    
    # Relationships
    assigned_to_user = relationship("User", foreign_keys=[assigned_to], back_populates="plans")
    daily_reports = relationship("DailyReport", back_populates="weekly_plan")


class DailyReport(Base):
    """Daily progress report submitted by employees"""
    __tablename__ = "daily_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    weekly_plan_id = Column(Integer, ForeignKey("weekly_plans.id"))
    date = Column(DateTime, default=datetime.utcnow)
    task_worked_on = Column(Text)
    quantity_completed = Column(Integer)
    progress_percent = Column(Float)
    issues = Column(Text, nullable=True)
    status = Column(String, default="Pending Supervisor")  # Pending Supervisor, Confirmed, Rejected, Approved
    supervisor_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    supervisor_comment = Column(Text, nullable=True)
    admin_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    admin_comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", foreign_keys=[user_id], back_populates="reports")
    weekly_plan = relationship("WeeklyPlan", back_populates="daily_reports")
    material_usage = relationship("MaterialUsage", back_populates="daily_report")


class Material(Base):
    """Raw materials inventory"""
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text, nullable=True)
    unit = Column(String)  # kg, meters, pieces, etc.
    current_stock = Column(Float, default=0)
    reorder_level = Column(Float, default=10)
    unit_price = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    usage = relationship("MaterialUsage", back_populates="material")


class MaterialUsage(Base):
    """Track material usage in daily reports"""
    __tablename__ = "material_usage"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materials.id"))
    daily_report_id = Column(Integer, ForeignKey("daily_reports.id"))
    quantity_used = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    material = relationship("Material", back_populates="usage")
    daily_report = relationship("DailyReport", back_populates="material_usage")


class AuditLog(Base):
    """Audit trail for all critical actions"""
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(String)  # created, updated, approved, rejected, etc.
    user_id = Column(Integer, ForeignKey("users.id"))
    target_type = Column(String)  # WeeklyPlan, DailyReport, Material, etc.
    target_id = Column(Integer)
    old_value = Column(Text, nullable=True)
    new_value = Column(Text, nullable=True)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="audit_logs")
