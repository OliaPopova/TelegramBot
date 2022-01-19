# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import meduza
import nplus1
import telebot
import requests
from bs4 import BeautifulSoup

token = "5084782927:AAHXpO6WaA8uuXQCNl1Cwm9okbNjFfSTW1s"
id_channel = "@news2k22botnews"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types= ["text"])
def commands(message):
    if message.text == "Старт":
        back_post_url = None
        back_post_id = None
        while True:
            post_text_nplus1 = nplus1.parsernplus1(back_post_id)
            back_post_id = post_text_nplus1[1]
            if post_text_nplus1[0] != None:
                bot.send_message(id_channel, post_text_nplus1[0])
                time.sleep(60)
            post_text_meduza= meduza.parsermeduza(back_post_url)
            back_post_url = post_text_meduza[1]
            if post_text_meduza[0] != None:
                bot.send_message(id_channel, post_text_meduza[0])
                time.sleep(60)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Старт")

bot.polling(none_stop=True, interval=0)