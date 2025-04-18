# /backend/agents/risk_assessment_agent.py

class RiskAssessmentAgent:
    def __init__(self):
        self.risk_thresholds = {
            "high_price_threshold": 500000,
            "low_rental_yield_threshold": 5.0,
            "market_risk_factor": 1.2  # 1 = neutral, >1 = riskier
        }

    def assess_property(self, property_info):
        """
        Analyze individual property risk based on price, rental yield, and market risk.
        """
        risk_score = 0

        if property_info["price"] > self.risk_thresholds["high_price_threshold"]:
            risk_score += 2  # Price too high = riskier investment

        if property_info["rental_yield"] < self.risk_thresholds["low_rental_yield_threshold"]:
            risk_score += 3  # Low rental returns = big risk

        market_factor = property_info.get("market_risk_factor", 1.0)
        if market_factor > self.risk_thresholds["market_risk_factor"]:
            risk_score += 2  # Market instability

        return {
            "property_id": property_info.get("id", "N/A"),
            "risk_score": risk_score,
            "risk_level": self._categorize_risk(risk_score)
        }

    def _categorize_risk(self, score):
        if score <= 2:
            return "Low"
        elif score <= 4:
            return "Moderate"
        else:
            return "High"

    def run_batch_assessment(self, properties):
        """
        Assess multiple properties at once.
        """
        return [self.assess_property(prop) for prop in properties]

# Optional manual run
if __name__ == "__main__":
    agent = RiskAssessmentAgent()
    sample_properties = [
        {"id": "P001", "price": 480000, "rental_yield": 6.2, "market_risk_factor": 1.1},
        {"id": "P002", "price": 600000, "rental_yield": 4.5, "market_risk_factor": 1.3},
    ]
    assessments = agent.run_batch_assessment(sample_properties)
    for a in assessments:
        print(a)
