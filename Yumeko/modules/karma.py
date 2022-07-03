from Yumeko import pbot as app
from Yumeko.utils.errors import capture_err
from Yumeko.utils.dbfunctions import (update_karma, get_karma, get_karmas,
                                   int_to_alpha, alpha_to_int)
from Yumeko.utils.filter_groups import karma_positive_group, karma_negative_group
from pyrogram import filters


regex_upvote = r"^((?i)\+|\+\+|\+1|thx|tnx|ty|thank you|thanx|thanks|pro|cool|good|👍|nice|noice|piro)$"
regex_downvote = r"^(\-|\-\-|\-1|👎|noob|Noob|gross|fuck off)$"


@app.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_upvote)
    & ~filters.via_bot
    & ~filters.bot
    & ~filters.edited,
    group=karma_positive_group
)
@capture_err
async def upvote(_, message):
    if message.reply_to_message.from_user.id == message.from_user.id:
        return
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
    if current_karma:
        current_karma = current_karma['karma']
        karma = current_karma + 1
        new_karma = {"karma": karma}
        await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
    else:
        karma = 1
        new_karma = {"karma": karma}
        await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
    await message.reply_text(
        f'Incremented Karma of {user_mention} By 1 \nTotal Points: {karma}'
    )


@app.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_downvote)
    & ~filters.via_bot
    & ~filters.bot
    & ~filters.edited,
    group=karma_negative_group
)
@capture_err
async def downvote(_, message):
    if message.reply_to_message.from_user.id == message.from_user.id:
        return
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
    if current_karma:
        current_karma = current_karma['karma']
        karma = current_karma - 1
        new_karma = {"karma": karma}
        await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
    else:
        karma = 1
        new_karma = {"karma": karma}
        await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
    await message.reply_text(
        f'Decremented Karma Of {user_mention} By 1 \nTotal Points: {karma}'
    )


@app.on_message(filters.command("karma") & filters.group)
@capture_err
async def karma(_, message):
    chat_id = message.chat.id

    if not message.reply_to_message:
        karma = await get_karmas(chat_id)
        msg = f"**Karma list of {message.chat.title}:- **\n"
        limit = 0
        karma_dicc = {}
        for i in karma:
            user_id = await alpha_to_int(i)
            user_karma = karma[i]['karma']
            karma_dicc[str(user_id)] = user_karma
            karma_arranged = dict(
                sorted(karma_dicc.items(), key=lambda item: item[1], reverse=True))
        for user_idd, karma_count in karma_arranged.items():
            if limit > 9:
                break
            try:
                user_name = (await EREN.get_users(int(user_idd))).username
            except Exception:
                continue
            msg += f"{user_name} : `{karma_count}`\n"
            limit += 1
        await message.reply_text(msg)
    else:
        user_id = message.reply_to_message.from_user.id
        karma = await get_karma(chat_id, await int_to_alpha(user_id))
        if karma:
            karma = karma['karma']
            await message.reply_text(f'**Total Points**: __{karma}__')
        else:
            karma = 0
            await message.reply_text(f'**Total Points**: __{karma}__')

__mod_name__ = "Kᴀʀᴍᴀ"

__help__ = """

Upvote - Use upvote keywords like "+", "+1", "thanks", etc. to upvote a message.
Downvote - Use downvote keywords like "-", "-1", etc. to downvote a message.
Commands

 ❍ /karma:- reply to a user to check that user's karma points.
 ❍ /karma:- send without replying to any message to check karma point list of top 10
 ❍ /karmas off/on :- Enable/Disable karma in your group.
"""
