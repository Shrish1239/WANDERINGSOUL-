from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl

from telethon import events
from telethon.tl.functions.channels import LeaveChannelRequest


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:

        if len(e.text) > 7:
            event = await e.reply("» 𝚂𝙿𝙰𝙼𝙼𝙴𝚁 𝙻𝙴𝙰𝚅𝙸𝙽𝙶 𝙱𝙰𝙱𝚈 𝙹𝚄𝚂𝚃 𝚆𝙰𝙸𝚃 𝙰𝙽𝙳 𝚆𝙰𝚃𝙲𝙷❤️💋...")
            mkl = e.text.split(" ", 1)
            try:
                await event.client(LeaveChannelRequest(int(mkl[1])))
            except Exception as e:
                await event.edit(str(e))
        else:
             if e.is_private:
                  alt = f"**» 𝚈𝙾𝚄 𝙲𝙰𝙽'𝚃 𝙳𝙾 𝚃𝙷𝙸𝚂 𝙷𝙴𝚁𝙴 𝙱𝙰𝙱𝚈 💋👻 !!**\n\n» {hl}𝙻𝙴𝙰𝚅𝙸𝙽𝙶 : 𝚃𝚈𝙿𝙴 𝚃𝙷𝙸𝚂 𝙸𝙽 𝙶𝚁𝙾𝚄𝙿"
                  await e.reply(alt)
             else:
                  event = await e.reply("» 𝚂𝙿𝙰𝙼𝙼𝙴𝚁 𝙻𝙴𝙰𝚅𝙸𝙽𝙶 𝙱𝙰𝙱𝚈 𝙹𝚄𝚂𝚃 𝚆𝙰𝙸𝚃 𝙰𝙽𝙳 𝚆𝙰𝚃𝙲𝙷❤️💋...")
                  try:
                      await event.client(LeaveChannelRequest(int(e.chat_id)))
                  except Exception as e:
                      await event.edit(str(e))
