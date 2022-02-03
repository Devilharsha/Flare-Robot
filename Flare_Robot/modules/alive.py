import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Flare_Robot.events import register
from Flare_Robot import telethn as tbot


PHOTO = "https://telegra.ph//file/8be8938f6a7f17df7d65c.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = "**♡ I,m ғʟᴀʀᴇ ʀᴏʙᴏᴛ 愛** \n\n"
    TEXT += f"**♡ I'm Working With ultra flame Speed** \n\n"
    TEXT += f"**♡ ғʟᴀʀᴇ: LATEST Version** \n\n"
    TEXT += f"**♡ My Creator: [ ᴀsᴛᴀ](http://t.me/harshahero)** \n\n"
    TEXT += f"**♡ ᴀɴʏ ɪssᴜᴇs ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ @SenkuChat** \n\n"
    TEXT += "**♡ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ 💘💘💘**"
    BUTTON = [
        [
            Button.url("📢 Updates", "https://t.me/SENKUBOTS"),
            Button.url("🚑 Support", "https://t.me/SENKUCHAT"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
