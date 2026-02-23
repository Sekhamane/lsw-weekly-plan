# Data model outline for Leather Sole Works & Supplies Production Management System

# User roles: Admin, Supervisor, Employee
# Entities: User, WeeklyPlan, DailyReport, Material, Inventory, AuditLog

from enum import Enum
from datetime import datetime
from typing import List, Optional

class Role(str, Enum):
    ADMIN = "admin"
    SUPERVISOR = "supervisor"
    EMPLOYEE = "employee"

class User:
    id: int
    username: str
    password_hash: str
    role: Role
    supervisor_id: Optional[int]  # For employees

class WeeklyPlan:
    id: int
    assigned_by: int  # Admin user id
    assigned_to: int  # Employee user id
    work_type: str  # Repair, Custom Order, Stock Production
    receipt_number: Optional[str]
    order_number: Optional[str]
    for_stock: bool
    product_type: Optional[str]
    task_description: str
    target_quantity: int
    required_materials: List[int]  # Material IDs
    deadline: datetime
    status: str  # Assigned, Accepted, In Progress, etc.
    created_at: datetime
    accepted_at: Optional[datetime]

class DailyReport:
    id: int
    user_id: int
    weekly_plan_id: int
    date: datetime
    task_worked_on: str
    quantity_completed: int
    progress_percent: float
    materials_used: List[int]  # MaterialUsage IDs
    issues: Optional[str]
    status: str  # Pending Supervisor, Rejected, Confirmed, Approved
    supervisor_id: Optional[int]
    supervisor_comment: Optional[str]
    admin_id: Optional[int]
    admin_comment: Optional[str]
    timestamps: dict

class Material:
    id: int
    name: str
    unit: str
    current_stock: float

class MaterialUsage:
    id: int
    material_id: int
    quantity_used: float
    daily_report_id: int

class Inventory:
    id: int
    material_id: int
    quantity: float
    last_updated: datetime

class AuditLog:
    id: int
    action: str
    user_id: int
    target_type: str
    target_id: int
    timestamp: datetime
    details: Optional[str]
