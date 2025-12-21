from fastapi import FastAPI
from routes.fetch_jobs import jobs_router
from routes.fetch_resume import resume_router

app = FastAPI(title="Job Ingestion Service")

app.include_router(jobs_router)
app.include_router(resume_router)