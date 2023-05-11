from aiogram.fsm.state import StatesGroup, State


class TaskState(StatesGroup):
    name = State()
    description = State()
    deadline = State()
