# pmpermit for VAMPBOT.....

import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import userbot.plugins.sql_helper.pmpermit_sql as vamp_sql
from userbot import ALIVE_NAME, bot
from userbot.config import Config
from var import Var
VAMPUSER = str(ALIVE_NAME) if ALIVE_NAME else "Userbot"
from userbot.utils import vamp_cmd

VAMP_WRN = {}
VAMP_REVL_MSG = {}

VAMP_PROTECTION = Config.VAMP_PRO

SPAM = os.environ.get("SPAM", None)
if SPAM is None:
    HMM_LOL = "5"
else:
    HMM_LOL = SPAM

VAMP_PM = os.environ.get("VAMP_PM", None)
if VAMP_PM is None:
    CUSTOM_VAMP_PM_PIC = "https://telegra.ph/file/53aed76a90e38779161b1.jpg"
else:
    CUSTOM_VAMP_PM_PIC = VAMP_PM
FUCK_OFF_WARN = f"Blocked You Bitch You Spammed {VAMPUSER} IDC Why You Are Here Just Fuck Off 🖕"




OVER_POWER_WARN = (
    f"**Hello Sir Im Here To Protect {VAMPUSER} Dont Under Estimate Me 😂😂  **\n\n"
    f"`My Master {VAMPUSER} is Busy Right Now !` \n"
    f"{VAMPUSER} Is Very Busy Why Came Please Lemme Know Choose Your Deasired Reason"
    f"**Btw Dont Spam Or Get Banned** 😂😂 \n\n"
    f"**{CUSTOM_VAMP_PM_PIC}**\n"
)

