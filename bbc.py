import requests
from bs4 import BeautifulSoup

def parserbbc(back_post_url):

    URL = "https://www.bbc.com/news/technology"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("div", class_="gs-c-promo gs-t-News nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-c-promo--inline@m gs-c-promo--stacked@xxl gs-c-promo--flex")
    url = post.find("a",class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor", href=True)["href"].strip()

    if url != back_post_url:
        title = soup.select('h3')[0].get_text()
        return f"{title}\n\n{URL + url}", url
    else:
        return None, url