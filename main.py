import os
import telebot

bot = telebot.TeleBot("2055977464:AAFH43eSWHRWS5hPghaaehD6L9TSSpCfe6Y")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello There! I'm Prabshwara's Chat bot")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.reply_message(message,"t.me/ImshZe")
    
bot.polling()
