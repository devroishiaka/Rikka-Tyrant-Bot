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
    backup_dir = "./"
    """
    backup_file = f"{backup_dir}/{db_name}.backup"
    backup_command = f"pg_dump -h {db_host} -p {db_port} -U {db_user} -F c -b -v {db_name} > {backup_file}"
    """
    
    backup_command = pg_dump "postgres://chizuru:PbOsQzJfjaSfDizJv67ZGjCf1hfWHanU@dpg-cfp1k7h4rebfdaqpper0-a.oregon-postgres.render.com/chizuru_m4xr" > backup.sql
    # Execute the backup command
    subprocess.run(backup_command, shell=True, check=True)

    # Send a message to the user with the backup file
    try:
        with open(backup_file, "rb") as file:
            update.message.reply_document(file, filename=f"{db_name}.backup")
    except Exception as e:
        update.message.reply_text(e)


dispatcher.add_handler(CommandHandler("db_export", db_backup))
#dispatcher.add_handler(CommandHandler("db_import", db_migrate))
