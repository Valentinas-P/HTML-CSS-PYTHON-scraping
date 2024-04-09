from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib

my_email = "pythonchr@gmail.com"
password = "ural gtiy bosc kztc"


URL = "https://www.amazon.co.uk/KOORUI-Inch-Computer-Monitor-AdaptiveSync/dp/B0B2RCXTK9/ref=sr_1_2_sspa?crid=3260IWO8BP2PK&dib=eyJ2IjoiMSJ9.KYgdzfdM9DBR5KeDyOlCN_R-rO27t13prVO0KXIbIXv184Z1O2dqd-PgVYrqkygllANToxPfb_ud2cDVBSHCgHBSN04EemAc1gd08UH5Ja4Hrzmu4yasDC61eTeZHti9TTsJYooAV4NVaSpD3NjzBuxAKyrqIsZ9w0bkcbovAQZ2bxAIWZvgOr7_yaYYmrUQ23Db4gip9iVAHN1P_E49qQFnV46Q2hmy0qDY-PCVxHo.c8kF2pdpxzhyebq0LmvPbp4KMwlWBxZM2M705BBVKQw&dib_tag=se&keywords=144hz%2Bmonitor&qid=1712061812&sprefix=144%2Caps%2C56&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

pound_currency = driver.find_element(By.CLASS_NAME, value="a-price-whole")
pence_currency = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

price_currently = f"{pound_currency.text}.{pence_currency.text}"

looking_at_price = float(99)

if float(price_currently) > looking_at_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr="pythonchr@gmail.com",
            to_addrs="valiuncka@gmail.com",
            msg=f"Subject: Amazon Price Tracker (Monitor)\n\nThe price went down based of the "
                f"original price take a look at the price now it should be 99 pounds: {URL}"
        )

driver.quit()
