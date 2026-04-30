"""Lavash Center Bot - Main entry point"""

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from config import BOT_TOKEN
from handlers import start_handler, menu_handler

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot instance
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Register handlers
@dp.message(Command('start'))
async def start_command(message: types.Message):
    await start_handler.start_command(message)

@dp.message(Command('help'))
async def help_command(message: types.Message):
    await start_handler.help_command(message)

@dp.message(Command('menu'))
async def menu_command(message: types.Message):
    await menu_handler.show_menu(message)

# TODO: More handlers

async def main():
    """Bot ishga tushish"""
    logger.info('🤖 Lavash Center Bot ishga tushdi!')
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())