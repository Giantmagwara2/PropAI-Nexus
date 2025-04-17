# /backend/agents/currency_conversion_agent.py

class CurrencyConversionAgent:
    def __init__(self):
        self.rates = {
            "USD": 1.0,
            "ZAR": 18.2,
            "EUR": 0.92,
            # More rates could be dynamically fetched later
        }

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Convert an amount from one currency to another.
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Unsupported currency.")

        usd_amount = amount / self.rates[from_currency]
        converted_amount = usd_amount * self.rates[to_currency]
        return round(converted_amount, 2)
