# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import naked_science
import nplus1
import telebot
import hightech

token = "5084782927:AAHXpO6WaA8uuXQCNl1Cwm9okbNjFfSTW1s"
id_channel = "@news2k22botnews"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types= ["text"])
def commands(message):
    if message.text == "Старт":
        bot.send_message(message.from_user.id, "Я запустился!")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Старт")
bot.polling()