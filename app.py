#!/usr/bin/env python3

"""

Anuhaz XRD WORM AI Telegram Bot

"""

import logging

from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from bot_handlers import BotHandlers

from config import BOT_TOKEN

logging.basicConfig(

    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

    level=logging.INFO

)

logger = logging.getLogger(__name__)

def main():

    logger.info("🚀 Starting Anuhaz XRD WORM AI Bot...")

    

    try:

        application = Application.builder().token(BOT_TOKEN).build()

        handlers = BotHandlers()

        

        application.add_handler(CommandHandler("start", handlers.start_command))

        application.add_handler(CommandHandler("menu", handlers.menu_command))

        application.add_handler(CommandHandler("clear", handlers.clear_command))

        application.add_handler(CommandHandler("help", handlers.help_command))

        application.add_handler(CallbackQueryHandler(handlers.button_callback))

        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_message))

        

        logger.info("✅ Bot starting...")

        application.run_polling()

        

    except Exception as e:

        logger.error(f"❌ Error: {e}")

        raise

if __name__ == '__main__':

    main()
