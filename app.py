from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI(title="Sentiment Analysis API")

# Загружаем модель при старте
pipe = pipeline("text-classification",
                model="tabularisai/multilingual-sentiment-analysis",
                framework="pt")


class TextRequest(BaseModel):
    text: str


@app.post("/predict")
async def predict_sentiment(request: TextRequest):
    print(request.text)
    result = pipe(request.text)
    return {"text": request.text, "prediction": result[0]}


@app.get("/")
async def root():
    return {"message": "Sentiment Analysis API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
