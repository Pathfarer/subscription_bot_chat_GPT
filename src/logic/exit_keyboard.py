from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def exit_keyboard():
    button = [
        [KeyboardButton(text='Выйти в стартовое меню')]
    ]
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
