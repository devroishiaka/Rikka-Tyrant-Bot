import os
from telegram import InlineKeyboardButton, ParseMode, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, run_async
import subprocess

from Yumeko import (
    OWNER_ID,
    dispatcher
)


# Define the backup command
def db_backup(update: Update, context: CallbackContext):
    # Get the database credentials
    db_host = "dpg-cfp1k7h4rebfdaqpper0-a"
    db_port = 5432
    db_name = "chizuru_m4xr"
    db_user = "chizuru"
    db_password = "PbOsQzJfjaSfDizJv67ZGjCf1hfWHanU"
    backup_dir = ""


dispatcher.add_handler(CommandHandler("db_export", db_backup))
dispatcher.add_handler(CommandHandler("db_import", db_migrate))
