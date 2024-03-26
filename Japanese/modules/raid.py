import asyncio

from random import choice

from telethon import events

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from Japanese.data import RAID, REPLYRAID, DEV

REPLY_RAID = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in DEV:
                await e.reply("𝙽𝙾𝙿𝙴,𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝚆𝙰𝙽𝙳𝙴𝚁𝙸𝙽𝙶'𝚂 𝙾𝚆𝙽𝙴𝚁 𝙵𝚄𝙲𝙺𝙸𝙽𝙶 𝙲𝙾𝚆𝙰𝚁𝙳 𝙱𝙰𝙱𝚈 𝙰𝙷𝙷𝙷𝙷𝙷𝙷𝙷 ❤️💋 ")
            elif uid == OWNER_ID:
                await e.reply("ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ❤️")
            elif uid in SUDO_USERS:
                await e.reply("𝙽𝙾𝙿𝙴, 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙱𝙰𝙱𝚈 ❤️💋")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝙼𝙾𝙳𝚄𝙻𝙴 𝙽𝙰𝙼𝙴 : 𝚁𝙰𝙸𝙳\n  » {hl}𝚁𝙰𝙸𝙳 <𝙲𝙾𝚄𝙽𝚃> <𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 𝙾𝚏 𝚄𝚜𝚎𝚛 𝚋𝚊𝚋𝚢❤️💋>\n  » {hl}𝚁𝙰𝙸𝙳 <𝙲𝙾𝚄𝙽𝚃> <𝚁𝚎𝚙𝚕𝚢 𝚃𝚘 𝙰 𝚄𝚜𝚎𝚛 𝚋𝚊𝚋𝚢❤️💋>")
        except Exception as e:
            print(e)


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
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in DEV:
                await e.reply("𝙽𝙾𝙿𝙴,𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝚆𝙰𝙽𝙳𝙴𝚁𝙸𝙽𝙶'𝚂 𝙾𝚆𝙽𝙴𝚁 𝙵𝚄𝙲𝙺𝙸𝙽𝙶 𝙲𝙾𝚆𝙰𝚁𝙳 𝙱𝙰𝙱𝚈 𝙰𝙷𝙷𝙷𝙷𝙷𝙷𝙷 ❤️💋 ")
            elif user_id == OWNER_ID:
                await e.reply("ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ❤️")
            elif user_id in SUDO_USERS:
                await e.reply("𝘕𝙽𝙾𝙿𝙴, 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙱𝙰𝙱𝚈 ❤️💋")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» 𝙰𝙲𝚃𝙸𝚅𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝚈𝚁𝙰𝙸𝙳 !! ✅")
        except NameError:
            await e.reply(f"𝙼𝙾𝙳𝚄𝙻𝙴 𝙽𝙰𝙼𝙴 : RRAID\n  » {hl}𝚁𝚁𝙰𝙸𝙳 <𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 𝙾𝚏 𝚄𝚜𝚎𝚛 𝚋𝚊𝚋𝚢❤️💋>\n  » {hl}𝚁𝚁𝙰𝙸𝙳  <𝚁𝚎𝚙𝚕𝚢 𝚃𝚘 𝙰 𝚄𝚜𝚎𝚛 𝚋𝚊𝚋𝚢❤️💋>")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» 𝙳𝙴-𝙰𝙲𝚃𝙸𝚅𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝚈𝚁𝙰𝙸𝙳 !! ✅")
        except NameError:
            await e.reply(f"𝙼𝙾𝙳𝚄𝙻𝙴 𝙽𝙰𝙼𝙴 : 𝙳𝚁𝚁𝙰𝙸𝙳\n  » {hl}𝙳𝚁𝚁𝙰𝙸𝙳 <𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 𝙾𝚏 𝚄𝚜𝚎𝚛 𝚋𝚊𝚋𝚢❤️💋>\n  » {hl}𝙳𝚁𝚁𝙰𝙸𝙳 <𝚁𝚎𝚙𝚕𝚢 𝚃𝚘 𝙰 𝚄𝚜𝚎𝚛 𝚋𝚊𝚋𝚢❤️💋>")
