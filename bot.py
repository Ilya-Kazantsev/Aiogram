import asyncio
from aiogram import Dispatcher, Bot
from aiogram.fsm.strategy import FSMStrategy
from aiogram.types import BotCommand

import config
from handlers import common


async def main():
    dp = Dispatcher(fsm_strategy=FSMStrategy.CHAT)
    bot = Bot(config.TOKEN)
    # Подключение обработчиков чата
    dp.include_router(common.router)

    # Подключение стартового меню бота
    await bot.set_my_commands([BotCommand(command='start', description='Начало')])
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
