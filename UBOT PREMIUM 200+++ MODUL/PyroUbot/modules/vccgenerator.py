import requests
from pyrogram import Client, filters
from PyroUbot import *

__MODULE__ = "ᴠᴄᴄ ɢᴇɴᴇʀᴀᴛᴏʀ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴄ ɢᴇɴᴇʀᴀᴛᴏʀ ⦫</b>
<blockquote>⎆ perintah :
ᚗ <code>{0}vcc</code>
⊶ untuk membuat fake vcc</blockquote>
"""

@PY.UBOT("vcc")
async def generate_vcc(client, message):
    API_URL = "https://api.siputzx.my.id/api/tools/vcc-generator"
    params = {
        "type": "MasterCard",
        "count": 5
    }
    
    try:
        response = requests.get(API_URL, params=params)
        data = response.json()
        
        if data.get("status"):
            vcc_list = data.get("data", [])
            result = "<blockquote>**Generated VCCs:**\n"
            
            for vcc in vcc_list:
                result += f"\n💳 **Card Number:** `{vcc['cardNumber']}`\n"
                result += f"📅 **Exp Date:** `{vcc['expirationDate']}`\n"
                result += f"👤 **Holder:** `{vcc['cardholderName']}`\n"
                result += f"🔑 **CVV:** `{vcc['cvv']}`\n"
                result += "-------------------------</blockquote>"
            
            await message.reply_text(result)
        else:
            await message.reply_text("Gagal mengambil data VCC.")
    
    except Exception as e:
        await message.reply_text(f"Terjadi kesalahan: {e}")
