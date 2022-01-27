import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def parsernaked_science(back_post_url2):
    s = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    driver = webdriver.Chrome(service=s, options=options)

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