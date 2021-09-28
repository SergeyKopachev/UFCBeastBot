from aiogram.types import BotCommand


async def set_bot_command(dp):
	await dp.bot.set_my_commands(
		[
			BotCommand('start', 'Start'),
			BotCommand('events', 'Events'),
			BotCommand('results', 'Results'),
			BotCommand('reminder', 'Reminder'),
			BotCommand('settings', 'Settings'),
			BotCommand('help', 'Help')
		]
	)
