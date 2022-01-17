import requests
from bs4 import BeautifulSoup

URL= "https://nplus1.ru/"

page= requests.get(URL)
soup= BeautifulSoup(page.content, "html.parser")

post= soup.find("article", class_='item item-main item-main- _exist-image')

title = post.find("div", class_="caption").text.strip()
description = "Пока только так"
url = post.find("a", href=True)["href"].strip()
for item in soup.find_all("a", href=url, attrs={"data-id": True}):
    print (URL+url)

