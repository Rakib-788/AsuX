import asyncio
import time

from telegram import Update
from telegram.ext import Application

from AsuX.modules import ALL_MODULES
from config import MONGO_DB_URL, TOKEN

TOKEN = TOKEN
MONGO_DB_URL = MONGO_DB_URL

AI_API_KEY = "ccdFpFeTghMRjtbg"
AI_BID = "172001"

StartTime = time.time()

rani = Application.builder().token(TOKEN).build()
asyncio.get_event_loop().run_until_complete(rani.bot.initialize())


BOT_ID = rani.bot.id
BOT_USERNAME = rani.bot.username

print("ɪɴғᴏ: ʙᴏᴛᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ")
print("sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴏᴀᴅᴇᴅ ᴍᴏᴅᴜʟᴇs -: " + str(ALL_MODULES))
print(f"ɪɴғᴏ: ʙᴏᴛᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ ᴀs -: {BOT_USERNAME} ")
