from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

from core.Base.BaseKeyboard import BaseKeyboard

from app.app_texts import KEYBOARD


class UserKeyboard(BaseKeyboard):
	back_cd: CallbackData

	def __init__(self):
		super().__init__()

		self.back_cd = CallbackData('back_cd', 'callback_data')

	async def back_kb(self):
		key = ReplyKeyboardMarkup(resize_keyboard=True)

		key.insert(await self.__get_back_btn())

		return key

	async def inline_back_kb(self):
		key = InlineKeyboardMarkup()

		key.insert(await self.__get_inline_back_btn())

		return key

	# Логика отдельных кнопок
	async def __get_back_btn(self):
		text = KEYBOARD['back']
		btn = KeyboardButton(text=text)
		return btn

	async def __get_inline_back_btn(self):
		text = KEYBOARD['back']
		cd = self.back_cd.new(callback_data='callback_data')
		return await self._get_inline_btn(text, cd)
	# ----------------------------------------------------------------
