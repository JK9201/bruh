from pyrogram import Client, filters
from botexe import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from config import LOGGER_ID
from botexe import Ubot

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('• ɢʀᴏᴜᴘ •', url='https://t.me/DevilSupportChat'),
            InlineKeyboardButton("• ᴄʜᴀɴɴᴇʟ •", url='https://t.me/UNI_INDIA_0008')
        ],
        [
            InlineKeyboardButton("• ʀᴇᴘᴏ •", url='https://t.me/FriendCastel')
        ]
    ]
)


START_TEXT = """
__**ʜᴇʏ 💕**__ {}

**ᴍʏ ᴍᴀꜱᴛᴇʀ 🫂** {}

**ʙʏ 👀 @THE_TRIO_0009 💕**
"""

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(client, message :Message):
    x = Ubot.me.mention
    await message.reply_text(
        text=START_TEXT.format(message.from_user.first_name, x),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=START_BUTTONS
    )

@Bot.on_message(filters.incoming & filters.private,group=-1)
async def cid(shiva, message):
          await message.forward(LOGGER_ID)
