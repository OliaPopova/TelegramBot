import requests
from bs4 import BeautifulSoup

def parserbbc(back_post_url):

    URL = "https://mashable.com/tech"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("div", class_="flex-1")
    url = post.find("a",class_=" block w-full text-lg font-bold leading-6 mt-2", href=True)["href"].strip()

    if url != back_post_url:
        title = soup.select('a')[0].get_text()
        return f"{title}\n\n{URL + url}", url
    else:
        return None, url