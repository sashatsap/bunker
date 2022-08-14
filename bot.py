import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Configure logging
logging.basicConfig(
    format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.INFO,
    # filename="bunker.log",
)

dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start_function(message: types.Message):
    await message.answer('hello world')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
