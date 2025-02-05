import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    print(f"Scrapping {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # jobs = soup.find("section", id="category-18")
    jobs = soup.find("section", class_="jobs").find_all("li")[:-1]

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

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))
     
total_page_number = get_pages("https://weworkremotely.com/remote-full-time-jobs?")

for x in range(total_page_number):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))