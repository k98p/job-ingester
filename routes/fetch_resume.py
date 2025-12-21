from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import PlainTextResponse
import httpx
import re

resume_router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

GCS_BASE_URL = "https://storage.googleapis.com/latex-resume-inputs"

FILENAME_REGEX = re.compile(r"^[a-zA-Z0-9._-]+\.tex$")

@resume_router.get("/fetch-base", response_class=PlainTextResponse)
async def fetch_base_resume(
    resume_file_name: str = Query("sample_resume.tex", description="LaTeX resume file name")
):
    # Validate filename
    if not FILENAME_REGEX.match(resume_file_name):
        raise HTTPException(status_code=400, detail="Invalid file name")

    url = f"{GCS_BASE_URL}/{resume_file_name}"

    timeout = httpx.Timeout(10.0)

    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.get(url)

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Resume file not found")

    if response.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail=f"GCS error: {response.status_code}"
        )

    # Force UTF-8 decoding
    response.encoding = "utf-8"

    return response.text
