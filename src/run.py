from loguru import logger

import emoji

from src.utils.io import write_json
from src.constants import keyboards,create_keyboard
from src.filters import IsAdmin
from src.bot import bot

class Bot:
    """
    Telegram bot to randomly connect two strangers.

    """
    def	__init__(self, bot) -> None:

        self.bot = bot

        self.bot.add_custom_filter(IsAdmin())

        self.handler()

        logger.info('Bot is running....')
        self.bot.infinity_polling()

        self.echo_all = (self.echo_all)

    def handler(self) -> None:

        @self.bot.message_handler(commands=['start'])
        def start(message) -> None:
            self.bot.reply_to(message, 'Hello!')

        @self.bot.message_handler(is_admin=True)
        def admin(message) -> None:
            self.send_message(message.chat.id, '<strong> You are An Admin!</strong>')

        @self.bot.message_handler(func=lambda m: True)
        def echo_all(message) -> None:
            #write_json(message.json, 'data/message.json')
            #for word in message.text.split():
            #self.bot.reply_to(message, message.text)
            self.send_message(
                message.chat.id, message.text,reply_markup=keyboards.main)
            #self.bot.send_message(message.chat.id, message.text,reply_markup=create_keyboard(message.from_user.id))
            logger.info(f'Message \'{message.text}\' received from {message.from_user.first_name}')

    def send_message(self, chat_id, text, reply_markup=None,emozies=False):

        if emozies:
            text = emoji.emojize(text, use_aliases=True)

        self.bot.send_message(chat_id, text, reply_markup=reply_markup)



if __name__ == '__main__':
    logger.info("Bot started")
    bot = Bot(bot)

