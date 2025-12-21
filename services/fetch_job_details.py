import asyncio
import httpx
from bs4 import BeautifulSoup
import json
import html

def filter_job(job_posting):
    q = job_posting.get("min_qualification")
    months = job_posting.get("months_of_experience")
    if q and q.lower() == 'bachelor degree' and months and (24 <= months <= 60):
        return True
    return False

async def enrich_job(httpclient, job_posting):
    try:
        url = job_posting["url"]
        response = await httpclient.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            script_tag = soup.find('script', type='application/ld+json')
            if script_tag:
                try:
                    data = json.loads(script_tag.string)
                except Exception:
                    return None
                job_posting["date_posted"] = data.get("datePosted")
                job_posting["job_description"] = html.unescape(data.get("description", ""))
                job_posting["min_qualification"] = data.get("educationRequirements", {}).get("credentialCategory")
                job_posting["months_of_experience"] = data.get("experienceRequirements", {}).get("monthsOfExperience")
                return job_posting
        else:
            print(f"Laude lag gaye because of {response}")
            print(response.text)
    except Exception as e:
        print("Laude lag gaye inside exception")
    return None

async def enrich_job_list(job_list):
    async with httpx.AsyncClient() as client:
        tasks = [enrich_job(client, job_posting) for job_posting in job_list]
        enriched_job_postings = await asyncio.gather(*tasks)
        print(enrich_job_list)
        return [enriched_job_posting for enriched_job_posting in enriched_job_postings if enriched_job_posting and filter_job(enriched_job_posting)]
    

async def fetch_job_details(job_url, headers):
    try:
        async with httpx.AsyncClient() as httpclient:
            response = await httpclient.get(job_url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                script_tag = soup.find('script', type='application/ld+json')
                code_tag = soup.find('code', id="applyUrl")
                if script_tag:
                    try:
                        data = json.loads(script_tag.string)
                    except Exception:
                        return None
                    title = data.get("title")
                    location = data.get("jobLocation", {}).get("address", {}).get("addressLocality")
                    org = data.get("hiringOrganization", {}).get("name")
                    date_posted = data.get("datePosted")
                    valid_through = data.get("validThrough")
                    employment_type = data.get("employmentType")
                    description_html = html.unescape(data.get("description", ""))
                    min_qualification = data.get("educationRequirements", {}).get("credentialCategory")
                    months_of_experience = data.get("experienceRequirements", {}).get("monthsOfExperience")
                    return {
                        "Kompany": org,
                        "Title": title,
                        "Location": location,
                        "Date Posted": date_posted,
                        "Valid Through": valid_through,
                        "employment_type": employment_type,
                        "job_description": description_html,
                        "min_qualification": min_qualification,
                        "months_of_experience": months_of_experience,
                        "linked_in_apply": job_url,
                        "external_apply": "NA" if not code_tag else code_tag.string
                    }
            else:
                print(f"Laude lag gaye because of {response}")
                print(response.text)
    except Exception as e:
        print(f"Laude lag gaye due to {e}")
    return None