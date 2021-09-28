from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.redis import RedisStorage

from settings import bot_settings, redis_settings
from core.database.db_connect import db


# storage = RedisStorage(redis_settings.HOST, port=redis_settings.port, db=5)

bot = Bot(bot_settings.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

async def bot_on_startup(dp):
	from app.set_bot_command import set_bot_command

	from app.User.UserHandler import UserHandler

	await set_bot_command(dp)

	await UserHandler.register_handlers(dp)

async def bot_on_shutdown(dp):
	db.close()

if __name__ == '__main__':
	executor.start_polling(dp, on_startup=bot_on_startup, on_shutdown=bot_on_shutdown)
