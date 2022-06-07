import os
import nekos
import requests
from PIL import Image
from Yumeko import dispatcher
from telegram.ext import CommandHandler, run_async
@run_async
def neko(update, context):
    msg = update.effective_message
    target = "neko"
    msg.reply_photo(nekos.img(target))

@run_async
def wallpaper(update, context):
    msg = update.effective_message
    target = "wallpaper"
    msg.reply_photo(nekos.img(target))

@run_async
def tickle(update, context):
     msg = update.effective_message
     target = "tickle"
     msg.reply_video(nekos.img(target))

@run_async
def feed(update, context):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))

@run_async
def smug(update, context):
    msg = update.effective_message
    target = "smug"
    msg.reply_video(nekos.img(target))

NEKO_HANDLER = CommandHandler("neko", neko)
WALLPAPER_HANDLER = CommandHandler("wallpaper", wallpaper)
TICKLE_HANDLER = CommandHandler("tickle", tickle)
FEED_HANDLER = CommandHandler("feed", feed)
SMUG_HANDLER = CommandHandler("smug", smug)

dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(SMUG_HANDLER)

__handlers__ = [
    NEKO_HANDLER,
    WALLPAPER_HANDLER,
    TICKLE_HANDLER,
    FEED_HANDLER,
    SMUG_HANDLER,
]



__mod_name__ = "SFW"

__help__ = """
*Commands* *:*  
   ➢ `/neko`*:*Sends Random SFW Neko source Images.
   ➢ `/tickle`*:*Sends Random Tickle GIFs.
   ➢ `/feed`*:*Sends Random Feeding GIFs.
   ➢ `/smug`*:* Sends Random Smug GIFs.
"""
