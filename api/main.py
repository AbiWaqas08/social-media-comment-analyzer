from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Sentiment API is running!"}

@app.post("/predict/")
def predict_sentiment(data: TextInput):
    text_vector = vectorizer.transform([data.text])
    pred = model.predict(text_vector)[0]
    label = label_encoder.inverse_transform([pred])[0]
    return {"prediction": label}
