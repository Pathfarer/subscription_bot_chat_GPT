from loguru import logger

from src.loader import dp, bot

__import__("src.handlers")

if __name__ == '__main__':
    logger.debug("Starting bot...")
    dp.run_polling(bot, skip_updates=True)
