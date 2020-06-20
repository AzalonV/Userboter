from pyrogram import Filters, Message

from userbot import UserBot
from userbot.plugins.help import add_command_help


@UserBot.on_message(Filters.command('s', '.') & Filters.me)
async def to_saved(_, message: Message):
    await message.delete()
    await message.reply_to_message.forward('self')


# Command help section
add_command_help(
    'save', [
        ['s', 'Reply to any message and instantly send it to your saved messages.'],
    ]
)
