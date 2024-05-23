# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/UnZip-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UnZip-Bot



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup




@Client.on_message(filters.command("start"))
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔰 ᴜᴘᴅᴀᴛᴇ 🔰", url="https://t.me/synaxnetwork"),
            InlineKeyboardButton("🔰 ʙᴏᴛs 🔰", url="https://t.me/synaxbots")
        ],
        [
            InlineKeyboardButton("🇮🇳 sᴜᴘᴘᴏʀᴛ 🇮🇳", url="t.me/synaxchatgroup"),
            InlineKeyboardButton("🇮🇳 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🇮🇳", url="https://t.me/hhlokooo"),
        ] 
   ]
  )
    start_message = (
        "ʜᴇʟʟᴏ ᴍʏ ғᴀᴍɪʟʏ 🇮🇳💗\n\n"
        "sᴇɴᴅ ᴍᴇ ᴀ ᴢɪᴘ ғɪʟᴇ ᴀɴᴅ ɪ'ʟʟ ᴜɴᴢɪᴘ ɪᴛ ғᴏʀ ʏᴏᴜ.\n\n"
        "ᴍᴀᴅᴇ ʙʏ @synaxnetwork 🇮🇳💗"
    )
    await message.reply(start_message, reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def help_command(client, message):
    reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔰 ᴜᴘᴅᴀᴛᴇ 🔰", url="https://t.me/synaxnetwork"),
        ],
        [
            InlineKeyboardButton("🔰 ʙᴏᴛ 🔰", url="https://t.me/synaxbots"),
        ] 
   ]
  )
    help_message = (
        "ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ʏᴏᴜ ᴄᴀɴ ᴜsᴇ :\n\n"
        "© /start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ɢᴇᴛ ᴛʜᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ.\n"
        "© /help - ɢᴇᴛ ʜᴇʟᴘ ᴏɴ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ.\n\n"
        "✰ ᴛᴏ ᴜɴᴢɪᴘ ᴀ ғɪʟᴇ , sɪᴍᴘʟʏ sᴇɴᴅ ᴍᴇ ᴀ ᴢɪᴘ ғɪʟᴇ ᴀɴᴅ ɪ ᴡɪʟʟ ᴇxᴛʀᴀᴄᴛ ɪᴛs ᴄᴏɴᴛᴇɴᴛs ᴀɴᴅ sᴇɴᴅ ᴛʜᴇᴍ ʙᴀᴄᴋ ᴛᴏ ʏᴏᴜ ✰\n\n"
        "➳ ᴏᴡɴᴇʀ : @sanatanisynax ❤️"
    )
    await message.reply(help_message, reply_markup=reply_markup)

