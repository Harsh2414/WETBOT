import asyncio

from telethon import events


@telebot.on(admin_cmd(pattern="(bin|vbv|me|key|iban)(.*)", outgoing=True))
async def _(event):
    chat = "carol5_bot"
    input_str = event.pattern_match.group(1)
    b = event.pattern_match.group(2)
    if input_str == "bin":
        a = f"/bin {b}"
    elif input_str == "vbv":
        a = f"/vbv {b}"
    elif input_str == "me":
        a = f"/me {b}"
    elif input_str == "key":
        a = f"/key {b}"
    elif input_str == "iban":
        a = f"/iban {b}"
    else:
        return

    async with event.client.conversation(chat) as conv:
        response = conv.wait_event(
            events.NewMessage(incoming=True, from_users=1247032902)
        )
        await event.client.send_message(chat, "/start")
        await asyncio.sleep(3)
        await event.client.send_message(chat, a)
        response = await response
        await event.client.send_message(event.chat_id, response.message)
        await event.delete()
