from typing import Optional

import Yumeko.modules.sql.rules_sql as sql
import Yumeko.modules.sql.feds_sql as fsql
from Yumeko import dispatcher
from Yumeko.modules.helper_funcs.chat_status import user_admin
from Yumeko.modules.helper_funcs.string_handling import markdown_parser
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import escape_markdown


@run_async
def get_rules(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    send_rules(update, chat_id)


# Do not async - not from a handler
def send_rules(update, chat_id, from_pm=False):
    bot = dispatcher.bot
    user = update.effective_user  # type: Optional[User]
    reply_msg = update.message.reply_to_message
    try:
        chat = bot.get_chat(chat_id)
    except BadRequest as excp:
        if excp.message == "Chat not found" and from_pm:
            bot.send_message(
                user.id,
                "The rules shortcut for this chat hasn't been set properly! Ask admins to "
                "fix this.\nMaybe they forgot the hyphen in ID",
            )
            return
        else:
            raise

    rules = sql.get_rules(chat_id)
    text = f"The rules for *{escape_markdown(chat.title)}* are:\n\n{rules}"
    try:
        fed_id = fsql.get_fed_id(chat.id)
    except:
        fed_id = False
    try:
        frules = fsql.get_frules(fed_id)
    except KeyError:
        frules = False
    if from_pm and rules:
        bot.send_message(
            user.id, text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
    elif from_pm and fed_id and frules and not rules:
        ftext = f" The admins of *{escape_markdown(chat.title)}* haven't set any rules yet.\n*Reverting to the rules set by the fed admins:*\n\n {frules}"
        bot.send_message(
            user.id, ftext, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
    elif from_pm and fed_id and not frules and not rules:
        bot.send_message(
            user.id,
            "The group admins haven't set any rules for this chat yet. "
            "This probably doesn't mean it's lawless though...!",
        )
    elif from_pm and not fed_id and not rules:
        bot.send_message(
            user.id,
            "The group admins haven't set any rules for this chat yet. "
            "This probably doesn't mean it's lawless though...!",
        )
    elif rules and reply_msg:
        reply_msg.reply_text(
            "Please click the button below to see the rules.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Rules", url=f"t.me/{bot.username}?start={chat_id}"
                        )
                    ]
                ]
            ),
        )
    elif rules:
        update.effective_message.reply_text(
            "Please click the button below to see the rules.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Rules", url=f"t.me/{bot.username}?start={chat_id}"
                        )
                    ]
                ]
            ),
        )
    elif fed_id and frules and not rules:
        update.effective_message.reply_text(
            "The group admins haven't set any rules for this chat yet.\nPlease click the button below to see the fed rules.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Fed Rules", url=f"t.me/{bot.username}?start={chat_id}"
                        )
                    ]
                ]
            ),
        )
    else:
        update.effective_message.reply_text(
            "The group admins haven't set any rules for this chat yet. "
            "This probably doesn't mean it's lawless though...!"
        )


@run_async
@user_admin
def set_rules(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    msg = update.effective_message  # type: Optional[Message]
    raw_text = msg.text
    args = raw_text.split(None, 1)  # use python's maxsplit to separate cmd and args
    if len(args) == 2:
        txt = args[1]
        offset = len(txt) - len(raw_text)  # set correct offset relative to command
        markdown_rules = markdown_parser(
            txt, entities=msg.parse_entities(), offset=offset
        )

        sql.set_rules(chat_id, markdown_rules)
        update.effective_message.reply_text("Successfully set rules for this group.")


@run_async
@user_admin
def clear_rules(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    sql.set_rules(chat_id, "")
    update.effective_message.reply_text("Successfully cleared rules!")


rulese = int(sql.num_chats())
rulesee = rulese+9

def __stats__():
    return f"• {rulesee} chats have rules set."


def __import_data__(chat_id, data):
    # set chat rules
    rules = data.get("info", {}).get("rules", "")
    sql.set_rules(chat_id, rules)


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, user_id):
    return f"This chat has had it's rules set: `{bool(sql.get_rules(chat_id))}`"


__help__ = """
 • `/rules`*:* get the rules for this chat.

*Admins only:*
 • `/setrules <your rules here>`*:* set the rules for this chat.
 • `/clearrules`*:* clear the rules for this chat.
"""

__mod_name__ = "Rules"

GET_RULES_HANDLER = CommandHandler("rules", get_rules, filters=Filters.group)
SET_RULES_HANDLER = CommandHandler("setrules", set_rules, filters=Filters.group)
RESET_RULES_HANDLER = CommandHandler("clearrules", clear_rules, filters=Filters.group)

dispatcher.add_handler(GET_RULES_HANDLER)
dispatcher.add_handler(SET_RULES_HANDLER)
dispatcher.add_handler(RESET_RULES_HANDLER)
