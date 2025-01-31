from requests import get

websites = (
    "www.google.com",
    "https://www.naver.com",
    "www.daum.net",
    "https://www.nate.com",
    "www.python.org"
)

results = {

}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        results[website] = "OK"
    else:
        results[website] = "FAILED"
    
print(results)