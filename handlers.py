from aiogram.types import Message

from config import admin_id
from main import bot, dp


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text='Bot started')


@dp.message_handler()
async def echo(message: Message):
    text = f'Hi! You wrote {message.text}'
    await message.reply(text=text)
