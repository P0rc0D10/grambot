from random import choice
from userbot import bot
from telethon import TelegramClient, events

@bot.on(events.NewMessage(pattern='\.die'))
async def insult(event):
    pattern_string = event.pattern_match.string
    entity = pattern_string[pattern_string.find("(")+1:pattern_string.find(")")]
    file = open("./plugins/data/insults").read().split("\n")
    insult = choice(file)
    await event.respond(insult, reply_to=event.reply_to_msg_id)