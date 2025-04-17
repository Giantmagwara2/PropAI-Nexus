# /backend/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./predictions.db"  # 🔥 (You can later switch to PostgreSQL easily.)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # SQLite-specific
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
