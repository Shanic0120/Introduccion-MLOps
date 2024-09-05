from fastapi import FastAPI
from .app.models import PredictionResponse, PredictionRequest
from .app.views import predict

app = FastAPI()

@app.post("/api/predict/")
def make_model_prediction(request: PredictionRequest):
    return PredictionResponse(HiringDecision=predict(request))

# uvicorn api.main:app --reload