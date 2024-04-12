from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        cookies_button = self.driver.find_element(By.ID, value="onetrust-reject-all-handler")
        time.sleep(2)

        cookies_button.click()
        time.sleep(1)

        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()
        time.sleep(45)

        self.up = float(self.driver.find_element(By.CLASS_NAME, value="result-data-large").text)
        print(f"Download Speed: {self.up}")
        self.down = float(self.driver.find_element(By.CLASS_NAME, value="upload-speed").text)
        print(f"Upload Speed: {self.down}")

    def tweet_at_provider(self):
        USERNAME = ""
        PASSWORD = ""

        self.driver.get("https://twitter.com/i/flow/login")
        print(self.driver.title)
        time.sleep(5)

        username = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(f"{USERNAME}")
        time.sleep(2)

        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(2)

        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(f"{PASSWORD}")
        time.sleep(3)

        login_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_button.click()
        time.sleep(4)

        message = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        message.send_keys("Hi, I'm new here looking forward to it!")
        time.sleep(2)

        post_message = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        post_message.click()


PROMISED_DOWN = 100
PROMISED_UP = 10

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if PROMISED_DOWN < bot.up or PROMISED_UP < bot.down:
    bot.tweet_at_provider()
