import requests
import time
import datetime
from bs4 import BeautifulSoup
import tkinter
from tkinter import messagebox


break_loop = False

hours = 0

url = "https://arvutitark.ee/est/tracking/ER34AFJTTT"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

print(
    f"\nStarted tracking the status at {date_time}\nURL: https://arvutitark.ee/est/tracking/ER34AFJTTT\n")


def check_status():
    global break_loop

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    status = soup.find_all("td", valign="top")[5].text

    print(f"Checking status..")

    print(f"Current status: {status}\n")

    if status != "Tellimata":
        print(f"<!-- PRODUCT STATUS HAS CHANGED --!>")
        show_popup()

        break_loop = True


def show_popup():
    root = tkinter.Tk()
    root.withdraw()

    messagebox.showinfo("Arvutitark", "Product status has changed!")


while True:
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"\nChecked price at {date_time} ({hours} hours)")

    check_status()

    if break_loop:
        print("Stopped the tracker.")
        break

    time.sleep(3600)
    hours += 1
