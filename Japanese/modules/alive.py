from telethon import __version__, events, Button
import asyncio
import sys
import heroku3
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

pongg = "𝙹𝚊𝚙𝚊𝚗𝚎𝚜𝚎 𝚇 𝚂𝚙𝚊𝚖𝚋𝚘𝚝 𝙸𝚜 𝙰𝚕𝚒𝚟𝚎 𝙱𝚊𝚋𝚢❤️💋"
PIC = "https://graph.org/file/d0cea91a72399897dfd75.mp4"
Alivemsg = "𝙹𝚊𝚙𝚊𝚗𝚎𝚜𝚎 𝚇 𝚂𝚙𝚊𝚖𝚋𝚘𝚝 𝙷𝚎𝚛𝚎 𝚋𝚊𝚋𝚢❤️💋"

TEXT = f"‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌=≡❰ • 𝙹𝚊𝚙𝚊𝚗𝚎𝚜𝚎 𝚇 𝚂𝚙𝚊𝚖𝚋𝚘𝚝 𝙸𝚜 𝙰𝚕𝚒𝚟𝚎 𝙱𝚊𝚋𝚢❤️💋 • ❱≡=\n"
TEXT = f"‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌🚀 ʙᴏᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ 🚀\n"
TEXT += f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
TEXT += f"**• ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ**🐍: `3.11.3`\n"
TEXT += f"**• ꜱᴘᴀᴍʙᴏᴛ ᴠᴇʀꜱɪᴏɴ**⚙️: `M2.0`\n"
TEXT += f"**• ɢʀᴏᴜᴘ ❤️: [Jᴀᴘᴀɴᴇsᴇ ɢʀᴏᴜᴘ ✨](https://t.me/Japanese_Userbot_Chat)**\n"
TEXT += f"**• ᴄʜᴀɴɴᴇʟ ✨: [Jᴀᴘᴀɴᴇsᴇ ᴄʜᴀɴɴᴇʟ ✨](https://t.me/Japanese_Userbot)**\n"
TEXT += f"**• ᴅᴇᴠ 🫂: [Nᴏʙɪᴛᴀ Xᴅ ✨](https://t.me/Nobitaa_xd)**\n"
TEXT += f"➖➖➖➖➖➖➖➖➖➖➖➖"
                                  
@X1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  PIC,
                                  caption=TEXT,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Japanese_Userbot"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/Japanese_Userbot_Chat")
        ],
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
