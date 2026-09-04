from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="PatchMind API",
    version="0.1.0",
)
class AnalysisRequest(BaseModel):
    repository_path: str = Field(min_length=1)

@app.post("/analyze")
def analyze_repository(request: AnalysisRequest):
    return {
        "repository_path": request.repository_path,
        
        "status": "queued",

    }

class ProjectCreate(BaseModel):
    name: str =Field(min_length=1, max_length=100)
    repository_path: str = Field(min_length=1,)
    language: str = Field(min_length=1, max_length=50)
    

@app.post("/projects")
def create_project(project: ProjectCreate):
    return {
        "id": 1,
        "message": "project received",
        "project": project,
    }

@app.get("/")
def root():
    return{
        "name": "PatchMind",
        "status": "running",
        "version": "0.1.0",
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
@app.get("/projects/{project_id}")
def get_project(project_id: int):
    return {
        "project_id": project_id,   
        "message":"project found"
    }
@app.get("/projects")
def list_projects(language: str | None = None):
    return {
        "language_filter": language,
    }