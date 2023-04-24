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
    
    if not message.reply_to_message or not message.reply_to_message.photo and not message.reply_to_message.sticker:
        await message.reply_text("Reply to an image or sticker to reverse search it!")
        return
    
    file = message.reply_to_message.photo or message.reply_to_message.sticker
    
    file_id = file.file_id
    new_id = file.file_unique_id
    file_path = os.path.join("temp", f"{new_id}.jpg")
    
    fileOBJ = await client.download_media(file_id, file_path)
    print(fileOBJ)
    with open(fileOBJ, "rb") as f:
        data = {"img_url": f.read()}
    print(data)
    
    """
    if message.reply_to_message and (
        message.reply_to_message.photo or message.reply_to_message.sticker
    ):
        file_id = message.reply_to_message.photo.file_id
        print(file_id)


        try:
            data = {"img_url": file_url}
            headers = {"API-KEY": api_key}

            async with aiohttp.ClientSession() as session:
                async with session.post(URL, headers=headers, json=data) as resp:
                    response_text = await resp.text()

            await message.reply_text(response_text)
        except Exception as e:
            await message.reply_text("Can't find anything!")
    """
