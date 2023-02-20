#ISHIKKI_AKABANE
import json
import requests
from telegram.ext import MessageHandler, Filters
from telegram import ParseMode

"""import your dispatcher obejct as dispatcher"""
from Yumeko import dispatcher

api_key = "ishikkiakabanelovesalice"

url = "https://blue-ishikki.vercel.app/records"
headers = {'API-KEY': api_key}
response = requests.get(url, headers=headers)
if response.status_code == 400: # bad request
    print("RESTARTING BLUE SCANNER!!!!")
    response = requests.get(url, headers=headers)
    if response.status_code != 200: # unknown error
        print("BLUE SCANNER FAILED TO START!!!")

elif response.status_code == 401: # not valid api key
    print("INVALID API KEY FOR BLUE SCANNER!!!")

else:
    pass

BLUE_DATABASE = {}
if response.status_code == 200: # SUCCESSFULL
    BLUE_DATABASE = json.loads(response.text) # {user_id: [case_id, reason, bancode]}
    print("BLUE SCANNER IS ONLINE!!!")


SCANNED_ID = [] # Your list of scanned user IDs
allkeys = BLUE_DATABASE.keys()
for userid in allkeys:
    userid = int(userid)
    SCANNED_ID.append(userid)
print(f"Scanned user: {SCANNED_ID}")
scanned_users = {} # Keep track of the scanned users detected in each group

NOTICE_MSG = """
CASE ID: `{}`
[{}](tg://user?id={}) is banned globally as `{}`
Reason: `{}` | Appeal By: @DevsLab
"""

def scanning(update, context):
    user_id = update.message.user.id
    if user_id in SCANNED_ID:
        bot = context.bot
        first_name = update.message.user.first_name
        chat_id = update.message.chat.id
        try:
            bot.kick_chat_member(chat_id, user_id)
            message.reply_text(
                NOTICE_MSG.format(
                    BLUE_DATABASE[str(user_id)][0],
                    first_name,
                    user_id,
                    BLUE_DATABASE[str(user_id)][2],
                    BLUE_DATABASE[str(user_id)][1]
                ),
                parse_mode=ParseMode.MARDOWN
            )
        except:
            if chat_id in scanned_users and user_id in scanned_users[chat_id]:
                return
            if chat_id not in scanned_users:
                scanned_users[chat_id] = []
            scanned_users[chat_id].append(user_id)
            message.reply_text(
                NOTICE_MSG.format(
                    BLUE_DATABASE[str(user_id)][0],
                    first_name,
                    user_id,
                    BLUE_DATABASE[str(user_id)][2],
                    BLUE_DATABASE[str(user_id)][1]
                ),
                parse_mode=ParseMode.MARKDOWN
            )
    

BLUE_SCANNING = MessageHandler(Filters.group & Filters.all, scanning)
dispatcher.add_handler(BLUE_SCANNING)
