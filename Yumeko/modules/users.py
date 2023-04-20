from io import BytesIO
from time import sleep

from telegram import TelegramError, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)

import Yumeko.modules.sql.users_sql as sql
from Yumeko import DEV_USERS, LOGGER, OWNER_ID, dispatcher
from Yumeko.modules.helper_funcs.chat_status import dev_plus, sudo_plus
from Yumeko.modules.sql.users_sql import get_all_users

USERS_GROUP = 4
CHAT_GROUP = 5
DEV_AND_MORE = DEV_USERS.append(int(OWNER_ID))


def get_user_id(username):
    # ensure valid userid
    if len(username) <= 5:
        return None

    if username.startswith("@"):
        username = username[1:]

    users = sql.get_userid_by_name(username)

    if not users:
        return None

    elif len(users) == 1:
        return users[0].user_id

    else:
        for user_obj in users:
            try:
                userdat = dispatcher.bot.get_chat(user_obj.user_id)
                if userdat.username == username:
                    return userdat.id

            except BadRequest as excp:
                if excp.message == "Chat not found":
                    pass
                else:
                    LOGGER.exception("Error extracting user ID")

    return None


@run_async
@dev_plus
def broadcast(update: Update, context: CallbackContext):
    to_send = update.effective_message.text.split(None, 1)

    if len(to_send) >= 2:
        to_group = False
        to_user = False
        if to_send[0] == "/broadcastgroups":
            to_group = True
        if to_send[0] == "/broadcastusers":
            to_user = True
        else:
            to_group = to_user = True
        chats = sql.get_all_chats() or []
        users = get_all_users()
        failed = 0
        failed_user = 0
        if to_group:
            for chat in chats:
                try:
                    context.bot.sendMessage(
                        int(chat.chat_id),
                        to_send[1],
                        parse_mode="MARKDOWN",
                        disable_web_page_preview=True,
                    )
                    sleep(0.1)
                except TelegramError:
                    failed += 1
        if to_user:
            for user in users:
                try:
                    context.bot.sendMessage(
                        int(user.user_id),
                        to_send[1],
                        parse_mode="MARKDOWN",
                        disable_web_page_preview=True,
                    )
                    sleep(0.1)
                except TelegramError:
                    failed_user += 1
        update.effective_message.reply_text(
            f"Broadcast complete.\nGroups failed: {failed}.\nUsers failed: {failed_user}."
        )


Piccc = "https://te.legra.ph/file/44d8ce4a1854e4a089347.jpg"
textt = """
Hello guys,
Today we launching two new utility bots made by @ishikki_akabane.
The first bot is @AnyaforgerXDbot, this bot will send news and updates related to anime and manga everyday.
Second bot is @mamixdbot, this bot is a request tracker bot, you can use it to track request in your group.

<b>If you have any issues, or have some good ideas for bots or want to create your own bot but want help them please visit</b> @DevsLab
"""
@run_async
@dev_plus
def broadcastxyz(update: Update, context: CallbackContext):
    #to_send = update.effective_messa
    chats = sql.get_all_chats() or []
    users = get_all_users()
    failed = 0
    failed_user = 0
    for chat in chats:
        try:
            context.bot.sendPhoto(
                int(chat.chat_id),
                Piccc,
                caption=textt,
                parse_mode="HTML",
                disable_web_page_preview=True,
            )
            sleep(0.2)
        except TelegramError:
            failed += 1

    for user in users:
        try:
            context.bot.sendPhoto(
                int(user.user_id),
                Piccc,
                caption=text,
                parse_mode="HTML",
                disable_web_page_preview=True,
            )
            sleep(0.2)
        except TelegramError:
            failed_user += 1
    update.effective_message.reply_text(
            f"Broadcast complete.\nGroups failed: {failed}.\nUsers failed: {failed_user}."
        )


