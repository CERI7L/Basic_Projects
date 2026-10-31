from bs4 import BeautifulSoup
from pathlib import Path


def scrape_mock_jobs(file_path: str) -> list[dict]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Could not find file: {path}")

    html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    jobs = []

    for card in soup.select(".job-card"):
        title_tag = card.select_one(".title")
        company_tag = card.select_one(".company")
        location_tag = card.select_one(".location")
        link_tag = card.select_one(".apply-link")

        job = {
            "title": title_tag.get_text(strip=True) if title_tag else "",
            "company": company_tag.get_text(strip=True) if company_tag else "",
            "location": location_tag.get_text(strip=True) if location_tag else "",
            "link": link_tag["href"] if link_tag and link_tag.has_attr("href") else "",
            "source": "mock_html",
        }

        jobs.append(job)

    return jobs


if __name__ == "__main__":
    scraped_jobs = scrape_mock_jobs("sample_data/mock_jobs.html")

    for job in scraped_jobs:
        print(job)