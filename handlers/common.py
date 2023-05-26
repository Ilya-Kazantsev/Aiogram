from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram3_calendar import simple_cal_callback, SimpleCalendar

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
    await message.answer('Введите дату исполнения', reply_markup=await SimpleCalendar().start_calendar())
    await state.set_state(TaskState.deadline)


@router.callback_query(simple_cal_callback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await state.update_data(deadline=date.strftime("%d/%m/%Y"))
        data = await state.get_data()
        await callback_query.message.answer(f"{data['name']}\n{data['description']}\n{data['deadline']}")
