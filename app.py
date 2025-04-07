from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="API for analyzing sentiment in text using a pre-trained model",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the frontend static files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

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
async def read_root():
    return FileResponse("frontend/index.html")

@app.post("/analyze", response_model=SentimentResponse)
def analyze_sentiment(input_data: TextInput):
    # Temporary mock response until we get transformers working
    return SentimentResponse(
        text=input_data.text,
        sentiment="POSITIVE" if "good" in input_data.text.lower() or "great" in input_data.text.lower() else "NEGATIVE",
        score=0.95
    )

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True) 