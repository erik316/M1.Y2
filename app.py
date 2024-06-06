import config
import telebot
from random import choice

API_TOKEN = config.bot_token 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['joke'])

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    joke = choice(["What do You Call a Fish with No Eyes? A Fsh", "What do computers like to eat? Chips", ""])
    bot.reply_to(message, joke.text)

bot.infinity_polling()