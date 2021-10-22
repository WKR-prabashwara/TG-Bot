import os
import telebot

bot = telebot.TeleBot("2055977464:AAFH43eSWHRWS5hPghaaehD6L9TSSpCfe6Y")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hᴇʟʟᴏ Tʜᴇʀᴇ👋, I ᴀᴍ [Sᴏᴘʜɪᴀ](https://t.me/The_Sophia_Bot) ʙᴏᴛ 🍑
I ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ꜰᴇᴍᴀʟᴇ ʙᴏᴛ. Yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ᴇᴀꜱɪʟʏ ᴀɴᴅ ꜱᴍᴏᴏᴛʜʟʏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ʜᴏᴍᴇ 🙋‍♀️
Hɪᴛ /help ᴛᴏ ꜰɪɴᴅ ᴍʏ ʟɪꜱᴛ ᴏꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴀɴᴅꜱ 🕹 
                 buttons = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 💬", url="https://t.me/BoTupdateZone"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 👥", url="https://t.me/tgzoNechat"),
    ],
    [
        InlineKeyboardButton(text="ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📜", url="https://github.com/WKRPrabashwara/Sophia_Bot"),
        InlineKeyboardButton(text="ʜᴇʟᴘ ❔", url="http://t.me/The_Sophia_Bot?start=help"),
    ],
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ 👨‍💻", url="https://t.me/ImshZe"),
    ],
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴀɴᴋɪ ᴠᴇᴄᴛᴏʀ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="t.me/The_Sophia_Bot?startgroup=true"
        ),
    ],
]")
                 


@bot.message_handler(commands=["how"])
def send_message(message):
    bot.reply_message(message,"t.me/ImshZe")
    
bot.polling()