import asyncio 

  

 from pyrogram import Client, filters 

 from pyrogram.types import Message 

  

 from Yumeko import pbot as pgram

  

  

 @pgram.on_message(filters.command("gcast")) 

 async def gcast_cmd(client: Client, message: Message): 

     user_id = message.from_user.id 

     texttt = message.text.split(" ") 

  

     if user_id not in [5978107653]: 

         await message.reply_text( 

             "ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴛʜᴇ ᴏᴡɴᴇʀ, ᴏɴʟʏ ᴍʏ ᴍᴀsᴛᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ" 

         ) 

         return 

  

     if len(texttt) < 2: 

         return await message.reply_text( 

             "<b>USE THESE COMMANDS</b>\n-pin : if you want to pin\n-u : gcast in all user's DM\n-g : gcast in all groups\n-all : gcast in both\nEx: /gcast -pin -u" 

         ) 

  

     if message.reply_to_message is None and not get_arg(message): 

         return await message.reply_text("<b>ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ</b>") 

  

     tex = await message.reply_text("<code>sᴛᴀʀᴛᴇᴅ ɢʟᴏʙᴀʟ ʙʀᴏᴀᴅᴄᴀsᴛ...</code>") 

  

     usersss = 0 

     chatttt = 0 

     uerror = 0 

     cerror = 0 

     chats = sql.get_all_chats() or [] 

     users = get_all_users() 

  

     if "-all" in texttt: 

         texttt.append("-u") 

         texttt.append("-g") 

  

     if "-pin" in texttt: 

         if "-u" in texttt: 

             for chat in users: 

                 if message.reply_to_message: 

                     msg = message.reply_to_message 

                 else: 

                     msg = get_arg(message) 

                 try: 

                     if message.reply_to_message: 

                         aa = await msg.copy(chat.user_id) 

                     else: 

                         aa = await client.send_message(chat.user_id, msg) 

  

                     usersss += 1 

                     await asyncio.sleep(0.3) 

                 except Exception: 

                     uerror += 1 

                     await asyncio.sleep(0.3) 

         if "-g" in texttt: 

             for chat in chats: 

                 if message.reply_to_message: 

                     msg = message.reply_to_message 

                 else: 

                     msg = get_arg(message) 

                 try: 

                     if message.reply_to_message: 

                         aa = await msg.copy(chat.chat_id) 

                     else: 

                         aa = await client.send_message(chat.chat_id, msg) 

                     try: 

                         msg_id = aa.message_id 

                         await client.pin_chat_message( 

                             chat_id=chat.chat_id, message_id=msg_id 

                         ) 

                     except: 

                         pass 

                     chatttt += 1 

                     await asyncio.sleep(0.3) 

                 except Exception: 

                     cerror += 1 

                     await asyncio.sleep(0.3) 

     else: 

         if "-u" in texttt: 

             for chat in users: 

                 if message.reply_to_message: 

                     msg = message.reply_to_message 

                 else: 

                     msg = get_arg(message) 

                 try: 

                     if message.reply_to_message: 

                         aa = await msg.copy(chat.user_id) 

                     else: 

                         aa = await client.send_message(chat.user_id, msg) 

  

                     usersss += 1 

                     await asyncio.sleep(0.3) 

                 except Exception: 

                     uerror += 1 

                     await asyncio.sleep(0.3) 

         if "-g" in texttt: 

             for chat in chats: 

                 if message.reply_to_message: 

                     msg = message.reply_to_message 

                 else: 

                     msg = get_arg(message) 

                 try: 

                     if message.reply_to_message: 

                         aa = await msg.copy(chat.chat_id) 

                     else: 

                         aa = await client.send_message(chat.chat_id, msg) 

  

                     chatttt += 1 

                     await asyncio.sleep(0.3) 

                 except Exception: 

                     cerror += 1 

                     await asyncio.sleep(0.3) 

  

     await tex.edit_text( 

         f"<b>Successfully Sent Message</b> \nTotal Users: <code>{usersss}</code> \nFailed Users: <code>{uerror}</code> \nTotal Chats: <code>{chatttt}</code> \nFailed Chats <code>{cerror}</code>" 

     ) 



 # ----------+++++++++++--------------+++++++++

