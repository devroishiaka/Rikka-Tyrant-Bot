import os
from telegram import InlineKeyboardButton, ParseMode, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, run_async
import subprocess

from Yumeko import (
    OWNER_ID,
    dispatcher
)


@run_async
def db_backup(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        update.message.reply_text("Only for owner!!")
        return
    
    backup_dir = "./"
    backup_file = f"{backup_dir}/backup.sql"
    
    backup_command = "pg_dump 'postgres://chizuru:PbOsQzJfjaSfDizJv67ZGjCf1hfWHanU@dpg-cfp1k7h4rebfdaqpper0-a.oregon-postgres.render.com/chizuru_m4xr' > backup.sql"
    # Execute the backup command
    subprocess.run(backup_command, shell=True, check=True)

    # Send a message to the user with the backup file
    try:
        with open(backup_file, "rb") as file:
            update.message.reply_document(file, filename="backup.sql")
    except Exception as e:
        update.message.reply_text(e)

        
@run_async
def db_migrate(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        update.message.reply_text("Only for owner!!")
        return
    
    backup_dir = "./"
    backup_file = f"{backup_dir}/backup.sql"
    
    try:
        backup_command = "psql 'postgres://chizuru:e16mjneLHdty2uBriNd9X0rUVu8r7VHD@dpg-cgbdnbpmbg55nqlq0c70-a.oregon-postgres.render.com/chizuru_qiea' -f backup.sql"
        # Execute the backup command
        subprocess.run(backup_command, shell=True, check=True)
        update.message.reply_text("Migration started!")
    except Exception as e:
        update.message.reply_text(e)

        
dispatcher.add_handler(CommandHandler("db_export", db_backup))
dispatcher.add_handler(CommandHandler("db_import", db_migrate))
