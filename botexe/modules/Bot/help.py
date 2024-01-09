from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import HANDLER as hl
import time
from pyrogram import Client, filters
from botexe import Bot
from config import HELP_PIC
from botexe import Ubot
from pyrogram.types import InlineQueryResultPhoto as IQRP

PIC = HELP_PIC

HELP_TEXT = "**๏ ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ʀᴀꜰᴛᴀʀ ᴜꜱᴇʀʙᴏᴛ 🌪**\n\n**๏ ʀᴀꜰᴛᴀʀ ᴜꜱᴇʀʙᴏᴛ 💕**\n\n๏ **ʙʏ © @THE_TRIO_0009 🍷**\n\n**๏ ᴘᴀɢᴇ** ~ `1/2`"
HELP_TEXTT = "**๏ ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ʀᴀꜰᴛᴀʀ ᴜꜱᴇʀʙᴏᴛ 🌪**\n\n**๏ ʀᴀꜰᴛᴀʀ ᴜꜱᴇʀʙᴏᴛ 💕**\n\n๏ **ʙʏ © @THE_TRIO_0009 🍷**\n\n**๏ ᴘᴀɢᴇ** ~ `2/2`"

ADMINS_MSG = f"""
**ᴀᴅᴍɪɴꜱ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ʙᴀɴ` » ᴛᴏ ʙᴀɴ ᴀɴʏᴏɴᴇ ɪɴ ɢᴄ...

๏ `{hl}ᴜɴʙᴀɴ` » ᴛᴏ ᴜɴʙᴀɴ ᴀɴʏᴏɴᴇ ɪɴ ɢᴄ...

๏ `{hl}ᴍᴜᴛᴇ` » ᴛᴏ ᴍᴜᴛᴇ ᴀɴʏᴏɴᴇ ɪɴ ɢᴄ...

๏ `{hl}ᴜɴᴍᴜᴛᴇ` » ᴛᴏ ᴜɴᴍᴜᴛᴇ ᴀɴʏᴏɴᴇ ɪɴ ɢᴄ..!!

๏ `{hl}ᴋɪᴄᴋ` » ᴛᴏ ᴋɪᴄᴋ ᴀɴʏᴏɴᴇ ɪɴ ɢᴄ..!!

๏ `{hl}ᴘɪɴ` » ᴛᴏ ᴘɪɴ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ..!!

๏ `{hl}ᴜɴᴘɪɴ` » ᴛᴏ ᴜɴᴘɪɴ ᴍᴇꜱꜱᴀɢᴇ..!!

๏ `{hl}ᴘʀᴏᴍᴏᴛᴇ` » ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ ᴀɴʏᴏɴᴇ..!!

๏ `{hl}ᴅᴇᴍᴏᴛᴇ` » ᴛᴏ ᴅᴇᴍᴏᴛᴇ ᴀɴʏᴏɴᴇ..!!

๏ `{hl}ꜱᴇᴛɢᴘɪᴄ` » ᴛᴏ ꜱᴇᴛ ᴘꜰᴘ ɪɴ ɢᴄ..!!
"""

EXTRA_MSG = f"""
**ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ᴘɪɴɢ` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴘɪɴɢ ᴀɴᴅ ᴜᴘᴛɪᴍᴇ..!!

๏ `{hl}ᴀʟɪᴠᴇ` » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ..!!

๏ `{hl}ʀᴇᴘᴏ` » ᴛᴏ ɢᴇᴛ ʙᴏᴛ ʀᴇᴘᴏ..!!

๏ `{hl}ꜱᴛᴀʀᴛᴠᴄ` » ᴛᴏ ꜱᴛᴀʀᴛ ᴠᴄ ɪɴ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛ..!!

๏ `{hl}ɪᴅ` » ᴛᴏ ɢᴇᴛ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ'ꜱ ᴜꜱᴇʀ_ɪᴅ..!!

๏ `{hl}ꜱɢ` » ʏᴏ ɢᴇᴛ ɴᴀᴍᴇ ʜɪꜱᴛᴏʀʏ ᴏꜰ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ..!!

๏ `{hl}ɢɪᴛɪɴꜰᴏ` <ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ɢᴇᴛ ɢɪᴛ ᴀᴄᴄ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ..!!
"""

INVITE_MSG = f"""
**ɪɴᴠɪᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ɪɴᴠɪᴛᴇ` » ᴛᴏ ᴀᴅᴅ ᴍᴇᴍʙᴇʀꜱ ɪɴ ɢᴄ ʙʏ ʜɪꜱ/ʜᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ..!!

๏ `{hl}ɪɴᴠɪᴛᴇʟɪɴᴋ` » ᴛᴏ ɢᴇᴛ ᴀɴʏ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ʟɪɴᴋ..!!

๏ `{hl}ɪɴᴠɪᴛᴇᴀʟʟ` » ᴛᴏ ɪɴᴠɪᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ᴏꜰ ᴏᴛʜᴇʀ ɢᴄ ᴛᴏ ᴜʀ ɢᴄ..!!
"""

