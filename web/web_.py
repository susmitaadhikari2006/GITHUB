from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import bs4
import re

DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome()
url = "https://www.google.com/maps/search/wendy's+near+cincinnati+oh"

driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
elements = driver.find_elements(By.XPATH, "//div[@class=\"y7PRA\"]")
print(len(elements))

rs = []
for e in elements:
    title = e.find_element(By.CSS_SELECTOR, "div.fontHeadlineSmall")
    address = e.find_element(By.CSS_SELECTOR, "div.W4Efsd > div.W4Efsd > span:nth-Child(2)")
    rs.append(str(title.text) + ", Address: " + str(address.text[2:]))

for s in rs:
    print(s + "\n")
driver.close()