import time
import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')


class HouseSearch:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.get_information()

    def get_information(self):
        zillow_end_point = "https://appbrewery.github.io/Zillow-Clone/"

        response = requests.get(url=zillow_end_point)
        response.raise_for_status()

        # Links to the addresses of home
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        links = soup.select(selector=".StyledPropertyCardDataArea-anchor")

        self.links_to_properties = [link.get("href") for link in links]
        self.addresses = [address.text.replace("|", "").strip().replace("#", "") for address in links]

        # Prices to the addresses of home
        prices = soup.select(selector=".PropertyCardWrapper__StyledPriceLine")

        one_clean_section_by_plus = [price.text.split("+")[0] for price in prices]
        self.second_clean_section_by_symbol = [symbol.split("/")[0] for symbol in one_clean_section_by_plus]

    def fill_the_form(self):
        for i in range(0, len(self.second_clean_section_by_symbol)):
            self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLScMuydxX12B2mUzmQ5M27_quuVr9hlI0e5HArOWA73haDdfpA"
                            "/viewform?usp=sf_link")
            address_field = self.driver.find_element(By.XPATH,
                                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(1)
            address_field.send_keys(f"{self.addresses[i]}"), Keys.TAB
            price_field = self.driver.find_element(By.XPATH,
                                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field.send_keys(f"{self.second_clean_section_by_symbol[i]}"), Keys.TAB
            link_field = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field.send_keys(f"{self.links_to_properties[i]}"), Keys.ENTER
            submit_button = self.driver.find_element(By.XPATH,
                                                     value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit_button.click()
            submit_another_response = self.driver.find_element(By.XPATH,
                                                               value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            submit_another_response.click()


if __name__ == "__main__":
    search = HouseSearch()
    search.fill_the_form()
