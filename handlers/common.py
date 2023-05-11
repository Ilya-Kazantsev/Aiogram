from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message

from keyboards.main import main_keyboard

router = Router()
"""
    Фильтры
    Command() - фильтр команд (команда в ТГ предваряется '/')
    
"""


@router.message(Command(commands=['start']))
async def start_bot(message: Message):
    await message.answer(text='Добро пожаловать!', reply_markup=main_keyboard)


@router.message(Text(contains='О боте'))
async def about(message: Message):
    await message.answer('Данный бот способен записывать ваши задачи, а также периодично напоминать о них с помощью пометок,'
                         'также у вас будет возможность посмотреть задачи на любой из дней')
