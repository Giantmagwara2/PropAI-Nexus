# /backend/tasks/__init__.py
import json
from datetime import datetime
from pathlib import Path
# /backend/tasks/__init__.py

from .log_prediction_task import log_prediction

__all__ = [
    "log_prediction",
]


# Log file path
LOG_FILE = Path("logs/predictions.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)  # Ensure 'logs/' exists

async def log_prediction(data: dict):
    """
    Logs prediction data to a local file with timestamp.
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": data.get("input"),
        "output": data.get("output")
    }

    try:
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        # Optionally print/log this error somewhere else
        print(f"Logging failed: {e}")
