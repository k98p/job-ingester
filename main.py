from fastapi import FastAPI
from routes.fetch_jobs import jobs_router

app = FastAPI(title="Job Ingestion Service")

app.include_router(jobs_router)