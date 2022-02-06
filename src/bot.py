import telebot
import os

bot = telebot.TeleBot(os.environ['BotToken'],parse_mode='HTML')