from userbot.utils import admin_cmd
from selenium import webdriver
import requests
import html

@borg.on(admin_cmd(pattern="bin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    try:
        kek = event.pattern_match.group(1)
        url = f"https://lookup.binlist.net/{kek}"
        midhunkm = requests.get(url=url).json()
        kekvro = midhunkm["country"]
        ninja = midhunkm["bank"]
        data_is = (f"✅ Provided Bin is Valid!\n\n<b>Bin</b>: {kek} \n"
           f"<b>Brand</b>: {midhunkm['scheme']} \n"
           f"<b>Level</b>: {midhunkm['brand']} \n"
           f"<b>Bank</b>: {kekvro['name']} \n"
           f"<b>Country</b>: {kekvro['name']} {kekvro['emoji']} \n\n"
           f"🌐<b>Info Provided By Ninja Userbot</b>🌐 \n")
        await event.edit(data_is, parse_mode="HTML")
    except:
        await event.edit("Not a Valid Bin Or Don't Have Enough Info.")

                   
@borg.on(admin_cmd(pattern="iban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    inputs = event.pattern_match.group(1)
    api = f"https://openiban.com/validate/{inputs}?getBIC=true&validateBankCode=true"
    lol = requests.get(url=api).json()
    try:
        banks = lol["bankData"]
        kek = (f"<b>Provided IBAN is Valid:</b>: {lol['valid']} \n"
           f"<b>IBAN</b>: {lol['iban']} \n"
           f"<b>BANK-CODE</b>: {banks['bankCode']} \n"
           f"<b>BANK-NAME</b>: {banks['name']} \n"
           f"<b>ZIP</b>: {banks['zip']} \n"
           f"<b>CITY</b>: {banks['city']} \n"
           f"<b>BIC</b>: {banks['bic']} \n\n"
         f"🌐<b>Info Provided By Ninja Userbot</b>🌐 \n")
        await event.edit(kek, parse_mode="HTML")
    except:
        await event.edit(f"Invalid IBAN Or Doesn't Have Enough Info")