from telethon import Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register
from Yumeko import telethn as tbot

PHOTO = "https://te.legra.ph/file/525fa3c63a58446823cc1.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = "🔶Mᴏsʜɪ Mᴏsʜɪ I'ᴍ Cʜɪᴢᴜʀᴜ!🔶 \n"
  TEXT += "🔹I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ🔹 \n"
  TEXT += "💠 Mʏ Oᴡɴᴇʀ : [ᏆՏᎻᏆᏦᏦᏆ ᎪᏦᎪᏴᎪΝᎬ](https://t.me/ishikki_akabane) 💠 \n"
  TEXT += f"🔹Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ : {tlhver} 🔹\n"
  TEXT += f"🔹Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ : {pyrover} 🔹"
  BUTTON = [[Button.url("Hᴇʟᴘ", "https://t.me/chizuruxdbot?start=help"), Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/suppporttxd")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

@register(pattern=("/reload"))
async def reload(event):
  TEXT = "🔷 **ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ** 🔷\n\n Aᴅᴍɪɴ ʟɪsᴛ ʜᴀs ʙᴇᴇɴ **ᴜᴘᴅᴀᴛᴇᴅ**"
  BUTTON = [[Button.url("📡 Uᴘᴅᴀᴛᴇs", "https://t.me/updatesxd")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