SPAM_MSG = f"""
**ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ꜱᴘᴀᴍ` » ᴛᴏ ꜱᴘᴀᴍ ᴍᴇꜱꜱᴀɢᴇꜱ ʙʏ ᴄᴏᴜɴᴛ..!!

๏ `{hl}ʙᴀɴᴀʟʟ` » ᴛᴏ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ᴏꜰ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛꜱ..!!

๏ `{hl}ʀᴀɪᴅ` » ᴛᴏ ᴀʙᴜꜱᴇ ᴀɴʏᴏɴᴇ..!!

๏ `{ʜʟ}ᴍʀᴀɪᴅ` » ᴛᴏ ɪᴍᴘʀᴇꜱꜱ ᴀɴʏᴏɴᴇ..!!

๏ `{hl}ʀᴇᴘʟʏʀᴀɪᴅ` » ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴘʟʏʀᴀɪᴅ ᴏɴ ᴀɴʏᴏɴᴇ..!!

๏ `{hl}ᴅʀᴇᴘʟʏʀᴀɪᴅ` » ᴛᴏ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴘʟʏʀᴀɪᴅ..!!

๏ `{hl}ᴘꜱ` » ᴛᴏ ᴘᴏʀɴ ꜱᴘᴀᴍ ʙʏ ᴄᴏᴜɴᴛ..!!
"""

ACC_MSG = f"""
**ᴘʀᴏꜰɪʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ꜱᴇᴛᴘꜰᴘ` » ᴛᴏ ꜱᴇᴛ ʏᴏᴜʀ ᴘꜰᴘ..!!

๏ `{hl}ʙʟᴏᴄᴋ` » ᴛᴏ ʙʟᴏᴄᴋ ᴜꜱᴇʀ ʙʏ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ..!!

๏ `{hl}ᴜɴʙʟᴏᴄᴋ` » ᴛᴏ ᴜɴʙʟᴏᴄᴋ ᴜꜱᴇʀ ʙʏ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ..!!

๏ `{hl}ꜱᴇᴛɴᴀᴍᴇ` » ᴛᴏ ꜱᴇᴛ ɴᴀᴍᴇ ᴏꜰ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ..!!

๏ `{hl}ꜱᴇᴛʙɪᴏ` » ᴛᴏ ꜱᴇᴛ ʙɪᴏ ᴏꜰ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ..!!
"""

OTHER_MSG = f"""
**ᴏᴛʜᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ᴛʀᴜᴍᴘ` » ᴛᴏ ᴍᴀᴋᴇ ᴛʀᴜᴍᴘ ᴛᴡᴇᴇᴛ..!!

๏ `{hl}ᴜᴛᴡᴇᴇᴛ` » ᴛᴏ ᴍᴀᴋᴇ ᴛᴡᴇᴇᴛ ʙʏ ᴜꜱᴇʀɴᴀᴍᴇ..!!

๏ {hl}ꜰ<ᴀᴄᴛɪᴏɴ> » ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ > `{ʜʟ}ꜰᴛʏᴘɪɴɢ`

๏ `{hl}ᴛᴇʟᴇɢʀᴀᴘʜ` » ᴛᴏ ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏꜰ ʀᴇᴘʟʏᴇᴅ ᴍᴇᴅɪᴀ..!!

๏ `{hl}ᴄᴀʀʙᴏɴ` » ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ ᴏꜰ ɢɪᴠᴇɴ ᴛᴇxᴛ..!!

๏ `{hl}ᴘᴀꜱᴛᴇ` » ᴛᴏ ᴘᴀꜱᴛᴇ ᴀɴʏ ᴛᴇxᴛ ᴀɴᴅ ᴅᴏᴄꜱ ᴜɴ ᴍᴇᴅɪᴀ..!!
"""

LOVE_MSG = f"""
**ʟᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ʟᴏᴠᴇʀ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ᴇꜰʟɪʀᴛ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ʜꜰʟɪʀᴛ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!
"""

FUN_MSG = f"""
**ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ʟᴏᴠᴇʀ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ꜱᴛᴜᴘɪᴅ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ɪʟᴏᴠᴇᴜ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ꜱᴇx` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ᴄʜᴀɴᴄᴇ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ᴋɪꜱꜱ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ꜱʟᴀᴘ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ᴅᴀʀᴇ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!

๏ `{hl}ᴛʀᴜᴛʜ` » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ..!!
"""

