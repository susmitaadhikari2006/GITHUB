import requests
import bs4

url = "https://www.eastlandfairfield.com/o/hs/page/programs"
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

page = requests.get(url, headers=headers)

page.encoding = "utf-8"

title_start = page.text.find("<title>")+ len("<title>")
title_end = page.text.find("</title>")
soup = bs4.BeautifulSoup(page.text, "html.parser")
print(page.text[title_start:title_end])

images = soup.find_all("<h3>")
for i in images:
    print(i[3:2])
print(len(images))