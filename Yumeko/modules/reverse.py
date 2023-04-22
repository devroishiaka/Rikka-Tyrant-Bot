import os
import aiohttp

from pyrogram import Client, filters
from pyrogram.types import Message

from Yumeko import pbot

api_key = "blue-api-testing"
url = 'https://blue-api.vercel.app/reverse'

@pbot.on_message(filters.command(["pp", "grs", "p", "reverse"]))
async def reverse(client, message):
    chat_id = message.chat.id
    rtmid = message.message_id

    reply = message.reply_to_message
    if not reply:
        await message.reply_text("Please reply to a sticker or an image to search it!")
        return
    

    if reply.sticker:
        file_id = reply.sticker.file_id
        new_id = reply.sticker.file_unique_id
    elif reply.photo:
        file_id = reply.photo[-1].file_id
        new_id = reply.photo[-1].file_unique_id
    else:
        await message.reply_text("Reply to an image or sticker to lookup!")
        return

    file_path = os.path.join("temp", f"{new_id}.jpg")
    file_obj = await client.download_media(message=reply)
    file_url = file_obj.file_path

    try:
        data = {"img_url": file_url}
        headers = {"API-KEY": api_key}

        async with aiohttp.ClientSession() as session:
            async with session.post(URL, headers=headers, json=data) as resp:
                response_text = await resp.text()

        await message.reply_text(response_text)
    except Exception as e:
        await message.reply_text("Can't find anything!")