PM_MSG = f"""
**ᴘᴍᴘᴇʀᴍɪᴛ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ᴘᴍᴘᴇʀᴍɪᴛ` » ᴛᴏ ᴏɴ/ᴏꜰꜰ ᴘᴍᴘᴇʀᴍɪᴛ..!!

๏ `{hl}ᴀ` » ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ᴜꜱᴇʀ ɪɴ ᴘᴍ..!!

๏ `{hl}ᴅᴀ` » ᴛᴏ ᴅɪꜱᴀᴘᴘʀᴏᴠᴇ ᴜꜱᴇʀ ɪɴ ᴘᴍ..!!
"""

NEWS_MSG = f"""
** ɴᴇᴡꜱ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ɴᴇᴡꜱ` » ᴛᴏ ɢᴇᴛ ᴛᴏᴘ ʜᴇᴀᴅʟɪɴᴇꜱ ᴏꜰ ɴᴇᴡꜱ..!!

๏ `{hl}ᴡᴇᴀᴛʜᴇʀ (ᴄɪᴛʏ ɴᴀᴍᴇ)` » ᴛᴏ ɢᴇᴛ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ..!!
"""

CONVERT_MSG = f"""
**ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ᴛᴛꜱ` » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ..!!

๏ `{hl}ɢᴇᴛꜱᴛɪᴄᴋᴇʀ` » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ᴍɪᴅᴇᴀ..!!

๏ `{hl}ᴋᴀɴɢ` » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴍɪᴅᴇᴀ ᴛᴏ ꜱᴛɪᴄᴋᴇʀ..!!

๏ `{hl}ᴡᴇʙꜱꜱ (ᴜʀʟ)` » ᴛᴏ ᴛᴀᴋᴇ ᴀɴʏ ᴡᴇʙꜱɪᴛᴇ ꜱꜱ..!!
"""

INSTA_MSG = f"""
**ɪɴꜱᴛᴀ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ᴅᴏᴡɴʟᴏᴀᴅ (ᴜʀʟ)` » ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ɪɴꜱᴛᴀ ᴘᴏꜱᴛ/ʀᴇᴇʟꜱ..!!
"""

INFO_MSG = f"""
** ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ɪɴꜰᴏ` » ᴛᴏ ɢᴇᴛ ɪɴꜰᴏ ᴀʙᴏᴜᴛ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ ᴀᴄᴄ..!!
"""

IMPORTANT_MSG = f"""
**ɪᴍᴘᴏʀᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ʀᴇꜱᴛᴀʀᴛ` » ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ..!!

๏ `{hl}ɴɪᴄᴇ` » ᴛᴏ ꜱᴀᴠᴇ ᴛɪᴍᴇʀ ᴘɪᴄ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ ɪɴ ꜱᴀᴠᴇᴅ ᴍᴇꜱꜱᴀɢᴇ..!!

๏ `{hl}ᴀꜰᴋ` » ᴛᴏ ᴇɴᴀʙʟᴇ ᴀᴋꜰ..!!

๏ `{hl}ᴇᴠᴀʟ` » ᴛᴏ ʀᴜɴ ᴀɴʏ ᴘʏᴛʜᴏɴ ᴄᴏᴅᴇꜱ..!!
"""

Q_MSG = f"""
**Q ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}Q` » ᴛᴏ ᴍᴀᴋᴇ Q..!!

๏ `{hl}ᴀɴɪ` » ᴛᴏ ᴍᴀᴋᴇ ᴀɴɪᴍᴀᴛɪᴏɴ Q..!!
"""

CREATE_MSG = f"""
**ᴄʀᴇᴀᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ**

๏ `{hl}ᴄʀᴇᴀᴛᴇ ɢʀᴏᴜᴘ (ɴᴀᴍᴇ)` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ɢʀᴏᴜᴘ..!!

๏ `{hl}ᴄʀᴇᴀᴛᴇ ᴄʜᴀɴɴᴇʟ (ɴᴀᴍᴇ)` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴄʜᴀɴɴᴇʟ..!!
"""

HELP_BUTTON = IKM(
              [
              [
              IKB("• ᴘᴍᴘᴇʀᴍɪᴛ •", callback_data='pmpermit'),
              IKB("• ɴᴇᴡꜱ •", callback_data='news')
              ],
              [
              IKB("• ɪᴍᴘᴏʀᴛᴀɴᴛ •", callback_data='important'),
              IKB("• ᴄʀᴇᴀᴛᴇ •", callback_data='create')
              ],
              [
              IKB("• Q •", callback_data='q'),
              IKB("• ɪɴꜱᴛᴀɢʀᴀᴍ •", callback_data='insta')
              ],
              [
              IKB("• ɪɴꜰᴏ •", callback_data='info'),
              IKB("• ᴄᴏɴᴠᴇʀᴛ •", callback_data='convert')
              ],
              [
              IKB(" ʜᴏᴍᴇ 🤖", callback_data='home')
              ]
              ]
              )

                
