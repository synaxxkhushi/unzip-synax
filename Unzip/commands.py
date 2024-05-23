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
            InlineKeyboardButton("🇮🇳 ʜᴇʟᴘ 🇮🇳", callback_data="/help"),
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
    help_message = (
        "Here are the commands you can use:\n\n"
        "/start - Start the bot and get the welcome message\n"
        "/help - Get help on how to use the bot\n\n"
        "To unzip a file, simply send me a ZIP file and I will extract its contents and send them back to you.\n\n"
        "©️ Channel : @NT_BOT_CHANNEL"
    )
    await message.reply(help_message)
    
