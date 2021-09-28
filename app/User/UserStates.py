from aiogram.dispatcher.filters.state import StatesGroup, State


class YourState(StatesGroup):
	waiting_data = State()
