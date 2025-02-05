import requests
from bs4 import BeautifulSoup

url = "https://remoteok.com/remote-flutter-jobs"

response = requests.get(url,
                        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"})

soup = BeautifulSoup(response.content, "html.parser")

job_lists = soup.find("table", id="jobsboard").find_all("td")
print(job_lists)