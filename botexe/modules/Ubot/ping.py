from pyrogram import Client, filters
from pyrogram.types import Message
from botexe import startTime
from botexe import get_uptime
import time 
from config import HANDLER as hl
from botexe import grt
from botexe import Ubot

@Ubot.on_message(filters.command("ping",  hl) & filters.me)
async def ping(client, message):
    r = await client.get_me()
    st = time.time()
    end = time.time()
    user = r.mention
    upt = get_uptime(time.time())
    pong = str((end-st)*1000)[0:5]
    gtr = grt(int(time.time()-startTime))
    PING = f"""
—͟͞͞★ ʀᴀғᴛᴀʀ »  🍷
ɴᴇᴇᴅ ꜰᴏʀ ꜱᴘᴇᴇᴅ ʙᴀʙʏ 🍻
** ᴘɪɴɢ »** `{pong}`
"""
    return await message.edit(PING)
