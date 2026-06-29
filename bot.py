import os
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

usd = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/").json()[0]["Rate"]
eur = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/").json()[0]["Rate"]

text = f"""📊 Valyuta kurslari

🇺🇸 USD: {usd} so'm
🇪🇺 EUR: {eur} so'm
"""

bot.send_message(chat_id=CHANNEL_ID, text=text)