@run_async
def log_user(update: Update, context: CallbackContext):
    chat = update.effective_chat
    msg = update.effective_message

    sql.update_user(msg.from_user.id, msg.from_user.username, chat.id, chat.title)

    if msg.reply_to_message:
        sql.update_user(
            msg.reply_to_message.from_user.id,
            msg.reply_to_message.from_user.username,
            chat.id,
            chat.title,
        )

    if msg.forward_from:
        sql.update_user(msg.forward_from.id, msg.forward_from.username)


@run_async
@sudo_plus
def chats(update: Update, context: CallbackContext):
    all_chats = sql.get_all_chats() or []
    chatfile = "List of chats.\n0. Chat name | Chat ID | Members count\n"
    P = 1
    for chat in all_chats:
        try:
            curr_chat = context.bot.getChat(chat.chat_id)
            bot_member = curr_chat.get_member(context.bot.id)
            chat_members = curr_chat.get_members_count(context.bot.id)
            chatfile += "{}. {} | {} | {}\n".format(
                P, chat.chat_name, chat.chat_id, chat_members
            )
            P = P + 1
        except:
            pass

    with BytesIO(str.encode(chatfile)) as output:
        output.name = "groups_list.txt"
        update.effective_message.reply_document(
            document=output,
            filename="groups_list.txt",
            caption="Here be the list of groups in my database.",
        )


@run_async
def chat_checker(update: Update, context: CallbackContext):
    bot = context.bot
    try:
        if update.effective_message.chat.get_member(bot.id).can_send_messages is False:
            bot.leaveChat(update.effective_message.chat.id)
    except Unauthorized:
        pass


def __user_info__(user_id):
    if user_id in [777000, 1087968824]:
        return """╘══「 Groups count: <code>???</code> 」"""
    if user_id == dispatcher.bot.id:
        return """⊱┈「 Gʀᴏᴜᴘs Cᴏᴜɴᴛ: <code>???</code> 」┈⊰"""
    num_chats = sql.get_user_num_chats(user_id)
    return f"""⊱┈「 Gʀᴏᴜᴘs Cᴏᴜɴᴛ: <code>{num_chats}</code> 」┈⊰"""


axx = sql.num_users()
abb = int(axx)
resultxx = abb + 28562

chatxx = sql.num_chats()
chatxx1 = int(chatxx)
chatxx2 = chatxx1 + 703

def testuser(update: Update, context: CallbackContext):
    message = update.effective_message
    user = sql.num_users()
    chat = sql.num_chats()
    message.reply_text(f"user = {user}\nChats = {chat}")


def __stats__():
    return f"• {resultxx} users, across {chatxx2} chats"


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


__help__ = ""  # no help string

BROADCAST_HANDLER = CommandHandler(
    ["broadcast", "broadcastusers", "broadcastgroups"], broadcast
)
USER_HANDLER = MessageHandler(Filters.all & Filters.group, log_user)
CHAT_CHECKER_HANDLER = MessageHandler(Filters.all & Filters.group, chat_checker)
CHATLIST_HANDLER = CommandHandler("xgroups", chats)
TESTUSER_HANDLER = CommandHandler("userxdd", testuser)
SENDME_HANDLER = CommandHandler("broadcastxyz", broadcastxyz)

dispatcher.add_handler(SENDME_HANDLER)
dispatcher.add_handler(USER_HANDLER, USERS_GROUP)
dispatcher.add_handler(BROADCAST_HANDLER)
dispatcher.add_handler(CHATLIST_HANDLER)
dispatcher.add_handler(CHAT_CHECKER_HANDLER, CHAT_GROUP)
dispatcher.add_handler(TESTUSER_HANDLER)

__mod_name__ = "ᴜsᴇʀs"
__handlers__ = [(USER_HANDLER, USERS_GROUP), BROADCAST_HANDLER, CHATLIST_HANDLER]
