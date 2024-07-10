import logging
import asyncio
import sys

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, types, Dispatcher
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from handlers import router



dp = Dispatcher()

async def main() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())