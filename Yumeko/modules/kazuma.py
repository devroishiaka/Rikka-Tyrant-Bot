from Yumeko import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

def kazumaclanxd(update: Update, context: CallbackContext):
    TEXT = "**[ᴋᴀᴢᴜᴍᴀ ᴄʟᴀɴ](t.me/kazumaclanxd)** ɪs ᴀɴ ᴀɴɪᴍᴇ ᴛʜᴇᴍᴇᴅ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴍᴀᴅᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ᴀʟʟ ᴋɪɴᴅs ᴏғ ᴀɴɪᴍᴇ ʀᴇʟᴀᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛs. ᴏᴜʀ ᴍᴀɪɴ ᴘᴇʀsᴘᴇᴄᴛɪᴠᴇ ɪs Pᴇᴀcᴇ\n\n━━━━━━━━━━━━━━━━━\nᴠɪsɪᴛ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ғᴏʀ ᴀʟʟ ʏᴏᴜʀ ϙᴜᴇʀɪᴇs\nʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴀᴘᴘᴇᴀʟ ғᴏʀ ɢʙᴀɴ ᴏʀ ғʙᴀɴ.\n━━━━━━━━━━━━━━━━━"
    update.effective_message.reply_photo(
        PHOTO, caption= TEXT,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/suppporttxd/"),
                    InlineKeyboardButton(text="Owɴᴇʀ", url="https://t.me/ishikki_akabane")
                ],
                [   
                    InlineKeyboardButton(text="◈ ᴋᴀᴢᴜᴍᴀ ᴄʟᴀɴ ◈", url="https://t.me/kazumaclanxd")
                ]
            ]
        ),
    )


KAZUMACLAN_HANDLER = CommandHandler("kazumaclan", kazumaclanxd, run_async = True)
dispatcher.add_handler(KAZUMACLAN_HANDLER)

__mod_name__ = "ᴋᴀᴢᴜᴍᴀ ᴄʟᴀɴ"

__help__ = """
━━━━━━━━━━━━━━━━━━━
ᴋᴀᴢᴜᴍᴀ ᴄʟᴀɴ ɪs ᴀɴ ᴀɴɪᴍᴇ ᴛʜᴇᴍᴇᴅ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴍᴀᴅᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ᴀʟʟ ᴋɪɴᴅs ᴏғ ᴀɴɪᴍᴇ ʀᴇʟᴀᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛs. ᴏᴜʀ ᴍᴀɪɴ ᴘᴇʀsᴘᴇᴄᴛɪᴠᴇ ɪs ᴛᴏ ᴜɴɪᴛᴇ ᴀɴɪᴍᴇ ʟᴏᴠᴇʀs ᴀɴᴅ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴛʜᴇʏ ᴡᴀɴᴛ.

ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴀɴɪᴍᴇ, ᴍᴀɴɢᴀ, ᴀɴɪᴍᴇ ᴀᴍᴠ, ᴀɴɪᴍᴇ ᴛʜᴇᴍᴇᴅ ʙᴏᴛs, ᴡᴀʟʟᴘᴀᴘᴇʀ ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ.
━━━━━━━━━━━━━━━━━━━
ᴠɪsɪᴛ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ғᴏʀ ᴀʟʟ ʏᴏᴜʀ ϙᴜᴇʀɪᴇs
ʏᴏᴜ ᴄᴀɴ ʀᴇϙᴜᴇsᴛ ʏᴏᴜʀ ᴀɴɪᴍᴇ, ᴍᴀɴɢᴀ, ᴀɴᴅ ᴘғᴘ ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘ.
ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴀᴘᴘᴇᴀʟ ғᴏʀ ɢʙᴀɴ ᴏʀ ғʙᴀɴ.
⊹⊸⊸⊱ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/suppporttxd)
ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ʀᴇᴘᴏʀᴛ ʙᴜɢ ɪɴ ᴏᴜʀ ʙᴏᴛs
~~ `/bug` <ɪɴғᴏʀᴍᴀᴛɪᴏɴ>: Rᴇᴘᴏʀᴛs ʙᴜɢ ᴛᴏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ
━━━━━━━━━━━━━━━━━━━
"""
