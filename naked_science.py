import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:/Users/User/.wdm/drivers/chromedriver/win32/97.0.4692.71/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('headless')  # для открытия headless-браузера
driver = webdriver.Chrome(service=s, options=options)

def parsernaked_science(back_post_url2):

    URL = "https://naked-science.ru/article/hi-tech"
    driver.get(URL)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    post = soup.find('li', class_='sidebar-block-item')
    url = post.find("a", href=True)["href"].strip()

    if url != back_post_url2:
        title = post.find("div", class_="sidebar-block-item-title").select('h3')[0].get_text()
        return f"{title}\n\n{url}", url
    else:
        return None, url