from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


MODEL_PATH = Path("models/random_forest_rul.joblib")

_artifact = None


def get_artifact():
    global _artifact

    if _artifact is None:
        _artifact = joblib.load(MODEL_PATH)

    return _artifact


app = FastAPI(
    title="Predictive Maintenance API",
    description="Remaining Useful Life prediction for NASA C-MAPSS FD001 engines.",
    version="0.1.0",
)


class EngineObservation(BaseModel):
    unit_id: int
    cycle: int

    setting_1: float
    setting_2: float

    sensor_2: float
    sensor_3: float
    sensor_4: float
    sensor_6: float
    sensor_7: float
    sensor_8: float
    sensor_9: float
    sensor_11: float
    sensor_12: float
    sensor_13: float
    sensor_14: float
    sensor_15: float
    sensor_17: float
    sensor_20: float
    sensor_21: float


class PredictionResponse(BaseModel):
    unit_id: int
    cycle: int
    predicted_rul: float


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": "RandomForestRegressor",
    }


@app.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict(observation: EngineObservation):
    artifact = get_artifact()

    model = artifact["model"]
    feature_columns = artifact["feature_columns"]

    input_data = observation.model_dump()

    unit_id = input_data.pop("unit_id")

    input_df = pd.DataFrame([input_data])

    X = input_df[feature_columns]

    predicted_rul = model.predict(X)[0]

    return {
        "unit_id": unit_id,
        "cycle": observation.cycle,
        "predicted_rul": round(float(predicted_rul), 2),
    }