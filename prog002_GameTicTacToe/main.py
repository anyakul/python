import logging
from telegram.ext import filters, ApplicationBuilder, CommandHandler, MessageHandler
from model import *
from bot_commands import *


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    usr_handler = MessageHandler(
        filters.TEXT & (~filters.COMMAND), usr_msg_hdr)

    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(usr_handler)

    application.run_polling()
