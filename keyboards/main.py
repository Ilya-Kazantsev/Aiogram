from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Добавить задачу"), KeyboardButton(text="Мои задачи")],
    [KeyboardButton(text="О боте")]
], resize_keyboard=True)
