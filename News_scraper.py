import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = []

for h in soup.find_all(["h2", "h3"]):
    text = h.get_text(strip=True)
    if text and len(text) > 15:
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines, 1):
        file.write(f"{i}. {headline}\n")

print(" Headlines scraped and saved to 'haedlines.txt'")
