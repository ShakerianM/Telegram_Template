from telebot import types
import emoji

def create_keyboard(*keys, row_width=2, resize_keyboard=True):
    """
    Create a keyboard with the given keys.
    :param keys: list of strings
    :param row_width: int
    :param resize_keyboard: bool
    :return: types.ReplyKeyboardMarkup
    """
    keyboard = types.ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=resize_keyboard)
    #for key in keys:
     #   keyboard.add(types.KeyboardButton(key))
    keys = map(emoji.emojize, keys)
    buttons = map(types.KeyboardButton, keys)
    keyboard.add(*buttons)
    return keyboard
