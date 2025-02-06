import requests
from bs4 import BeautifulSoup

class JobScrape():
    def __init__(self):
        self.all_jobs = []

    def scrape(self, url):
        print(f"Scraping {url}...")
        response = requests.get(url,
                        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"})
        soup = BeautifulSoup(response.content, "html.parser")
        job_lists = soup.find("table", id="jobsboard").find_all("td", class_="company position company_and_position")
        for job_list in job_lists:
            try:
                title = job_list.find("h2", itemprop="title").text.strip()
                company = job_list.find("h3", itemprop="name").text.strip()
                list1 = job_list.find_all("div", class_="location")
                location = list1[0].text
                salary = list1[1].text
                job_data = {"title": title, "company": company, 
                             "location": location, "salary": salary}                
                self.all_jobs.append(f"{job_data}")
            except:
                pass
    
    def scrape_using_keywords(self, keyword):
        for keyword in keywords:
            url = f"https://remoteok.com/remote-{keyword}-jobs"
            self.scrape(url)
    
    def get_job_list(self):
        return self.all_jobs

scraper = JobScrape()
keywords = ["flutter"]
scraper.scrape_using_keywords(keywords)

print(scraper.get_job_list())
