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
