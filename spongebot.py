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
        if message.reply_to_message is None:
            new_message = mix(message.text.split(' ', 1)[1])
            reply_id = message.message_id
        else:
            new_message = mix(message.reply_to_message.text)
            reply_id = message.reply_to_message.message_id

        bot.send_photo(
                message.chat.id, 
                caption=new_message,
                photo="https://usatftw.files.wordpress.com/2017/05/spongebob.jpg?w=1000&h=600&crop=1",
                reply_to_message_id=reply_id)
    except:
        print("too bad")

while True:
    try:
        bot.polling()
    except:
        pass
