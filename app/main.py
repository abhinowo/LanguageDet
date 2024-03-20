from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict, __version__ as model_version

# Create an instance of the FastAPI app
app = FastAPI()

# Define your model input schema
class InputData(BaseModel):
    text: str

# Define your model output schema
class OutputData(BaseModel):
    prediction: str

@app.get("/", response_model=dict)
def model_info():
    return {"model_version": model_version}

@app.get("/status", response_model=dict)
def status():
    return {"status": "OK"}

# Define your endpoint with the input and output schema
@app.post("/predict", response_model=OutputData)
def predict_sentiment(payload: InputData):
    sentiment = predict(payload.text)
    return {"prediction": sentiment}
