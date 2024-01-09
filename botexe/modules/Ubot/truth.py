from pyrogram import Client, filters
from botexe import Ubot
from config import HANDLER as hl
from botexe.Data.truth import TRUTH
import random

@Ubot.on_message(filters.command("truth",  hl) & filters.me)
async def truth(client, message):
    msg = random.choice(TRUTH)
    await message.edit(msg)
