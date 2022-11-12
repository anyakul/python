import telebot
import logging
logger = telebot.logger

logger.basicConfig(filename='log.txt', level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s - %(message)s')
