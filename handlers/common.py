from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()
"""
    Фильтры
    Command() - фильтр команд (команда в ТГ предваряется '/')
    
"""


@router.message(Command(commands=["start"]))
async def start_bot(message: Message):
    await message.answer(text="Добро пожаловать!")
