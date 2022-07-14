#This module is created by @Ishikki_akabane

import time
from Yumeko import dispatcher
from telegram import ParseMode, Update
from telegram.ext import Filters, MessageHandler, CallbackContext, CommandHandler, run_async
from Yumeko.modules.helper_funcs.extraction import extract_user
from Yumeko.modules.helper_funcs.alternate import typing_action
from telegram.utils.helpers import escape_markdown


@run_async
@typing_action
def goodnight(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"*Hey {escape_markdown(first_name)} \nGood Night! 😴*"
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


@run_async
@typing_action
def goodmorning(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"*Hey {escape_markdown(first_name)} \nGood Morning!☀*"
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


@run_async
@typing_action
def hello(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"*Hello {escape_markdown(first_name)} ,\nHow are you*"
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


@run_async
@typing_action
def bye(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"*Bye {escape_markdown(first_name)} ,\nSee you later*"
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


GDMORNING_HANDLER = MessageHandler(
    Filters.regex("(?i)(good morning|goodmorning)"), goodmorning, friendly="goodmorning")
GDNIGHT_HANDLER = MessageHandler(
    Filters.regex("(?i)(good night|goodnight)"), goodnight, friendly="goodnight")
BYE_HANDLER = MessageHandler(
    Filters.regex("(?i)(bye|brb|afk|goodbye)"), bye, friendly="bye")
HELLO_HANDLER = MessageHandler(
    Filters.regex("(?i)(hello|hii|hi|hoi)"), hello, friendly="hello")

dispatcher.add_handler(GDMORNING_HANDLER)
dispatcher.add_handler(GDNIGHT_HANDLER)
dispatcher.add_handler(HELLO_HANDLER)
dispatcher.add_handler(BYE_HANDLER)
