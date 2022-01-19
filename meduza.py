import requests
from bs4 import BeautifulSoup

def parsermeduza(back_post_url):
    URL = "https://meduza.io/"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("article", class_="RichBlock-root RichBlock-isMobile RichBlock-isRich")
    url = post.find("a", class_="Link-root Link-isInBlockTitle", href=True)["href"].strip()

    if url != back_post_url:
        title = post.find("h2", class_="BlockTitle-first").text.strip()
        return f"{title}\n\n{URL + url}", url
    else:
        return None, url