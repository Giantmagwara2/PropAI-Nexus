# /backend/tasks.py

from db.session import SessionLocal
from models.prediction_log import PredictionLog

def log_prediction(log_data: dict):
    db = SessionLocal()
    try:
        log = PredictionLog(
            input_data=log_data["input"],
            predicted_value=log_data["output"],
            currency=log_data.get("currency", "USD")
        )
        db.add(log)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Logging failed: {str(e)}")
    finally:
        db.close()
