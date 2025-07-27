import requests
from bs4 import BeautifulSoup
import json

URL = "https://jiangranlv.github.io/robotics_arXiv_daily/"
OUTPUT_PATH = "robotics_arxiv_daily.json"

def scrape_and_save():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")[1:]  # skip header

    papers = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) != 5:
            continue
        date = cols[0].text.strip()
        title = cols[1].text.strip()
        authors = cols[2].text.strip()
        pdf_link = cols[3].find("a")["href"]
        pdf = cols[3].text.strip()
        code = cols[4].text.strip()
        papers.append({
            "date": date,
            "title": title,
            "authors": authors,
            "pdf": pdf,
            "pdfLink": pdf_link,
            "code": code
        })

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"papers": papers}, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    scrape_and_save()
