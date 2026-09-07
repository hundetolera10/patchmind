from fastapi import APIRouter
from app.schemas.analysis import AnalysisRequest
from app.services.analyzer import queue_analysis

router = APIRouter()

@router.post("/analyze")
def analyze_repository(request: AnalysisRequest):
    return queue_analysis(request.repository_path)
        
