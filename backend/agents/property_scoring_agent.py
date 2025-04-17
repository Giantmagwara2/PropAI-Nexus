# /backend/agents/property_scoring_agent.py

class PropertyScoringAgent:
    def __init__(self):
        pass

    def score_property(self, predicted_value: float, rental_yield: float, location: str) -> dict:
        """
        Score a property based on value, yield, and location.
        """
        investment_score = 0.5 * rental_yield + 0.5 * (predicted_value / 1000000)

        # Just a simple scoring formula for now
        return {
            "investment_score": round(investment_score, 2),
            "rating": "Excellent" if investment_score > 7 else "Good" if investment_score > 5 else "Average"
        }
