# SQLAlchemy database setup
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Example: postgresql://postgres:password@db.host:5432/postgres
SQLALCHEMY_DATABASE_URL = os.getenv("SUPABASE_DB_URL", "sqlite:///./lsw.db")

# Create engine with connection pooling and timeout settings
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"connect_timeout": 30},
    pool_pre_ping=True,
    pool_recycle=3600
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
