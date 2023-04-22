import os
import json
import requests
import aiohttp
import json

from telegram.ext import CommandHandler

from Yumeko import dispatcher

api_key = "blue-api-testing"
url = 'https://blue-api.vercel.app/reverse'


async def reverse(update, context):
    message = update.effective_message
    chat_id = update.effective_chat.id
    rtmid = message.message_id

    reply = message.reply_to_message

    if reply:
        if reply.sticker:
            file_id = reply.sticker.file_id
            new_id = reply.sticker.file_unique_id
        elif reply.photo:
            file_id = reply.photo[-1].file_id
            new_id = reply.photo[-1].file_unique_id
        else:
            await message.reply_text("Reply To An Image Or Sticker To Lookup!")
            return

        file_path = os.path.join("temp", f"{new_id}.jpg")
        file_obj = await context.bot.get_file(file_id)
        file_url = file_obj.file_path

    else:
        await message.reply_text(
            "Please Reply To A Sticker, Or An Image To Search It!"
        )
        return

    try:
        data = {"img_url": file_url}
        headers = {"API-KEY": api_key}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=data) as resp:
                    response_text = await resp.text()

            await message.reply_text(response_text)
        except:
            await message.reply_text("Cant find anything!!")
            
    except Exception as e:
        pass


dp.add_handler(CommandHandler(["pp", "grs", "p", "reverse"], reverse))
