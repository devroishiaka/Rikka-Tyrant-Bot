
# Imports from external libraries. (DON'T EDIT)
import requests
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async

# Imports dispatcher = updater.dispatcher from __init__.py (*MUST EDIT* CHANGE MODULE_NAME TO THE FOLDER NAME OF MODULES IN YOUR BOT)
from Yumeko import dispatcher

@run_async
def waifu(update, context):
    try:
        msg = update.effective_message
        # API (DON'T EDIT)
        url = f'https://api.animeepisode.org/waifu/'
        result = requests.get(url).json()
        img = result['Character_Image']
        # Message (EDIT THIS PART AS HTML *IF YOU WANT*)
        text = f'''
<b>Name :</b> <code>{result['Character_Name']}</code>
        
<b>Anime :</b> <code>{result['Anime_name']}</code>
'''
        msg.reply_photo(photo=img, caption=text, parse_mode=ParseMode.HTML)

    except Exception as e:
        text = f'<b>Error</b>: <code>' + e + '</code>'
        msg.reply_text(text, parse_mode=ParseMode.HTML)

# Command Handler (YOU CAN CHANGE 'waifu' TO ANY 'cmd' FOR THIS TO BE WORKED AS '/cmd' *IF YOU WANT*.)
WAIFU_HANDLER = CommandHandler('waifuinfo', waifu)
dispatcher.add_handler(WAIFU_HANDLER)

#  Buttons for /help .
__mod_name__ = "Wᴀɪғᴜ"

__help__ = """
❍ `/waifu` : Gives random image of best selected waifus.
❍ `/swaifu` : Gives random image of waifu
❍ `/waifus` : Gives random image of waifu
❍ `/waifuinfo` : Gives random image of waifu with info.
"""

__handlers__ = [WAIFU_HANDLER]
