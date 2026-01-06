from fastapi import APIRouter, Query
from services.fetch_jobs_list import fetch_jobs_list
from services.fetch_job_details import fetch_job_details
from core.constants import BASE_URL, HEADERS, PARAMS

jobs_router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@jobs_router.get("/scrape")
async def scrape_jobs(pages: int = 3, time_delta: int = 86400):
    return await fetch_jobs_list(
        BASE_URL,
        HEADERS.copy(),
        PARAMS.copy(),
        pages,
        time_delta
    )

@jobs_router.get("/fetch-details")
async def extract_job_details(
    url: str = Query(..., description="Target URL")
):
    return await fetch_job_details(
        url,
        HEADERS.copy()
    )
