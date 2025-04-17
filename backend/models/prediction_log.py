# /backend/models/prediction_log.py

from sqlalchemy import Column, Integer, String, Float, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(JSON, nullable=False)
    predicted_value = Column(Float, nullable=False)
    currency = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
