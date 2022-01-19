import requests
from bs4 import BeautifulSoup

def parserhightech(back_post_url):
    URL = "https://hightech.fm/rubrics/tehnologii"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    post = soup.find("div", class_="news-feed__grid")
    url = post.find("a", href=True)["href"].strip()

    if url != back_post_url:
        title = post.find("h2", class_="entry__title title title--size_sm truncate truncate--md").text.strip()
        return f"{title}\n\n{url}", url
    else:
        return None, url