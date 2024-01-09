from pyrogram import Client, filters
from config import HANDLER as hl
from botexe import Ubot
from pyrogram.types import Message
import asyncio


@Ubot.on_message(filters.command(["sex", "sux"], hl) & filters.me)
async def hearts(client: Client, message: Message):
    await message.edit("🤵‍♂               👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂            👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂       👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂👼👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂              👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂        👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂   👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂👼👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂              👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂        👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂   👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂👼👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂              👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂        👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂   👰‍♀")
    await asyncio.sleep(0.5)
    await message.edit("🤵‍♂👼👰‍♀")
