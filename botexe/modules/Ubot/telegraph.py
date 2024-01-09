from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import Telegraph, exceptions, upload_file
from config import HANDLER as hl
from botexe.powers import *
from botexe import Ubot

telegraph = Telegraph()
r = telegraph.create_account(short_name="R A F T A R")
auth_url = r["auth_url"]


@Ubot.on_message(filters.command(["tgm", "telegraph"], hl) & filters.me)
async def uptotelegraph(client: Client, message: Message):
    Ubot = await message.edit("`ρɾσƈҽʂʂιɳɠ...⚡`")
    if not message.reply_to_message:
        await Ubot.edit(
            "**__reply to the message, to get Telegraph link....__**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await Ubot.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        dones = (
            f"**๏ Successfully uploaded to** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await Ubot.edit(dones)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await Ubot.edit(f"**ERROR:** `{exc}`")
            return
        geek = f"**๏ Successfully uploaded to** [Telegraph](https://telegra.ph/{response['path']})"
        await Ubot.edit(geek)
