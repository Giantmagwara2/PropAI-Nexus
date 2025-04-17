# /backend/models/metrics_agent.py

class MetricsAgent:
    def __init__(self):
        self.total_properties = 0
        self.total_estimated_value = 0.0
        self.total_rental_yield = 0.0
        self.rental_yield_predictions = 0

    def log_property_prediction(self, estimated_value: float):
        self.total_properties += 1
        self.total_estimated_value += estimated_value

    def log_rental_yield_prediction(self, rental_yield_percent: float):
        self.rental_yield_predictions += 1
        self.total_rental_yield += rental_yield_percent

    def get_metrics(self):
        avg_yield = (
            self.total_rental_yield / self.rental_yield_predictions
            if self.rental_yield_predictions > 0
            else 0
        )
        return {
            "total_properties_analyzed": self.total_properties,
            "total_estimated_value": round(self.total_estimated_value, 2),
            "average_rental_yield": round(avg_yield, 2),
            "active_predictions": self.total_properties,  # we can refine later if needed
        }
