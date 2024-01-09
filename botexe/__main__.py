from botexe import Ubot, Bot
import asyncio
import time
import importlib
from pyrogram import Client, idle
from botexe.modules import ALL_MODULES
from config import LOGGER_ID

async def start_user():
    await Ubot.start()
    print("[•R A FT A R•]: ᴇᴠᴇʀʏᴛʜɪɴɢ ɪꜱ ᴏᴋ, ꜱᴛᴀʀᴛɪɴɢ... ʏᴏᴜʀ ᴜꜱᴇʀʙᴏᴛ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ... ⚡")
    for all_module in ALL_MODULES:
        importlib.import_module("Imshivaexe.modules" + all_module)
        print(f"[•R A F T A R•] ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ɪᴍᴘᴏʀᴛᴀᴛᴇᴅ {all_module} ⚡")
    await Ubot.start()
    x = await Ubot.get_me()
    print(f"ᴜꜱᴇʀʙᴏᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴛᴀʀᴛᴇᴅ ᴀꜱ {x.first_name} ⚡ ")
    try:
     await Ubot.join_chat("DevilSupportChat")
     await Ubot.join_chat("UNI_INDIA_0008")
    except:
      pass
    try:
     await Ubot.send_message(LOGGER_ID, "__**ѕ—͟͞͞★ 𝑺ț𝒶𝕣țₑԀ ★**__")
     await Bot.send_message(LOGGER_ID, "__**—͟͞͞★ 𝑺ț𝒶𝕣țₑԀ ★**__")
    except:
      pass
    await idle()
  
loop = asyncio.get_event_loop()
loop.run_until_complete(start_user())
