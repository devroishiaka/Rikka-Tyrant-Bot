# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/yumeko/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 10938772  # integer value, dont use "6973446"
    API_HASH = "b5e29cb144a6cb6f69884f39cecd212e"
    TOKEN = "BOT_TOKEN"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "5030730429"  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "ishikki_akabane"
    SUPPORT_CHAT = "botslabxd"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001631997698
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001691108474
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://ishikki:OUJm5DA5ya0NtmXxlt4uYOHnSQE975XV@dpg-cfe70ccgqg46rpmlkku0-a.oregon-postgres.render.com/chizuru_kcfb"  # needed for any database modules
    MONGO_DB_URI = "mongodb+srv://ishikki143:ishikki143@cluster0.sbxugre.mongodb.net/?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "XChWQMRDLpKVqoirR_cMDqlrGwiTn1bY1pYhTyGeVv7~T2gVG1JRyZFvlZGq4gtG"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@botslabxd"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "dragons")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs)
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "demons")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "wolfes")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "URWAVM2BWHQPCWCZ"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "TNOI2DHS7GLK"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
