from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"""
**[𝚆𝙰𝙽𝙳𝙴𝚁𝙸𝙽𝙶 𝚇 𝚂𝙿𝙰𝙼𝙱𝙾𝚃](https://t.me/Homosapienhu) 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄** ❤️

**𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 [𝚆𝙰𝙽𝙳𝙴𝚁𝙸𝙽𝙶 𝚇 𝚂𝙿𝙰𝙼𝙱𝙾𝚃](https://t.me/Homosapienhu)** ✨

**- 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: [𝚆𝙰𝙽𝙳𝙴𝚁𝙸𝙽𝙶 ᴄʜᴀɴɴᴇʟ](https://t.me/sudeokeliyeaajaobclog)**
**- 𝚂𝚄𝙿𝙿𝙾𝚁𝚃: [𝚆𝙰𝙽𝙳𝙴𝚁𝙸𝙽𝙶 ꜱᴜᴘᴘᴏʀᴛ](https://t.me/sudeokeliyeaajaobclog)**
"""
HELP_BUTTON = [
    [
      Button.inline("✧ 𝚂𝙿𝙰𝙼 ✧", data="spam"),
      Button.inline("✧ 𝚁𝙰𝙸𝙳 ✧", data="raid")
    ],
    [
      Button.inline("✧ 𝙴𝚇𝚃𝚁𝙰𝚂 ✧", data="extra"),
      Button.inline("✧ 𝙾𝚆𝙽𝙴𝚁 ✧", data="owner")
    ],
    [
      Button.url("✧ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✧", "https://t.me/sudeokeliyeaajaobclog")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://graph.org/file/bef47c3e48580593b9d92.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"𝙰𝙽 𝙴𝚇𝙲𝙴𝙿𝚃𝙸𝙾𝙽 𝙾𝙲𝙲𝚄𝚁𝚁𝙴𝙳!\n\n**𝙴𝚁𝚁𝙾𝚁:** {str(e)}")


extra_msg = f"""
**» 𝙴𝚇𝚃𝚁𝙰 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂⦂**

 ✧ 𝙲𝙷𝙴𝙲𝙺 𝙿𝙸𝙽𝙶

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}𝙿𝙸𝙽𝙶

 ✧ 𝚁𝙴𝚂𝚃𝙰𝚁𝚃 𝙱𝙾𝚃 𝙸𝚃 𝚆𝙸𝙻𝙻 𝙱𝙴 𝚃𝙰𝙺𝙴 5 𝙼𝙸𝙽𝚄𝚃𝙴𝚂

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ʀᴇꜱᴛᴀʀᴛ
🔸 {hl}ʀᴇʙᴏᴏᴛ

 ˣ ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ᴇᴄʜᴏ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʀᴍᴇᴄʜᴏ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ʟᴇᴀᴠᴇ (ɢʀᴏᴜᴘ/ᴄʜᴀᴛ ɪᴅ)
🔸 {hl}ʟᴇᴀᴠᴇ (ʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ)

 ˣ ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ʜᴀɴɢ (ᴄᴏᴜɴᴛᴇʀ)

 ˣ ꜱᴇɴᴅꜱ ᴇᴍᴏᴊɪ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛᴇʀ ᴏɴ ᴜꜱᴇʀ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ᴇᴍᴏᴊɪ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ᴇᴍᴏᴊɪ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ʟᴏᴠᴇʀᴀɪᴅ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ʟᴏᴠᴇʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜰʟɪʀᴛꜱ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛᴇʀ ᴏɴ ᴜꜱᴇʀ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ꜰʟɪʀᴛ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ꜰʟɪʀᴛ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ꜱʀᴀɪᴅ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ꜱʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ) 

**© @Nobitaa_xd**
"""


owner_msg = f"""
**» ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ⦂**

 ˣ ꜱᴜᴅᴏ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ꜱᴜᴅᴏ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

**© @Nobitaa_xd**
"""      
          
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

 ˣ ꜱᴛᴀʀᴛ ᴛʜᴇ ʀᴀɪᴅ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ʀᴀɪᴅ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʀᴀɪᴅ (ᴄᴏᴜɴᴛꜱ) (ᴜꜱᴇʀɴᴀᴍᴇ)

 ˣ ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀᴛ.

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ʀʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʀʀᴀɪᴅ (ᴜꜱᴇʀɴᴀᴍᴇ)

 ˣ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ᴅʀʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ᴅʀʀᴀɪᴅ (ᴜꜱᴇʀɴᴀᴍᴇ)

**© @Nobitaa_xd**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

 ˣ ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ)
🔸 {hl}ꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏɪɴɢ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ)

 ˣ ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ᴘꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ)

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ɢᴍ (ᴄᴏᴜɴᴛꜱ)
🔸 {hl}ɢᴍ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ɢᴍ -ᴜ
🔸 {hl}ɢᴍ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴀꜰᴛᴇʀɴᴏᴏɴ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ɢᴀ (ᴄᴏᴜɴᴛꜱ)
🔸 {hl}ɢᴀ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ɢᴀ -ᴜ
🔸 {hl}ɢᴀ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ɴɪɢʜᴛ

👨‍💻 𝚄𝚂𝙰𝙶𝙴 :
🔸 {hl}ɢɴ (ᴄᴏᴜɴᴛꜱ)
🔸 {hl}ɢɴ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ɢɴ -ᴜ
🔸 {hl}ɢɴ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

** © @Nobitaa_xd**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("✧ 𝚂𝙿𝙰𝙼 ✧", data="spam"),
                Button.inline("✧ 𝚁𝙰𝙸𝙳 ✧", data="raid")
              ],
              [
                Button.inline("✧ 𝙴𝚇𝚃𝚁𝙰𝚂 ✧", data="extra"),
                Button.inline("✧ 𝙾𝚆𝙽𝙴𝚁 ✧", data="owner")
              ],
              [
                Button.url("✧ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✧", "https://t.me/Japanese_Userbot_Chat")
              ]
            ]
          )
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ Jᴀᴘᴀɴᴇsᴇ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @Nobitaa_xd", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
              ) 
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ Jᴀᴘᴀɴᴇsᴇ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @Nobitaa_xd", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
          )
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ Jᴀᴘᴀɴᴇsᴇ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @Nobitaa_xd", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
            )
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ 𝚆𝙰𝙽𝙳𝙴𝚁𝙸𝙽𝙶 ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @Homosapienhu", cache_time=0, alert=True) 
