from pydantic import BaseModel

class LogData(BaseModel):
    logs: str

class AnalysisResult(BaseModel):
    summary: str
