from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import story, job
from core.config import settings

app = FastAPI(
    title="My API",
    description="This is a sample API",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router, prefix=settings.API_PREFIX)
app.include_router(job.router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
