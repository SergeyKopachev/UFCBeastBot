from main import bot

from core.Base.BaseRedis import BaseRedis
from core.Base.BaseKeyboard import BaseKeyboard


class BaseHandler():
	bot = ''
	keyboard: BaseKeyboard
	redis: BaseRedis

	def __init__(self):
		self.bot = bot
		self.redis = BaseRedis()
		self.keyboard = BaseKeyboard()
