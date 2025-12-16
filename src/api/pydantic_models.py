from pydantic import BaseModel
from typing import Any, Dict
class CustomerData(BaseModel):
    total_amount = float
    avg_amount = float
    transaction_count = int
    std_amount = float
    transaction_hour = float
    transaction_day = float
    transaction_month = float
    transaction_year = float
    def to_dataframe(self):
        import pandas as pd
        return pd.DataFrame([self.dict()])
    class PredictionResponse(BaseModel):
        risk_probability: float
        risk_label: int