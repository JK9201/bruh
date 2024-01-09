from botexe.powers import extract_user
from pyrogram import Client, filters
from config import HANDLER as hl
from botexe import Ubot
from pyrogram.types import Message

@Ubot.on_message(filters.command(["block"], hl) & filters.me)
async def block(client: Client, message: Message):
    user_id = await extract_user(message)
    Ubot = await message.edit("`ᴘʀᴏᴄᴇꜱꜱɪɴɢ...⚡`")
    if not user_id:
        return await message.edit(
            "ɢɪᴠᴇ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʟᴏᴄᴋ..!!"
        )
    if user_id == client.me.id:
        return await bunny.edit("ɪ ᴄᴀɴ'ᴛ ʙʟᴏᴄᴋ ᴍʏsᴇʟғ ʟᴏʟ..!!")
    await client.block_user(user_id)
    geek = (await client.get_users(user_id)).mention
    await message.edit(f"__**๏ {geek} ʙʟᴏᴄᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**__")
