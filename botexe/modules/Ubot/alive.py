from pyrogram import Client, filters
from botexe import startTime
from botexe import Ubot
from botexe import get_uptime
from botexe import ALIVE_PIC
from pyrogram import __version__ as py_version
from platform import python_version
from config import HANDLER as hl
import asyncio
import time
version = "v1.0"

@Ubot.on_message(filters.command("alive",  hl) & filters.me)
async def alive(client, message):
    sex = await message.edit("`ᴘʀᴏᴄᴇꜱꜱɪɴɢ....⚡`")
    await asyncio.sleep(0.3)
    user = (await client.get_me()).mention
    upt = get_uptime(time.time())
    await sex.edit("`ʀᴀꜰᴛᴀʀ ɪꜱ ᴀʟɪᴠᴇ...⚡`")
    await asyncio.sleep(0.3)
    await sex.edit("`ɢᴇᴛᴛɪɴɢ ʙᴏᴛ ᴅᴇᴛᴀɪʟꜱ...⚡`")
    aliver = f"""
╭────────────────๏
╰๏**ʀᴀꜰᴛᴀʀ ɪꜱ ᴀʟɪᴠᴇ 💕**
╰๏ **ᴍᴀꜱᴛᴇʀ 🫂 »** {user}
╰๏ **ᴜᴘᴛɪᴍᴇ ⌛ »** `{upt}`
╰────────────────๏
"""
    await asyncio.sleep(0.3)
    await sex.delete()
    await message.reply_photo(ALIVE_PIC, caption=aliver)
