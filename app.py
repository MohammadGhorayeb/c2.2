from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="API for analyzing sentiment in text using a pre-trained model",
    version="1.0.0"
)

# Load pre-trained sentiment analysis model
try:
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
except Exception as e:
    print(f"Error loading model: {e}")
    sentiment_analyzer = None

# Define request model
class TextInput(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "I really enjoyed this movie, it was fantastic!"
            }
        }

# Define response model
class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    score: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API"}

@app.post("/analyze", response_model=SentimentResponse)
def analyze_sentiment(input_data: TextInput):
    if sentiment_analyzer is None:
        raise HTTPException(status_code=503, detail="Model not available")
    
    if not input_data.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    try:
        result = sentiment_analyzer(input_data.text)[0]
        return SentimentResponse(
            text=input_data.text,
            sentiment=result["label"],
            score=result["score"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing sentiment: {str(e)}")

@app.get("/health")
def health_check():
    if sentiment_analyzer is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True) 