VAMP_STOP_EMOJI = (
    "✋"
)
if Var.PRIVATE_GROUP_ID is not None:
    @bot.on(events.NewMessage(outgoing=True))
    async def vamp_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not vamp_sql.is_approved(chat.id):
                if not chat.id in VAMP_WRN:
                    vamp_sql.approve(chat.id, "outgoing")
                    bruh = "Auto-approved bcuz outgoing 😄😄"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()  

    @borg.on(vamp_cmd(pattern="(a|approve)"))
    async def block(event):
        if event.fwd_from:
            return
        replied_user = await borg(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chats = await event.get_chat()
        if event.is_private:
            if not vamp_sql.is_approved(chats.id):
                if chats.id in VAMP_WRN:
                    del VAMP_WRN[chats.id]
                if chats.id in VAMP_REVL_MSG:
                    await VAMP_REVL_MSG[chats.id].delete()
                    del VAMP_REVL_MSG[chats.id]
                vamp_sql.approve(chats.id, f"Wow lucky You {VAMPUSER} Approved You")
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(firstname, chats.id)
                )
                await asyncio.sleep(3)
                await event.delete()

    @borg.on(vamp_cmd(pattern="block$"))
    async def vamp_approved_pm(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if vamp_sql.is_approved(chat.id):
                vamp_sql.disapprove(chat.id)
            await event.edit("Blocked [{}](tg://user?id={})".format(firstname, chat.id))
            await asyncio.sleep(2)
            await event.edit("Now Get Lost Retard [{}](tg://user?id={})".format(firstname, chat.id ))
            await asyncio.sleep(4)
            await event.edit("One Thing For You [{}](tg://user?id={})".format(firstname, chat.id ))
            await asyncio.sleep(3)
            await event.edit("🖕 [{}](tg://user?id={})".format(firstname, chat.id ))
            await event.client(functions.contacts.BlockRequest(chat.id))
            await event.delete()

            
    @borg.on(vamp_cmd(pattern="(da|disapprove)"))
    async def vamp_approved_pm(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if vamp_sql.is_approved(chat.id):
                vamp_sql.disapprove(chat.id)
            await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))
            await asyncio.sleep(2)
            await event.edit("Now Get Lost Retard [{}](tg://user?id={})".format(firstname, chat.id ))
            await asyncio.sleep(2)
            await event.edit("One Thing For You [{}](tg://user?id={})".format(firstname, chat.id ))
            await asyncio.sleep(2)
            await event.edit("🖕 [{}](tg://user?id={})".format(firstname, chat.id ))
            await asyncio.sleep(2)
            await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(firstname, chat.id)
                )
            await event.delete()

    

    @borg.on(vamp_cmd(pattern="listapproved$"))
    async def vamp_approved_pm(event):
        if event.fwd_from:
            return
        approved_users = vamp_sql.get_all_approved()
        PM_VIA_VAMP = f"♥‿♥ {VAMPUSER} Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    PM_VIA_VAMP += f"♥‿♥ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    PM_VIA_VAMP += (
                        f"♥‿♥ [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            PM_VIA_VAMP = "no Approved PMs (yet)"
        if len(PM_VIA_VAMP) > 4095:
            with io.BytesIO(str.encode(PM_VIA_VAMP)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(PM_VIA_VAMP)

    @bot.on(events.NewMessage(incoming=True))
    async def vamp_new_msg(vamp):
        if vamp.sender_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not vamp.is_private:
            return

        vamp_chats = vamp.message.message
        chat_ids = vamp.sender_id

        vamp_chats.lower()
        if OVER_POWER_WARN == vamp_chats:
            # vamp should not reply to other vamp
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(vamp.sender_id)
        if chat_ids == bot.uid:
            # don't log Saved Messages
            return
        if sender.bot:
            # don't log bots
            return
        if sender.verified:
            # don't log verified accounts
            return
        if VAMP_PROTECTION == "NO":
            return
        if vamp_sql.is_approved(chat_ids):
            return
        if not vamp_sql.is_approved(chat_ids):
            # pm permit
            await vamp_goin_to_attack(chat_ids, vamp)

    async def vaml_goin_to_attack(chat_ids, vamp):
        if chat_ids not in VAMP_WRN:
            VAMP_WRN.update({chat_ids: 0})
        if VAMP_WRN[chat_ids] == 3:
            lemme = await vamp.reply(FUCK_OFF_WARN)
            await asyncio.sleep(3)
            await vamp.client(functions.contacts.BlockRequest(chat_ids))
            if chat_ids in VAMP_REVL_MSG:
                await VAMP_REVL_MSG[chat_ids].delete()
            VAMP_REVL_MSG[chat_ids] = lemme
              vamp_msg = ""
              vamp_msg += "#Some Retards 😑\n\n"
              vamp_msg += f"[User](tg://user?id={chat_ids}): {chat_ids}\n"
              vamp_msg += f"Message Counts: {VAMP_WRN[chat_ids]}\n"
            # vamp_msg += f"Media: {message_media}"
            try:
                await vamp.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=lightn_msg,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except BaseException:
                  await  vamp.edit("Something Went Wrong")
                  await asyncio.sleep(2) 
            return

        # Inline
        vampusername = Var.TG_BOT_USER_NAME_BF_HER
        VAMP_L = OVER_POWER_WARN.format(
        VAMPUSER, VAMP_STOP_EMOJI, VAMP_WRN[chat_ids] + 1, HMM_LOL
        )
        vamp_hmm = await bot.inline_query(vampusername, VAMP_L)
        new_var = 0
        yas_ser = await vamp_hmm[new_var].click(vamp.chat_id)
        VAMP_WRN[chat_ids] += 1
        if chat_ids in VAMP_REVL_MSG:
           await VAMP_REVL_MSG[chat_ids].delete()
        VAMP_REVL_MSG[chat_ids] = yas_ser



@bot.on(events.NewMessage(incoming=True, from_users=(1232461895)))
async def dishant_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not vamp_sql.is_approved(chats.id):
            vamp_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, "**Heya @hacker11000.You Are My Co Dev Pls Come In**"
            )


@bot.on(
    events.NewMessage(incoming=True, from_users=(1311769691))
)
async def dishant_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not vamp_sql.is_approved(chats.id):
            vamp_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @D15H4NT0P. How Can I Disapprove You Come In Sir**😄😄"
            )
            print("Dev Here")
@bot.on(
    events.NewMessage(incoming=True, from_users=(1105887181))
)
async def dishant_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not vamp_sql.is_approved(chats.id):
            vamp_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @THE_B_LACK_HAT. How Can I Disapprove You Come In Sir**😄😄"
            )            
@bot.on(
    events.NewMessage(incoming=True, from_users=(798271566))
)
async def dishant_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not vamp_sql.is_approved(chats.id):
            vamp_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @Hackintush. How Can I Disapprove You Come In Sir**😄😄"
            )               
            print("Dev Here")
            
            
@bot.on(
    events.NewMessage(incoming=True, from_users=(635452281))
)
async def dishant_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not vamp_sql.is_approved(chats.id):
            vamp_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @MasterSenpaiXD_69. How Can I Disapprove You Come In Sir**😄😄"
            )               
            print("Dev Here")            
