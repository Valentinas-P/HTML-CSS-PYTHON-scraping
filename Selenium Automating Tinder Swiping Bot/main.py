from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

USERNAME = ""
PASSWORD = ""

URL = "https://tinder.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(1)

decline_button = driver.find_element(By.XPATH, value='//*[@id="c-945880602"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]/div')
decline_button.click()
time.sleep(1)

login_button = driver.find_element(By.XPATH, value='//*[@id="q1887506695"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()
time.sleep(1)

login_with_facebook = driver.find_element(By.XPATH, value='//*[@id="q159125619"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div/div')
login_with_facebook.click()
time.sleep(3)

cookies = input("Please press enter when you finished declining cookies: ")
time.sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

username = driver.find_element(By.XPATH, value='//*[@id="email"]')
username.send_keys(f"{USERNAME}", Keys.TAB)
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password.send_keys(f"{PASSWORD}", Keys.ENTER)
print("clicked")

wait_for_user = input("Please confirm this with clicking enter keyboard button when the confirmation of facebook is "
                      "done: ")
time.sleep(1)

driver.switch_to.window(base_window)
print(driver.title)

allow_button = driver.find_element(By.CLASS_NAME, value="lxn9zzn")
allow_button.click()
time.sleep(1)

notification_button = driver.find_element(By.CLASS_NAME, value="lxn9zzn")
notification_button.click()
time.sleep(3)

likes = 10

for i in range(0, likes):
    click_like_button = driver.find_element(By.XPATH, value='//*[@id="q1887506695"]/div/div['
                                                            '1]/div/div/main/div/div/div[1]/div/div[4]/div/div['
                                                            '4]/button')
    click_like_button.click()
    time.sleep(1)

