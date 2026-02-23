# Pydantic schemas for request/response validation
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None

class UserBase(BaseModel):
    username: str
    role: str
    supervisor_id: Optional[int]

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

class MaterialBase(BaseModel):
    name: str
    unit: str

class MaterialCreate(MaterialBase):
    current_stock: float

class MaterialOut(MaterialBase):
    id: int
    current_stock: float

class WeeklyPlanBase(BaseModel):
    assigned_to: int
    work_type: str
    receipt_number: Optional[str]
    order_number: Optional[str]
    for_stock: bool
    product_type: Optional[str]
    task_description: str
    target_quantity: int
    deadline: datetime

class WeeklyPlanCreate(WeeklyPlanBase):
    required_materials: List[int]

class WeeklyPlanOut(WeeklyPlanBase):
    id: int
    assigned_by: int
    status: str
    created_at: datetime
    accepted_at: Optional[datetime]

class DailyReportBase(BaseModel):
    weekly_plan_id: int
    task_worked_on: str
    quantity_completed: int
    progress_percent: float
    issues: Optional[str]
    materials_used: List[dict]

class DailyReportCreate(DailyReportBase):
    pass

class DailyReportOut(DailyReportBase):
    id: int
    user_id: int
    date: datetime
    status: str
    supervisor_id: Optional[int]
    supervisor_comment: Optional[str]
    admin_id: Optional[int]
    admin_comment: Optional[str]

class AuditLogOut(BaseModel):
    id: int
    action: str
    user_id: int
    target_type: str
    target_id: int
    timestamp: datetime
    details: Optional[str]
