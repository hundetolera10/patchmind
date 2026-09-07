from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "PatchMind API",
        "version": "0.1.0"
    }