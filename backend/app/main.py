from fastapi import FastAPI
from app.api.routes import projects, health, analysis


app = FastAPI(
    title="PatchMind API",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(projects.router)
app.include_router(analysis.router)


@app.get("/")
def root():
    return{
        "name": "PatchMind",
        "status": "running",
        "version": "0.1.0",
    }


    