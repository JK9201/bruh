import sys
import logging
from os import environ, execle, remove
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HANDLER as hl
from botexe import Ubot

GEEK = None

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

@Ubot.on_message(filters.command("restart", hl) & filters.me)
async def restart_bot(client, message: Message):
    try:
        msg = await message.edit("`ʀᴇꜱᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
        LOGGER(__name__).info("ʀᴇꜱᴛᴀʀᴛɪɴɢ ʙᴏᴛ ꜱᴇʀᴠᴇʀ....")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("**ʀᴇꜱᴛᴀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ..||**\n\n")
    if GEEK is not None:
        GEEK.restart()
    else:
        args = [sys.executable, "-m", "botexe"]
        execle(sys.executable, *args, environ)
