import os
import telebot

bot = telebot.TeleBot("2055977464:AAFH43eSWHRWS5hPghaaehD6L9TSSpCfe6Y")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hᴇʟʟᴏ Tʜᴇʀᴇ👋, I ᴀᴍ Sᴏᴘʜɪᴀ ʙᴏᴛ 🍑")

@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "t.me/ImshZe")
    
bot.polling()
