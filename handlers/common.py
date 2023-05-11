from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.main import main_keyboard
from task_state import TaskState

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


@router.message(Text(contains='Добавить задачу'))
async def add_new_task(message: Message, state: FSMContext):
    await message.answer('Введите название задачи')
    await state.set_state(TaskState.name)


@router.message(TaskState.name)
async def get_task_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите описание задачи')
    await state.set_state(TaskState.description)


@router.message(TaskState.description)
async def get_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Введите дату исполнения')
    await state.set_state(TaskState.deadline)


@router.message(TaskState.deadline)
async def get_deadline(message: Message, state: FSMContext):
    await state.update_data(deadline=message.text)
    data = await state.get_data()
    await message.answer(f"{data['name']}\n{data['description']}\n{data['deadline']}")
