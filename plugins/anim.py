from userbot import bot
from telethon import TelegramClient, events
from time import sleep

@bot.on(events.NewMessage(pattern='\.anim()'))
async def anim(event):
    pattern_string = event.pattern_match.string
    animes = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    lst = animes.split(",")
    before = lst[0].strip()
    after = lst[1].strip()
    try:
        reply_to_user = event.message.to_id.user_id
    except AttributeError:
        reply_to_user = event.message.to_id.channel_id
    sent = await bot.send_message(reply_to_user, message=after)
    for i in range(0, 6):
        await bot.edit_message(reply_to_user, sent.id, before)
        sleep(0.5)
        await bot.edit_message(reply_to_user, sent.id, after)
        sleep(0.5)