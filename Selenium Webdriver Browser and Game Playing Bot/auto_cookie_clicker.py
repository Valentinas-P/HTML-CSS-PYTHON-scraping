import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

collect_cookies = driver.find_element(By.ID, value="cookie")
collected_cookies = int(driver.find_element(By.ID, value="money").text)

click_interval = 2  # Click interval in seconds
last_click_time = time.time()

timeout = 300
timeout_start = time.time()
click = True

while time.time() < timeout_start + timeout and click:

    collect_cookies.click()

    collected_cookies += 1

    # Check if it's time to click on cursor
    if time.time() - last_click_time >= click_interval:
        last_click_time = time.time()  # Update last click time
        expenses_menu = {
            "shipment": 7000,
            "mine": 2000,
            "factory": 500,
            "grandma": 100,
            "cursor": 23,
        }

        items_ids = {
            "shipment": "buyShipment",
            "mine": "buyMine",
            "factory": "buyFactory",
            "grandma": "buyGrandma",
            "cursor": "buyCursor"
        }

        # Iterate over items in the expenses menu
        for item, price in expenses_menu.items():
            if collected_cookies >= price and item in items_ids:
                print(f"Enough cookies to buy {item}")
                # Purchase the item
                item_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, items_ids[item])))
                item_element.click()
                # Subtract the cost of the item from collected_cookies
                collected_cookies -= price
                # Reset the click timer
                last_click_time = time.time() + 3
                break
    else:
        continue

cookies_per_sec = driver.find_element(By.ID, value="cps").text
print(cookies_per_sec)
