import asyncio

from .. import CMD_HELP

LOGGER_GROUP = Var.PRIVATE_GROUP_ID

# ported by @its_xditya


@telebot.on(admin_cmd(pattern="tspam"))
@telebot.on(sudo_cmd(pattern="tspam", allow_sudo=True))
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()


@telebot.on(admin_cmd(pattern="ispam"))
@telebot.on(sudo_cmd(pattern="ispam", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@"):
        message = e.text
        counter = int(message[7:9])
        spam_message = str(e.text[9:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


@telebot.on(admin_cmd(pattern="ibigspam"))
@telebot.on(sudo_cmd(pattern="ibigspam", allow_sudo=True))
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@"):
        message = e.text
        counter = int(message[10:14])
        spam_message = str(e.text[14:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


@telebot.on(admin_cmd(pattern="picspam"))
@telebot.on(sudo_cmd(pattern="picspam", allow_sudo=True))
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        link = str(text[2])
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, link)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#PICSPAM \n\n" "PicSpam was executed successfully"
            )


@telebot.on(admin_cmd(pattern="delayspam (.*)"))
@telebot.on(sudo_cmd(pattern="delayspam (.*), allow_sudo=True"))
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(" ", 2)[0])
    counter = int(e.pattern_match.group(1).split(" ", 2)[1])
    spam_message = str(e.pattern_match.group(1).split(" ", 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if LOGGER:
        await e.client.send_message(
            LOGGER_GROUP, "#DelaySPAM\n" "DelaySpam was executed successfully"
        )


CMD_HELP.update(
    {
        "spammer": ".tspam <sentence>\nUse - Text spam\
        \n\n.ispam <number> <sentence>\nUse - Spam\
        \n\n.ibigspam <number> <sentence>\nUse - Bigger Spam\
        \n\n.picspam <reply to pic>\nUse - Picture Spam\
        \n\n.delayspam <time> <word>\nUse - Spam, with some time delay!"
    }
)
