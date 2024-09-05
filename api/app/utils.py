from pydantic import BaseModel
from pandas import DataFrame
from pycaret.classification import load_model
def get_model():
    model = load_model("./models/final_model_20240824")
    return model

def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    transition_dictionary = {key:[value] for key, value in class_model.model_dump().items()}
    data_frame = DataFrame(transition_dictionary)
    return data_frame
