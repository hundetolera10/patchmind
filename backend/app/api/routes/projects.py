from fastapi import APIRouter
from app.schemas.project import ProjectCreate

router = APIRouter()

@router.get("/projects")
def list_projects(language: str | None = None):
    return {
        "language_filter": language,
    }

@router.get("/projects/{project_id}")
def get_project(project_id: int):
    return {
        "project_id": project_id,   
        "message":"project found"
    }

@router.post("/projects")
def create_project(project: ProjectCreate):
    return {
        "id": 1,
        "message": "project created",
        "project": project,
    }