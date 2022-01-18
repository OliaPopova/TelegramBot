import requests
from bs4 import BeautifulSoup
def parsernlus1(back_post_id):
    URL = "https://nplus1.ru/"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("article", class_='item item-main item-main- _exist-image')
    url = post.find("a", href=True)["href"].strip()
    for data_id in soup.find_all("a", href=url, attrs={"data-id": True}):
        post_id=data_id['data-id']

    if post_id != back_post_id:
        title = soup.select('h3')[0].get_text()

        url = post.find("a", href=True)["href"].strip()
        return f"{title}\n\n{URL+url}",post_id
    else:
         return None, post_id
