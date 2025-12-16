from fastapi import FastAPI
import mlflow.pyfunc
from src.api.pydantic_models import  CustomerData, PredictionResponse

app = FastAPI(title='Credit Risk API')
MODEL_URL = "models:/BestModel/Production"
model = mlflow.pyfunc.load_model(MODEL_URL)


@app.get('/')
def health_check():
    return {"status": "API is running"}

@app.post('/predict', response_model=PredictionResponse)
def predict(data: CustomerData):
    df = data.to_dataframe()
    proba = model.predict_proba(df)[0][1]
    threshold = 0.5
    label = int(proba >= threshold)
    return PredictionResponse(risk_probability=float(proba), risk_label=label)