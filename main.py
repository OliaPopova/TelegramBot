# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import telebot
import requests
from bs4 import BeautifulSoup

token = "5084782927:AAHXpO6WaA8uuXQCNl1Cwm9okbNjFfSTW1s"
id_channel = "@news2k22botnews"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types= ["text"])

def commands(message):
    if message.text == "start":
        back_post_id=None
        while True:
            post_text = parser(back_post_id)
            back_post_id=post_text[1]
            print(post_text[0])
            if post_text[0]!=None:
                bot.send_message(id_channel, post_text[0])
                time.sleep(60)


    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши start")

def parser(back_post_id):
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



bot.polling()