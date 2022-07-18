# rewritten by Ishikki Akabane

from datetime import datetime
from Yumeko import DEV_USERS, OWNER_ID
from Yumeko import (
    OWNER_ID,
    OWNER_USERNAME,
    SUPPORT_CHAT,
    dispatcher
)
import time
from telegram import InlineKeyboardButton, ParseMode, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, run_async

BUGS_IMG = "https://te.legra.ph/file/dc9325a322b1c8981eaf7.jpg"

@run_async
def bug(update: Update, context: CallbackContext):
    try:
        args = update.effective_message.text.split(None, 1)
        user_id = update.effective_message.from_user.id
        message = update.effective_message
        msg_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
        if user_id == OWNER_ID:
            message.reply_text(
                    "❎ *Owner of the bot reported BUG?? Lol, is this a joke 😶*", parse_mode=ParseMode.MARKDOWN
                )
            return
        if update.effective_chat.type == "private":
            update.effective_message.reply_text(f"❎ *This command only works in public groups.*\n\n Visit @{SUPPORT_CHAT} to report bugs related to bot's pm.", parse_mode=ParseMode.MARKDOWN)
            return
        
        if len(args) >= 2:
            bugs = args[1]
            if message.chat.username:
                link_chat_id = message.chat.username
                message_link = f"https://t.me/{link_chat_id}/{msg_id}"
            else:
                update.effective_message.reply_text(f"❎ *This command only works in public groups.*\n\n Visit @{SUPPORT_CHAT} to report bugs related to bot's pm.", parse_mode=ParseMode.MARKDOWN)
                return
        else:
            message.reply_text(
                    f"❎ *No bug to Report!* Use `/bug <information>`", parse_mode=ParseMode.MARKDOWN
                )
            return
            
        first_name = update.effective_user.first_name
        user = message.from_user
        mention = f'<a href="tg://user?id={user.id}">{first_name}</a>'
        datetimes_fmt = "%d-%m-%Y"
        datetimes = datetime.utcnow().strftime(datetimes_fmt)
        bug_report = f"""
<b>#BUG :  @{OWNER_USERNAME}
From User :  {mention}
User ID :  {user_id}
Group :  @{link_chat_id}
Bug Report :  {bugs}
Event Stamp :  {datetimes}</b>
"""

        if user_id != OWNER_ID:
            message.reply_text(
                f"*Bug Report : {bugs}*\n\n"
                "✅ *The bug was successfully reported to the support group!*",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Support",
                                url="https://t.me/suppporttxd"
                            )
                        ]
                    ]
                ),
                parse_mode=ParseMode.MARKDOWN
            )
            dispatcher.bot.send_photo(
                f"@{SUPPORT_CHAT}",
                photo=BUGS_IMG,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="➡ View Bug",
                                url=f"{message_link}",
                            )
                        ]
                    ]
            ),
            parse_mode=ParseMode.HTML,
            )
    except:
        update.effective_message.reply_text(
            f"*ERROR!!! Contact @{SUPPORT_CHAT}*",
            parse_mode=ParseMode.MARKDOWN,
        )


BUG_HANDLER = CommandHandler(("bug", "bugs"), bug)

dispatcher.add_handler(BUG_HANDLER)

__command_list__ = ["bug"]
__handlers__ = [BUG_HANDLER]

__mod_name__ = "Bug"
