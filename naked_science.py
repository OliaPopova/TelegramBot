import os
from bs4 import BeautifulSoup
from selenium import webdriver

def parsernaked_science(back_post_url2):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)

    URL = "https://naked-science.ru/article/hi-tech"
    driver.get(URL)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    post = soup.find('li', class_='sidebar-block-item')
    url = post.find("a", href=True)["href"].strip()

    if url != back_post_url2:
        title = post.find("div", class_="sidebar-block-item-title").select('h3')[0].get_text()
        driver.close()
        return f"{title}\n\n{url}", url
    else:
        driver.close()
        return None, url