from aiogram.types import InlineKeyboardButton, ReplyKeyboardRemove


class BaseKeyboard():

    async def remove_kb(self):
        return ReplyKeyboardRemove()

    async def _get_inline_btn(self, text, callback_data):
        return InlineKeyboardButton(text=text, callback_data=callback_data)
