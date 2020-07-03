import requests
import time
import datetime
from bs4 import BeautifulSoup
import tkinter
from tkinter import messagebox


hours = 0

url = "https://arvutitark.ee/est/tracking/ER34AFJTTT"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

print(
    f"\nStarted tracking the status at {date_time}\nURL: https://arvutitark.ee/est/tracking/ER34AFJTTT\n")


def check_status():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    status = soup.find_all("td", valign="top")[2]

    print(f"CHECKING STATUS..")

    if status != "Tellimatta":
        print(f"PRODUCT STATUS HAS CHANGED")
        show_popup()


def show_popup():
    root = tkinter.Tk()
    root.withdraw()

    messagebox.showinfo("Arvutitark", "Product status has changed!")


while True:
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Checked price at {date_time} ({hours} hours)")
    check_status()
    time.sleep(3600)
    hours += 1
