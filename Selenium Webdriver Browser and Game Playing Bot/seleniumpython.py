from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

dates = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
event_titles = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

formatted_dates = [date.get_attribute("datetime").split("T")[0] for date in dates]
formatted_names = [title.text for title in event_titles]

combined_data = {i+1: {'time': date, 'name': name} for i, (date, name) in enumerate(zip(formatted_dates, formatted_names))}
print(combined_data)
driver.quit()
