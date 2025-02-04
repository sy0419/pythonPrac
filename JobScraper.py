import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-back-end-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# jobs = soup.find("section", id="category-18")

jobs = soup.find("section", class_="jobs").find_all("li")

print(jobs)