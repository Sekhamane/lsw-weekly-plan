# Placeholder for authentication and role management logic
# To be implemented: JWT-based authentication, role-based access control


from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db import SessionLocal
from models.models import User, RoleEnum
from schemas import Token, UserOut
from utils import verify_password, get_password_hash, create_access_token, decode_access_token
from jose import JWTError
from typing import Optional

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate credentials",
		headers={"WWW-Authenticate": "Bearer"},
	)
	try:
		payload = decode_access_token(token)
		username: str = payload.get("sub")
		if username is None:
			raise credentials_exception
	except JWTError:
		raise credentials_exception
	user = db.query(User).filter(User.username == username).first()
	if user is None:
		raise credentials_exception
	return user

@router.post("/register", response_model=UserOut)
def register(user: UserOut, password: str, db: Session = Depends(get_db)):
	db_user = db.query(User).filter(User.username == user.username).first()
	if db_user:
		raise HTTPException(status_code=400, detail="Username already registered")
	hashed_password = get_password_hash(password)
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

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
	user = db.query(User).filter(User.username == form_data.username).first()
	if not user or not verify_password(form_data.password, user.password_hash):
		raise HTTPException(status_code=400, detail="Incorrect username or password")
	access_token = create_access_token(data={"sub": user.username, "role": user.role})
	return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
	return current_user
