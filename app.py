import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import messagebox

# scraper setup
total_pages = 5
url_num = 1
url_num_str = str(url_num)
url = f"https://theninenine.com/quotes/top/{url_num_str}/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

print("STARTED SCRAPING..")

while url_num != total_pages + 1:
    url_num_str = str(url_num)
    url = f"https://theninenine.com/quotes/top/{url_num_str}/"

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    print(f"ON PAGE {url_num_str}/{total_pages}")

    # save quotes to quotes.py
    for quote_div in soup.find_all("div", class_="quotesBody"):
        quote = quote_div.find("p").text
        if len(quote) <= 280:
            print(f"'''{quote}''',", file=open("./quotes.py", "a"))

    url_num += 1

print("FINISHED SCRAPING")
