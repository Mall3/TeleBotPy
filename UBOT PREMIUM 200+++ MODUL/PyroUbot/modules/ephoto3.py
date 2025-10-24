import os
import requests
from PyroUbot import *

# Masukkan API Key Anda di sini
API_KEY = "moire"  # Ganti dengan API key yang benar

__MODULE__ = "ᴇᴘʜᴏᴛᴏ 3"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴇᴘʜᴏᴛᴏ 3 ⦫<b>

<blockquote>⎆ perintah :
ᚗ <code>{0}typo2</code> teks
⊷ membuat gambar dengan efek Typography 2.

ᚗ <code>{0}letters</code> teks
⊷ membuat gambar dengan efek Letters.

ᚗ <code>{0}cloth</code> teks
⊷ membuat gambar dengan efek Cloth.

ᚗ <code>{0}grafitti</code> teks
⊷ membuat gambar dengan efek Grafitti.

ᚗ <code>{0}gs</code> teks
⊷ membuat gambar dengan efek Galaxy Stone.

ᚗ <code>{0}sunlight</code> teks
⊷ membuat gambar dengan efek Sunlight.
</blockquote>

"""

def fetch_image(api_url, text):
    """
    Fungsi untuk mengambil gambar dari API
    """
    params = {"text": text, "apikey": API_KEY}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            print("Response bukan gambar:", response.text)  # Debugging
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")  # Debugging jika ada kesalahan
        return None

async def process_image_command(client, message, api_url, command_name):
    """
    Fungsi umum untuk menangani perintah pembuatan gambar
    """
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text(f"<b><i>Gunakan perintah /{command_name} <teks> untuk membuat gambar.</i></b>")
        return

    request_text = args[1]
    await message.reply_text("<b><i>Sedang memproses, mohon tunggu...</i></b>")

    image_content = fetch_image(api_url, request_text)
    if image_content:
        temp_file = f"{command_name}.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)
        await message.reply_photo(photo=temp_file)
        os.remove(temp_file)
    else:
        await message.reply_text("Gagal membuat gambar. Coba lagi nanti.")

# Handler untuk setiap perintah
@PY.UBOT("typo2")
async def eraser_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/typography2"
    await process_image_command(client, message, api_url, "typography2")

@PY.UBOT("letters")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/letters"
    await process_image_command(client, message, api_url, "letters")
    
@PY.UBOT("cloth")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/cloth"
    await process_image_command(client, message, api_url, "cloth")

@PY.UBOT("grafitti")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/grafitti"
    await process_image_command(client, message, api_url, "grafitti")
    
@PY.UBOT("sunlight")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/sunlight"
    await process_image_command(client, message, api_url, "sunlight")