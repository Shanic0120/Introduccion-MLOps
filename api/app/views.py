from .models import PredictionRequest
from .utils import get_model, transform_to_dataframe
from pycaret.classification import predict_model

model = get_model()

def predict(request: PredictionRequest) -> int:
    data_to_predict = transform_to_dataframe(request)
    prediction = predict_model(model, data=data_to_predict)

    return prediction["prediction_label"][0]