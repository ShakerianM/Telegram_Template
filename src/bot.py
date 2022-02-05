import telebot
import os
from loguru import logger
from src.utils.io import write_json
from src.constants import keyboards,create_keyboard

class Bot:
	"""
	Telegram bot to randomly connect two strangers.

	"""
	def	__init__(self) -> None:
		self.bot = telebot.TeleBot(os.environ['AnonBotToken'], parse_mode=None)
		self.echo_all = self.bot.message_handler(func=lambda m: True)(self.echo_all)
	def run(self) -> None:
		logger.info('Bot is running....')
		self.bot.infinity_polling()

	def echo_all(self, message) -> None:
		write_json(message.json, 'data/message.json')
		#for word in message.text.split():
		#self.bot.reply_to(message, message.text)
		self.bot.send_message(message.chat.id, message.text,reply_markup=keyboards.main)
		self.bot.send_message(message.chat.id, message.text,reply_markup=create_keyboard(message.from_user.id))
		logger.info(f'Message \'{message.text}\' received from {message.from_user.first_name} {message.from_user.last_name}')

if __name__ == '__main__':
	logger.info("Bot started")
	bot = Bot()
	bot.run()
