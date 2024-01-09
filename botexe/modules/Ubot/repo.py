from pyrogram import Client, filters
from botexe import Ubot
from config import HANDLER as hl

@Ubot.on_message(filters.command("repo", hl) & filters.me)
async def repo(client, message):
    msg = f"""
    **R A F T A R**

    ๏ **__GitHub**__ » [click here](https://t.me/THE_TRIO_0009) 
    ๏ **__Support**__ » [click here](https://t.me/THE_TRIO_0009) 
    ๏ **__Updates**__ » [click here](https://t.me/THE_TRIO_0009)

    **R A F T A R**
    """
    await message.edit(msg)
