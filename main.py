import os
import telebot

bot = telebot.TeleBot("2055977464:AAFH43eSWHRWS5hPghaaehD6L9TSSpCfe6Y")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hᴇʟʟᴏ Tʜᴇʀᴇ👋, I ᴀᴍ [Sᴏᴘʜɪᴀ](https://t.me/The_Sophia_Bot) ʙᴏᴛ 🍑
I ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ꜰᴇᴍᴀʟᴇ ʙᴏᴛ. Yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ᴇᴀꜱɪʟʏ ᴀɴᴅ ꜱᴍᴏᴏᴛʜʟʏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ʜᴏᴍᴇ 🙋‍♀️
Hɪᴛ /help ᴛᴏ ꜰɪɴᴅ ᴍʏ ʟɪꜱᴛ ᴏꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴀɴᴅꜱ 🕹")
                 


@bot.message_handler(commands=["how"])
def send_message(message):
    bot.reply_message(message,"t.me/ImshZe")
    
bot.polling()
