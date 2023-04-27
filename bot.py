import asyncio

from aiogram import Dispatcher, Bot

import config


async def main():
    dp = Dispatcher()
    bot = Bot(config.TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
