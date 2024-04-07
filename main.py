import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from config import TOKEN
from app.handlers import rt
from app.admin import admin
from app.database.models import async_main

async def main():
    await async_main()
    
    bot = Bot(token = TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_routers(rt, admin)
    
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')