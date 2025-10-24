from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ϙᴜᴏᴛᴇs sᴜᴋᴜ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ϙᴜᴏᴛᴇs sᴜᴋᴜ ⦫<b>

<blockquote>⎆ perintah :
ᚗ <code>{0}qjawa</code>
⊷ Quotes Jawa

ᚗ <code>{0}qminang</code>
⊷ Quotes Jawa

ᚗ <code>{0}qsunda</code>
⊷ Quotes Jawa

ᚗ <code>{0}qbatak</code>
⊷ Quotes Jawa

</blockquote>
"""

@PY.UBOT("qjawa")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
       prs = await message.reply_text(f"<emoji id=4943239162758169437>🤩</emoji> Menjawab....")
       response = requests.get(f'https://api.botcahx.eu.org/api/random/quotesjawa?apikey=moire')

       try:
          if "quotes" in response.json():
             x = response.json()["quotes"]                  
             await prs.edit(
                 f"<blockquote>{x}</blockquote>"
                 )

          else:
               await message.reply_text("No 'results' key found in the response.")
       except KeyError:
            await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")

@PY.UBOT("qminang")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
       prs = await message.reply_text(f"<emoji id=4943239162758169437>🤩</emoji> Menjawab....")
       response = requests.get(f'https://api.botcahx.eu.org/api/random/minangkabau?apikey=moire')

       try:
          if "hasl" in response.json():
             x = response.json()["hasl"]                  
             await prs.edit(
                 f"<blockquote>{x}</blockquote>"
                 )

          else:
               await message.reply_text("No 'results' key found in the response.")
       except KeyError:
            await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")

@PY.UBOT("qsunda")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
       prs = await message.reply_text(f"<emoji id=4943239162758169437>🤩</emoji> Menjawab....")
       response = requests.get(f'https://api.botcahx.eu.org/api/random/sunda?apikey=moire')

       try:
          if "hasl" in response.json():
             x = response.json()["hasl"]                  
             await prs.edit(
                 f"<blockquote>{x}</blockquote>"
                 )

          else:
               await message.reply_text("No 'results' key found in the response.")
       except KeyError:
            await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")

@PY.UBOT("qbatak")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
       prs = await message.reply_text(f"<emoji id=4943239162758169437>🤩</emoji> Menjawab....")
       response = requests.get(f'https://api.botcahx.eu.org/api/random/batak?apikey=moire')

       try:
          if "hasl" in response.json():
             x = response.json()["hasl"]                  
             await prs.edit(
                 f"<blockquote>{x}</blockquote>"
                 )

          else:
               await message.reply_text("No 'results' key found in the response.")
       except KeyError:
            await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
