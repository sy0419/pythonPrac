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
    if response.status_code >=200 and response.status_code < 300:
        results[website] = "OK"
    elif response.status_code >= 300 and response.status_code < 400:
        results[website] = "REDIRECT"
    elif response.status_code >= 400 and response.status_code < 500:
        results[website] = "ERROR"
    else:
        results[website] = "FAILED"
    
print(results)