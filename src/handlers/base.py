from aiogram import F

from aiogram.filters import Command, state
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from loguru import logger

from src.loader import dp
from src.filters import IsSubscribed


@dp.message(F.text == 'Выйти в стартовое меню', IsSubscribed())
async def exit(message: Message, state):
    logger.info(f"User {message.from_user.id}/{message.from_user.username} exit to start menu")
    await state.clear()
    await bot_start_subscribed(message)


@dp.message(Command('start'), IsSubscribed())
async def bot_start_subscribed(message: Message):
    logger.info(f"User {message.from_user.id}/{message.from_user.username} started bot")
    buttons = [
        [InlineKeyboardButton(text='Пообщаться', callback_data='chat_GPT')],
        [InlineKeyboardButton(text='Сгенерировать картинку', callback_data='pic_generation')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer('Привет!\nЯ бот, при помощи которого можно использовать возможности чата GPT:', reply_markup=markup)


@dp.message(Command('start'), ~IsSubscribed())
async def bot_start_unsubscribed(message: Message):
    logger.info(f"User {message.from_user.id}/{message.from_user.username} started bot")

    buttons = [
        [InlineKeyboardButton(text='Подписаться', callback_data='subscribe')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer(
        'Привет!\nЯ бот, при помощи которого ты можешь использовать возможности чата GPT.\nЧтобы начать мной пользоваться, необходимо оплатить подписку.',
        reply_markup=markup)
