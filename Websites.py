websites = (
    "www.google.com",
    "https://www.naver.com",
    "www.daum.com",
    "https://www.nate.com",
    "www.python.com"
)

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)