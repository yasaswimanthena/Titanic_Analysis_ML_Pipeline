from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import uvicorn

# Load the trained model
with open("best_rf_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Initialize FastAPI app
app = FastAPI()

# Define input schema (Add the missing features!)
class ModelInput(BaseModel):
    pclass: int
    age: float
    sibsp: int
    parch: int
    fare: float
    embarked: int
    sex: int
    cabin: int  # Example missing feature (Convert categorical to numeric)
    ticket: int  # Example missing feature (If used in training)
    body: int  # Example missing feature
    home_dest: int  # Example missing feature
    boat: int  # Example missing feature

# API Home Route
@app.get("/")
def home():
    return {"message": "Titanic Survival Prediction API is running!"}

# Prediction Endpoint
@app.post("/predict")
def predict(data: ModelInput):
    # Convert input into numpy array
    features = np.array([[data.pclass, data.age, data.sibsp, data.parch, 
                          data.fare, data.embarked, data.sex, 
                          data.cabin, data.ticket, data.body, data.home_dest, data.boat]])
    
    # Make prediction
    prediction = model.predict(features)
    
    # Return prediction result
    return {"prediction": int(prediction[0])}

# Run the API server (for local execution)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
