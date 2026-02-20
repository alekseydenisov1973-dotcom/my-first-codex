import requests
from config import KEYWORDS, CAREER_PATHS

def check_company_jobs(company, base_url):
    results = []

    if not isinstance(base_url, str) or base_url.strip() == "":
        return results

    base_url = base_url.rstrip("/")

    for path in CAREER_PATHS:
        url = base_url + path

        try:
            response = requests.get(url, timeout=5)
            text = response.text.lower()

            if any(keyword in text for keyword in KEYWORDS):
                results.append(url)

        except Exception:
            continue

    return results
