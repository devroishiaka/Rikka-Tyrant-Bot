from PhoenixScanner import Phoenix
import os
from telegram import Update
from telegram.ext import (
    CallbackContext,
    Filters,
    MessageHandler,
)

from Yumeko import dispatcher

RED = Phoenix("RED7-dsxdt9yahtakfy0ix95wj")

def redseven(update: Update, context: CallbackContext):
    chat = update.effective_chat
    msg = update.effective_message
    user = msg.from_user
    
    check = RED.check(user.id)
    if check["is_gban"]:
        Reply = f"""
 Alert ⚠️
User [{user.id}](tg://user?id={user.id}) is officially
Scanned by Team Red7 | Phoenix API ;)

Appeal [Here](https://t.me/Red7WatchSupport)
"""
        try:
          update.effective_message.reply_text(Reply)
          chat.ban_member(user.id)
        except:
          update.effective_message.reply_text(Reply)
          pass
        
dispatcher.add_handler(MessageHandler(Filters.all & Filters.chat_type.groups, phoenix, run_async = True))