HELP_MARKUP = IKM(
              [
              [
              IKB("• ᴀᴅᴍɪɴꜱ •", callback_data="admins"),
              IKB("• ᴇxᴛʀᴀ •", callback_data="extra")
              ],
              [
              IKB("• ɪɴᴠɪᴛᴇ •", callback_data="invite"),
              IKB("• ʟᴏᴠᴇ •", callback_data="love")
              ],
              [
              IKB("• ꜱᴘᴀᴍ •", callback_data="spam"),
              IKB("• ᴘʀᴏꜰɪʟᴇ •", callback_data="pro")
              ],
              [
              IKB("• ᴏᴛʜᴇʀ •", callback_data="other"),
              IKB("• ꜰᴜɴ •", callback_data='fun')
              ],
              [
              IKB("2ɴᴅ ᴘᴀɢᴇ 📄", callback_data="2page")
              ]
              ]
              )
sux = None

BACK = IKM(
       [
       [
       IKB("🔙", callback_data="back")
       ]
       ]
       )

X = IKM(
    [
    [
    IKB("➡️", callback_data="x")
    ]
    ]
    )

@Ubot.on_message(filters.command("help", hl))
async def help(client, message):
    global sux
    if not sux:
        sux = Bot.me.username
    await message.edit("`ᴘʀᴏᴄᴇꜱꜱɪɴɢ...`")
    try:
        nice = await client.get_inline_bot_results(bot=sux, query="inline_help")
    except Exception as e:
        return await message.reply(e)
    try:
        await message.delete()
        await message.delete()
    except:
        pass
    try:
        await client.send_inline_bot_result(message.chat.id, nice.query_id, nice.results[0].id)
    except Exception as e:
        await message.reply(e)

ans = [IQRP(photo_url=HELP_PIC, thumb_url=PIC, title="Help", description="Help Menu", caption=HELP_TEXT, reply_markup=HELP_MARKUP)]

@Bot.on_inline_query()
async def inl(y, x):
    text = x.query.lower()
    try:
        if text == "inline_help":
            await y.answer_inline_query(x.id, results=ans, cache_time=0)     
    except Exception as e:
        print(e)

@Bot.on_callback_query(filters.regex("back"))
async def back(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT, reply_markup=HELP_MARKUP)
  
@Bot.on_callback_query(filters.regex("admins"))
async def admins(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=ADMINS_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("extra"))
async def extra(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=EXTRA_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("invite"))
async def invite(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=INVITE_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("spam"))
async def spam(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=SPAM_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("love"))
async def love(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=LOVE_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("pro"))
async def profile(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=ACC_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("fun"))
async def profile(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=FUN_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("other"))
async def profile(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=OTHER_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("2page"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXTT, reply_markup=HELP_BUTTON)

@Bot.on_callback_query(filters.regex("x"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXTT, reply_markup=HELP_BUTTON)

@Bot.on_callback_query(filters.regex("fun"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=FUN_MSG, reply_markup=BACK)

@Bot.on_callback_query(filters.regex("pmpermit"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=PM_MSG, reply_markup=X)

@Bot.on_callback_query(filters.regex("news"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=NEWS_MSG, reply_markup=X)


@Bot.on_callback_query(filters.regex("convert"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=CONVERT_MSG, reply_markup=X)

@Bot.on_callback_query(filters.regex("home"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=HELP_TEXT, reply_markup=HELP_MARKUP)

@Bot.on_callback_query(filters.regex("info"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=INFO_MSG, reply_markup=X)

@Bot.on_callback_query(filters.regex("insta"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=INSTA_MSG, reply_markup=X)

@Bot.on_callback_query(filters.regex("important"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=IMPORTANT_MSG, reply_markup=X)

@Bot.on_callback_query(filters.regex("pmpermit"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=PM_MSG, reply_markup=X)

@Bot.on_callback_query(filters.regex("news"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=NEWS_MSG, reply_markup=X)

@Bot.on_callback_query(filters.regex("q"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=Q_MSG, reply_markup=X)

@Bot.on_callback_query(filters.regex("create"))
async def pange(client, message):
    if message.from_user.id != Bunny.me.id:
        return await message.answer("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀᴋᴀ..!!", show_alert=True)
    await message.answer()
    await message.edit_message_text(text=CREATE_MSG, reply_markup=X)
