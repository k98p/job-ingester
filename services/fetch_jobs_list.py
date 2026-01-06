import asyncio
import httpx
from bs4 import BeautifulSoup

async def fetch_job_list_paginated(httpclient, base_url, headers, params, page):
    try:
        params["start"] = str(page * 10)
        response = await httpclient.get(base_url, headers=headers, params=params)
        if response.status_code == 200:
            job_postings = []
            soup = BeautifulSoup(response.content, "lxml")
            for job_li in soup.select("li"):
                link_element = job_li.select_one('a[data-tracking-control-name="public_jobs_jserp-result_search-card"]')
                link = link_element["href"] if link_element else None
                sanitized_link = link.split('?',1)[0]
                title_element = job_li.select_one("h3.base-search-card__title")
                title = title_element.text.strip() if title_element else None
                company_element = job_li.select_one("h4.base-search-card__subtitle")
                company = company_element.text.strip() if company_element else None
                location_element = job_li.select_one("span.job-search-card__location")
                job_location = location_element.text.strip() if location_element else None
                job_postings.append({
                    "url": sanitized_link,
                    "title": title,
                    "company": company,
                    "job_location": job_location
                })
            return job_postings
    except Exception as e:
        print(f"Failed to load data for page: {page} due to {e}")
    return None

async def fetch_jobs_list(base_url: str, headers: dict, params: dict, pages: int, time_delta: int):
    async with httpx.AsyncClient() as client:
        params["f_TPR"] = f"r{time_delta}"
        tasks = [fetch_job_list_paginated(client, base_url, headers, params, page) for page in range(pages)]
        job_postings = await asyncio.gather(*tasks)
        return [jobs for paginated_job_list in job_postings if paginated_job_list for jobs in paginated_job_list]
