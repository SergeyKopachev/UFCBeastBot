from aiogram.types import Message, CallbackQuery

from core.Base.BaseHandler import BaseHandler

from app.User.UserKeyboard import UserKeyboard
from app.User.UserRedis import UserRedis

from app.app_texts import MESSAGES


class UserHandler(BaseHandler):

	def __init__(self):
		super().__init__()

		self.keyboard = UserKeyboard()
		self.redis = UserRedis()

	@classmethod
	async def register_handlers(cls, dp):
		handler = cls()

		dp.register_message_handler(handler.start, commands=['start'])
		dp.register_message_handler(handler.inline_start, commands=['inline_start'])
		

	async def start(self, msg: Message):
		key = await self.keyboard.back_kb()
		await msg.answer(MESSAGES['start'], reply_markup=key)

	async def inline_start(self, msg: Message):
		key = await self.keyboard.inline_back_kb()
		await msg.answer(MESSAGES['start'], reply_markup=key)
