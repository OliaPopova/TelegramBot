import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def parsernaked_science(back_post_url2):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("C:/Users/User/.wdm/drivers/chromedriver/win32/97.0.4692.71/chromedriver.exe",
                              options=options)
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