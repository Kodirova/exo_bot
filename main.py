from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot=Bot(token=TOKEN)
dp=Dispatcher(bot)


if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)