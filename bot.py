from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Hi! Write smth')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('I will answer if you write smth')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)