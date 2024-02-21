import requests
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"
SEARCH_TERM = input("what do you wanna search?\n")
ua = UserAgent()
options = Options()
options.add_argument(f"user-agent={ua.random}")

driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com")

driver.implicitly_wait(10)

searchBox = driver.find_element(By.ID, "twotabsearchtextbox")
searchBox.send_keys(SEARCH_TERM, Keys.ENTER)
'''
searchBox.send_keys(SEARCH_TERM)
searchButton = driver.find_element(By.ID, "nav-search-submit-button")
searchButton.Click
'''
driver.implicitly_wait(3)
products = WebDriverWait(driver, 7).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
print(len(products))
for p in products:
    item = p.find_element(By.CSS_SELECTOR,"a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
    desc = item.find_element(By.CSS_SELECTOR, "span")
    print(desc.text, end="\n")
    
    price_parent = p.find_element(By.CSS_SELECTOR, "a.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
    price = price_parent.find_element(By.CSS_SELECTOR, "span.a-price-whole")
    print("$ " + price.text, end="\n")
driver.close()