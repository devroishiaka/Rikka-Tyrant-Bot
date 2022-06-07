from telethon import Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register
from Yumeko import telethn as tbot

PHOTO = "https://telegra.ph/file/aade65f7e2cf96064e12d.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = "**Moshi Moshi I'm Rikka!** \n\n"
  TEXT += "×**I'm Working Properly** \n\n"
  TEXT += "×**My Owner : [Sneha Jha](https://t.me/Sneha_UwU_OwO)** \n\n"
  TEXT += f"×**Telethon Version : {tlhver}** \n\n"
  TEXT += f"×**Pyrogram Version : {pyrover}** \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Rikka_Tyrant_bot?start=help"), Button.url("Support", "https://t.me/tyranteyeeee")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

@register(pattern=("/reload"))
async def reload(event):
  TEXT = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/tyranteyeeee")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
