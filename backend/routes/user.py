# Placeholder for user routes (authentication, user management)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from models.models import User
from schemas import UserCreate, UserOut
from utils import get_password_hash

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# Admin creates a new user
@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
	db_user = db.query(User).filter(User.username == user.username).first()
	if db_user:
		raise HTTPException(status_code=400, detail="Username already registered")
	hashed_password = get_password_hash(user.password)
	new_user = User(
		username=user.username,
		password_hash=hashed_password,
		role=user.role,
		supervisor_id=user.supervisor_id
	)
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user
