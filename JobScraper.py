import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-back-end-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# jobs = soup.find("section", id="category-18")

jobs = soup.find("section", class_="jobs").find_all("li")[:-1]
all_jobs = []

for job in jobs:
    try:
        title = job.find("span", class_="title").text
        company, contract_type, region = job.find_all("span", class_="company")
        try:
            url = job.find('div', class_ = 'tooltip--flag-logo').next_sibling['href']
        except KeyError:
            url = 'You need log-in'
        job_data = {
            "title": title,
            "company": company.text,
            "contract_type": contract_type.text,
            "region": region.text,
            "url": f"https://weworkremotely.com{url}"
        }
        all_jobs.append(job_data)
    except:
        pass

print(all_jobs)