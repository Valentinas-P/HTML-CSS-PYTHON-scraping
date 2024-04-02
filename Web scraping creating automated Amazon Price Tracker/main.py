import requests
from bs4 import BeautifulSoup
import lxml
import random, time
import smtplib
import os

my_email = os.environ["MY_EMAIL"]
password = os.environ["MY_PASSWORD"]

url = "https://www.amazon.in/Marks-Spencer-Regular-Shirt-T25_4197K_Khaki/dp/B09BQMY95J/ref=sr_1_1_sspa?keywords=shirt+for+men&qid=1665582604&qu=eyJxc2MiOiIxMS42NSIsInFzYSI6IjExLjkwIiwicXNwIjoiMTAuMjIifQ%3D%3D&sprefix=shirts%2Caps%2C514&sr=8-1-spons&psc=1"

amazon_header = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "DNT": "1",  # Do not track request header
    "Connection": "close"
}

timeout = 10

try:
    time.sleep(0.5 * random.random())

    # Set timeout parameter
    response = requests.get(url=url, headers=amazon_header, timeout=timeout)

    # Check if response is OK
    if response.status_code == 200:
        html_content = response.text
        print(html_content)

        soup = BeautifulSoup(response.content, "lxml")
        price = soup.select_one(selector=".a-offscreen").getText()
        price_without_currency = price.split("£")[1]
        price_with_float = float(price_without_currency)
        print(price_with_float)

        if price_with_float < 100:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="#########",
                    msg=f"Subject: Amazon Price Tracker (Monitor)\n\nThe price went down based of the "
                        f"original price take a look at the price now: {url}"
                )
    else:
        print(f"Failed to fetch URL: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
