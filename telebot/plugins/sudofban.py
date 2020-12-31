import asyncio

from telebot import CMD_HELP

# By @HeisenbergTheDanger, @its_xditya 

@telebot.on(sudo_cmd(outgoing=True, pattern="sudofban?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("STARTED A MASS-FBAN.. \nPLEASE DO NOT SEND MUCH MESSEGES TO AVOID FLOODWAIT😎")
    fedList = []
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await telebot.download_media(
                previous_message, "fedlist"
            )
            await asyncio.sleep(10)
            file = open(downloaded_file_name, "r")
            lines = file.readlines()
            for line in lines:
                try:
                    fedList.append(line[:36])
                except BaseException:
                    pass
            arg = event.pattern_match.group(1)
            args = arg.split()
            if len(args) > 1:
                FBAN = args[0]
                REASON = ""
                for a in args[1:]:
                    REASON += a + " "
            else:
                FBAN = arg
                REASON = " #MASSBAN "
        else:
            FBAN = previous_message.sender_id
            REASON = event.pattern_match.group(1)
            if REASON.strip() == "":
                REASON = " #MASSBAN "
    else:
        arg = event.pattern_match.group(1)
        args = arg.split()
        if len(args) > 1:
            FBAN = args[0]
            REASON = ""
            for a in args[1:]:
                REASON += a + " "
        else:
            FBAN = arg
            REASON = " #MASSBAN "
    try:
        int(FBAN)
        if int(FBAN) == 630654925 or int(FBAN) == 719195224:
            await event.edit("Something went wrong.")
            return
    except BaseException:
        if FBAN == "@HeisenbergTheDanger" or FBAN == "@xditya":
            await event.edit("Something went wrong.")
            return
    if Config.FBAN_GROUP_ID:
        chat = Config.FBAN_GROUP_ID
    else:
        chat = await event.get_chat()
    if not len(fedList):
        for a in range(3):
            async with telebot.conversation("@MissRose_bot") as bot_conv:
                await bot_conv.send_message("/start")
                await bot_conv.send_message("/myfeds")
                await asyncio.sleep(6)
                response = await bot_conv.get_response()
                await asyncio.sleep(8)
                if "make a file" in response.text:
                    await asyncio.sleep(8)
                    await response.click(0)
                    await asyncio.sleep(8)
                    fedfile = await bot_conv.get_response()
                    await asyncio.sleep(6)
                    if fedfile.media:
                        downloaded_file_name = await telebot.download_media(
                            fedfile, "fedlist"
                        )
                        await asyncio.sleep(6)
                        file = open(downloaded_file_name, "r")
                        lines = file.readlines()
                        for line in lines:
                            try:
                                fedList.append(line[:36])
                            except BaseException:
                                pass
                    else:
                        return
                if len(fedList) == 0:
                    await event.edit(f"Something went wrong. Retrying ({a+1}/3)...")
                else:
                    break
        else:
            await event.edit(f"Error")
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("Try again after 5 mins.")
            return
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True

            elif In:
                tempFedId += x
        if len(fedList) == 0:
            await event.edit("Something went wrong.")
            return
    await event.edit(f"Fbaning in {len(fedList)} feds.")
    try:
        await telebot.send_message(chat, f"/start")
    except BaseException:
        await event.edit("FBAN_GROUP_ID is incorrect.")
        return
    await asyncio.sleep(3)
    if Config.EXCLUDE_FED:
        excludeFed = Config.EXCLUDE_FED.split("|")
        for n in range(len(excludeFed)):
            excludeFed[n] = excludeFed[n].strip()
    exCount = 0
    for fed in fedList:
        if Config.EXCLUDE_FED and fed in excludeFed:
            await telebot.send_message(chat, f"{fed} Excluded.")
            exCount += 1
            continue
        await telebot.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(8)
        await telebot.send_message(chat, f"/fban {FBAN} {REASON} SUPERFBANNED BY SUDO ")
        await asyncio.sleep(8)
    await event.edit(
        f"SuperFBan Completed. Affected {len(fedList) - exCount} feds.\n#TB"
    )

