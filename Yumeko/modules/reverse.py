import requests
import json
import os
import traceback

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler

from Yumeko import dispatcher

api_key = "blue-api-testing"
url = 'https://blue-api.vercel.app/reverse'

def reverse(update, context):
    message = update.effective_message
    chat_id = update.effective_chat.id

    reply = message.reply_to_message

    if reply:
        if reply.sticker:
            file_id = reply.sticker.file_id
            new_id = reply.sticker.file_unique_id
        elif reply.photo:
            file_id = reply.photo[-1].file_id
            new_id = reply.photo[-1].file_unique_id
        else:
            message.reply_text("Reply To An Image Or Sticker To Lookup!")
            return

        file_path = os.path.join("temp", f"{new_id}.jpg")
        file_obj = context.bot.get_file(file_id)
        file_url = file_obj.file_path
        
    else:
        message.reply_text(
            "Please Reply To A Sticker, Or An Image To Search It!"
        )
        return
    a = message.reply_text("searching...")
    try:
        data = {"img_url": file_url}
        headers = {"API-KEY": api_key}
        try:
            response = requests.post(url, headers=headers, json=data)
            reverse_dict = response.json()
            message.reply_text(
                text=reverse_dict["reverse"],
                reply_markup=InlineKeyboardMarkup(
                    [
                        InlineKeyboardButton(text="Link", url=reverse_dict["url"])
                    ]
                )
            )
        except Exception as e:
            message.reply_text("Cant find anything!!")
            print(f"{e}\n{traceback.format_exc()}")
    except Exception as e:
        message.reply_text("Cant find anything!!")
        print(f"{e}\n{traceback.format_exc()}")
    a.delete()
   

dispatcher.add_handler(CommandHandler(["pp", "grs", "p", "reverse"], reverse))
