from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

name = driver.find_element(By.NAME, value="fName")
name.send_keys("Testing", Keys.ENTER)

surname = driver.find_element(By.NAME, value="lName")
surname.send_keys("Python", Keys.ENTER)

email = driver.find_element(By.NAME, value="email")
email.send_keys("testing@gmail.com", Keys.ENTER)