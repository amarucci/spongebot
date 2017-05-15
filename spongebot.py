import telebot
import re
import random
from telebot import types
from secret_vars import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['spongify'])
def send_welcome(message):
    try:
        mix = lambda s: "".join((str.upper,str.lower)[i%2](ch) for i,ch in enumerate(s))
        new_message = mix(message.reply_to_message.text)

        bot.send_photo(
                message.chat.id, 
                caption=new_message,
                photo="https://usatftw.files.wordpress.com/2017/05/spongebob.jpg?w=1000&h=600&crop=1",
                reply_to_message_id=message.reply_to_message.message_id)
    except:
        print("too bad")

while True:
    try:
        bot.polling()
    except:
        pass
