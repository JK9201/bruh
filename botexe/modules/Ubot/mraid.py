from pyrogram import Client, filters
from botexe.powers import get_id
from botexe.Data.mraid import *
import random 
from config import HANDLER as hl
from botexe import Ubot

@Ubot.on_message(filters.command("mraid", hl) & filters.me)
async def mraid(client, message):
    usage = f"`{hl}ᴍʀᴀɪᴅ [ᴄᴏᴜɴᴛ] [ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ]`"
    try:
        if message.reply_to_message:
            count = int(message.text.split()[1])
            id = message.reply_to_message.from_user.id
        else:
            count = int(message.text.split()[1])
            txt = message.text.split()[2]
            try:
                id = int(txt)
            except:
                id = (await client.get_users(txt)).id
    except:
        return await message.edit(usage)
    user = (await client.get_users(id)).mention
    for i in range(0, count):
        await client.send_message(message.chat.id, f" {user}"+ random.choice(MRAID))
