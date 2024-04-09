from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.amazon.co.uk/KOORUI-FreeSync-Mountable-2560x1440-DisplayPort/dp/B0BBMPF6PT/ref=sr_1_1_sspa?crid=PX5LA2SZH4GT&dib=eyJ2IjoiMSJ9.KYgdzfdM9DBR5KeDyOlCN_R-rO27t13prVO0KXIbIXsEeh9om3rqHp3fBO535N8o94JkEbZoaPDbDPHQogNNnyLj2VGTL00dxLWzC373NQjrMc7Jlyrktlq4NJ9uLJdJ2MsXfx5Arpl_V_8142AjptwtGPWgzk7puCGsNNZ2PitvIx0G9JmKYDGz8s0u7TMa5J_Ign-Y3wXV-sB1zDtNJFvG4IHFlkH5mIXu8uB-qR0.6dT_QzC6qB39ncrL2pluFQZIPeiZLoWlZwdguYDViw8&dib_tag=se&keywords=144hz+monitor&qid=1712143384&sprefix=%2Caps%2C50&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

driver = webdriver.Chrome(options=chrome_options)
driver.get(f"{URL}")

price_pounds = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_pences = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is: {price_pounds.text}.{price_pences.text}")

driver.close()
