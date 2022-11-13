import random

from telethon import Button, events

from Yumeko import telethn as asst


BUTTON = [[Button.url("WHO ADDED THIS FEATURE❓", "https://t.me/kakashi_bots_updates/22")]]
HOT = "https://telegra.ph/file/20d6f58b629bfc8303c16.mp4"
SMEXY = "https://telegra.ph/file/bc1aef9db142d775de4af.mp4"
LEZBIAN = "https://telegra.ph/file/4bfaffdaa56a5eb515ed3.mp4"
BIGBALL = "https://telegra.ph/file/3017e2197e5f2b084f34b.mp4"
LANG = "https://telegra.ph/file/a922b51801f22d7859542.mp4"
CUTIE = "https://telegra.ph/file/f7493019b920c58905e8f.mp4"


@asst.on(events.NewMessage(pattern="/horny ?(.*)"))
async def horny(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HORNY = f"**🔥** {mention} **Is** {mm}**% Horny!**"
    await e.reply(HORNY, file=HOT)


@asst.on(events.NewMessage(pattern="/gay ?(.*)"))
async def gay(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAY = f"**🏳‍🌈** {mention} **Is** {mm}**% Gay!**"
    await e.reply(GAY, file=SMEXY)


@asst.on(events.NewMessage(pattern="/lezbian ?(.*)"))
async def lezbian(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    FEK = f"**💜** {mention} **Is** {mm}**% Lezbian!**"
    await e.reply(FEK, file=LEZBIAN)


@asst.on(events.NewMessage(pattern="/boobs ?(.*)"))
async def boobs(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BOOBS = f"**🍒** {mention}**'s Boobs Size Is** {mm}**!**"
    await e.reply(BOOBS, file=BIGBALL)


@asst.on(events.NewMessage(pattern="/cock ?(.*)"))
async def cock(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    COCK = f"**🍆** {mention}**'s Cock Size Is** {mm}**cm**"
    await e.reply(COCK, file=LANG)


@asst.on(events.NewMessage(pattern="/cute ?(.*)"))
async def cute(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"**🍑** {mention} {mm}**% Cute**"
    await e.reply(CUTE, file=CUTIE)


__mod_name__ = "How-All"
