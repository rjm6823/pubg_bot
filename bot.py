import discord
import asyncio
import rss
import format_message

client = discord.Client()


def is_not_pinned(message):
    return not message.pinned


async def check():
    """
    Checks for new updates every 8 hours and when the bot starts
    :return: N/A
    """
    while True:
        if rss.check_new():
            item = rss.most_recent()
            message = format_message.format_notes(item)
            await client.send_message(client.get_channel("350634825516056577"), message)
        await asyncio.sleep(28800)  # Check every 8 hours


@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + " - " + client.user.id)
    print('------')
    await check()


@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('!ping'):
        await client.send_message(channel, 'Pong!')
    elif message.content.startswith('!clear'):
        await client.purge_from(channel, check=is_not_pinned)
    elif message.content.startswith('!recent'):
        item = rss.most_recent()
        message = format_message.format_notes(item)
        await client.send_message(channel, message)


client.run('MzUwNjM0MDYzMzIyODA4MzIw.DIIAPw.vKYUeqpckkZp7O2KB-mvCshsqv8')
