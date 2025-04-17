# /backend/tasks.py

from backend.routes.metrics import metrics_agent

async def log_prediction(data: dict):
    try:
        output = data.get("output", {})

        if "predicted_price" in output:
            # Logging a property value prediction
            metrics_agent.log_property_prediction(output["predicted_price"])

        if "predicted_rental_yield_percent" in output:
            # Logging a rental yield prediction
            metrics_agent.log_rental_yield_prediction(output["predicted_rental_yield_percent"])

    except Exception as e:
        print(f"Error logging prediction: {e}")
