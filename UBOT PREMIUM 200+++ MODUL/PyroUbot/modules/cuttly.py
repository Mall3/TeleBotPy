import random
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import Message
from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴄᴜᴛᴛʟʏ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴜᴛᴛʟʏ ⦫</b>

<blockquote><b>⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}cuttly</code> link

⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:
ᚗ Memperpendek url link yang panjang</blockquote>
"""

@PY.UBOT("cuttly")
async def _(client, message):
    if len(message.command) < 2:
        await message.reply_text("<blockquote><b>**Gunakan perintah:** `/cuttly url`\n\nContoh: `/cuttly https://www.google.co.id`</blockquote></b>")
        return

    url = " ".join(message.command[1:])
    api_url = f"https://api.botcahx.eu.org/api/linkshort/cuttly?link={url}&apikey=moire"

    try:
        response = requests.get(api_url).json()

        if response.get("status"):
            title_res = response["result"]["title"].title()
            status_res = response["result"]["status"]
            date_res = response["result"]["date"]
            shortLink_res = response["result"]["shortLink"]
            fullLink_res = response["result"]["fullLink"]      

            reply_text = (
                f"<blockquote><b>**🪧 Title Link : {title_res}**\n\n</blockquote></b>"
                f"<blockquote><b>📟 Status : {status_res}\n</blockquote></b>"
                f"<blockquote><b>🗓️ Date : {date_res}\n</blockquote></b>"
                f"<blockquote><b>💫 ShortLink : {shortLink_res}\n</blockquote></b>"
                f"<blockquote><b>🌐 FullLink : {fullLink_res}\n</blockquote></b>"                                                
            )


            await message.reply_text(reply_text)
        else:
            await message.reply_text(f"<blockquote><b>❌ Maaf, Title dari **{title}** tidak ditemukan.</blockquote></b>")
    except Exception as e:
        await message.reply_text(f"<blockquote><b>⚠️ Terjadi kesalahan saat mengambil data:\n`{str(e)}`</blockquote></b>")
