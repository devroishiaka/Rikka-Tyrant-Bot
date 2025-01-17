#BLUE SCANNER
#CREATED BY ISHIKKI_AKABANE
#Need any help, then visit @DevsLab

import json
import requests
from pyrogram import Client, filters
from pyrogram.types import Message, Chat
from pyrogram.types import ChatPermissions
"""import your pyrogram client as pbot"""
from Yumeko import pbot

api_key = "kazumablue-663967744872-5030730429-water-f-divison" #Get it from @BlueXDBot by /token

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
print(SCANNED_ID)

scanned_users = {} # Keep track of the scanned users detected in each group
NOTICE_MSG = """
CASE ID: `{}`
{} is banned globally as `{}`
Reason: `{}` | Appeal By: @DevsLab
"""


@pbot.on_message(filters.group & filters.all)
async def scanning(client, message: Message):
    if message.from_user is None:
	    return
    if message.from_user.id in SCANNED_ID:
        chat_id = message.chat.id
        try:
            await client.ban_chat_member(chat_id, message.from_user.id)
            await message.reply_text(
                NOTICE_MSG.format(
                    BLUE_DATABASE[str(message.from_user.id)][0],
                    message.from_user.mention(message.from_user.first_name),
                    BLUE_DATABASE[str(message.from_user.id)][2],
                    BLUE_DATABASE[str(message.from_user.id)][1]
                )
            )
        except Exception as e:
            if chat_id in scanned_users and message.from_user.id in scanned_users[chat_id]:
                return
            if chat_id not in scanned_users:
                scanned_users[chat_id] = []
            scanned_users[chat_id].append(message.from_user.id)
            await message.reply_text(
                NOTICE_MSG.format(
                    BLUE_DATABASE[str(message.from_user.id)][0],
                    message.from_user.mention(message.from_user.first_name),
                    BLUE_DATABASE[str(message.from_user.id)][2],
                    BLUE_DATABASE[str(message.from_user.id)][1]
                )
            )
