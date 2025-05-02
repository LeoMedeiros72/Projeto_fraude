from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model.joblib")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]
    return {"fraude": bool(prediction), "probabilidade": round(proba, 2)}
