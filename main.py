from fastapi import FastAPI
from models import LogData, AnalysisResult
from ai_analyzer import analyze_logs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (for Flutter Web or mobile clients)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "LogSage backend is running"}

@app.post("/analyze", response_model=AnalysisResult)
def analyze(log_data: LogData):
    summary = analyze_logs(log_data.logs)
    return {"summary": summary}
