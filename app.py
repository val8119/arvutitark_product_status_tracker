import requests
import time
import datetime
from bs4 import BeautifulSoup
import win32api


print("Enter your product tracking URL:")
url = input("> ").strip()

print("Enter the delay in seconds (eg. 3600 = 1 hour):")
delay = int(input("> "))

old_status = ""
current_status = ""

break_loop = False

check_count = 0

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

print(
    f"\nStarted tracking the status at {date_time}\nURL: https://arvutitark.ee/est/tracking/ER34AFJTTT\n")


def check_status():
    global break_loop, old_status, current_status, url

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    current_status = soup.find_all("td", valign="top")[5].text

    print(f"Checking status..")

    print(f"Current status: {current_status}\n")

    if current_status != old_status:
        print("<!-- PRODUCT STATUS HAS CHANGED --!>")
        print(f"New status: {current_status}")

        show_popup(current_status)

        if current_status == "esinduses":
            break_loop = True

    old_status = current_status


def show_popup(status):
    win32api.MessageBox(
        0, f"The product status has changed!\nNew status: {status}", "Arvutitark", 0x00001000)


while True:
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    check_count += 1

    print(f"\nChecked price at {date_time} ({check_count} time(s))")

    check_status()

    if break_loop:
        print("The product has arrived.\nStopping the tracker.")
        break

    time.sleep(delay)
