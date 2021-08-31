# pmpermit for VAMPBOT.....

import asyncio
import io
import os
import time
import userbot.Config as Var

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

from userbot.plugins.sql_helper import pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, CUSTOM_PMPERMIT, VAMP_ID
from userbot.Config import Config
from VAMPBOT.utils import admin_cmd

PM_TRUE_FALSE = Config.PM_DATA

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
VAMPPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/9227ec6795ddc6e659236.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
d15h4nt0p = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "`Please wait for to response or you will be blocked and reported as spam!!`"
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Vamp User"
USER_BOT_WARN_ZERO = "**You were spamming my sweet master's inbox, henceforth you have been blocked by my master's PmPermit.**\n__Now GTFO, i'm busy__"
USER_BOT_NO_WARN = (
    "Hello, This is **Vãmpßøt Ultra Private Security Protocolâš ï¸**.\n"
)

if Var.PRIVATE_GROUP_ID is not None:

    @borg.on(admin_cmd(pattern="allow|.a ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit(
                    "Approved [{}](tg://user?id={}) to PM you.".format(
                        firstname, chat.id
                    )
                )
                await asyncio.sleep(3)
                await event.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit('`Reply To User To Approve Him !`')
                return
            if not pmpermit_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pmpermit_sql.approve(reply_s.sender_id, "Approved")
                await event.edit(
                        "Approved [{}](tg://user?id={}) to pm.".format(firstname, reply_s.sender_id)
                    )
                await asyncio.sleep(3)
                await event.delete()
            elif pmpermit_sql.is_approved(reply_s.sender_id):
                await event.edit('`User Already Approved !`')
                await event.delete()

                

    # Approve outgoing
    @bot.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if not chat.id in PM_WARNS:
                    pmpermit_sql.approve(chat.id, "outgoing")
                    bruh = "__Auto-approved bcuz outgoing ðŸš¶__"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()

    @borg.on(admin_cmd(pattern="block ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1212368262:
                await event.edit(
                    "You tried to block my masterðŸ˜¡. GoodBye for 100 seconds!ðŸ¥±ðŸ˜´ðŸ˜ªðŸ’¤"
                )
                time.sleep(100)
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        "Get lost retard.\nBlocked [{}](tg://user?id={})".format(
                            firstname, chat.id
                        )
                    )
                    await asyncio.sleep(3)
                    await event.client(functions.contacts.BlockRequest(chat.id))
        elif event.is_group:
            if chat.id == 1212368262:
                await event.edit(
                    "You tried to block my masterðŸ˜¡. GoodBye for 100 seconds!ðŸ¥±ðŸ˜´ðŸ˜ªðŸ’¤"
                )
                time.sleep(100)
            else:
                reply_s = await event.get_reply_message()
                if not reply_s:
                    await event.edit('`Reply To User To Block Him !`')
                    return
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                if pmpermit_sql.is_approved(event.chat_id):
                    pmpermit_sql.disapprove(event.chat_id)
                await event.edit("Blocked [{}](tg://user?id={})".format(firstname, reply_s.sender_id))
                await event.client(functions.contacts.BlockRequest(reply_s.sender_id))
                await asyncio.sleep(3)
                await event.delete()

    @borg.on(admin_cmd(pattern="disallow|.da ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1212368262:
                await event.edit("Sorry, I Can't Disapprove My Master")
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        "[{}](tg://user?id={}) disapproved to PM.".format(
                            firstname, chat.id
                        )
                    )
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit('`Reply To User To DisApprove`')
                return
            if pmpermit_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pmpermit_sql.disapprove(reply_s.sender_id)
                await event.edit(
                    "Disapproved [{}](tg://user?id={}) to PM.".format(firstname, reply_s.sender_id)
                )
                await asyncio.sleep(3)
                await event.delete()
            elif not pmpermit_sql.is_approved(reply_s.sender_id):
                await event.edit('`User Not Approved Yet`')
                await event.delete()    
                

    @borg.on(admin_cmd(pattern="listallowed|.la"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Currently Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"ðŸ‘‰ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"ðŸ‘‰ [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "No Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="[MafiaBot]Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.sender_id == bot.uid:
            return
