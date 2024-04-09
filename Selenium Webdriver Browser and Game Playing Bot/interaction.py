from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://en.wikipedia.org/wiki/Wiki"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

all_portals = driver.find_element(By.CSS_SELECTOR, value='#pt-createaccount-2 a')
all_portals.click()

search = driver.find_element(By.NAME, "wpName")
search.send_keys("Python")
