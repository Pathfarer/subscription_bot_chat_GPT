from aiogram import F

from loguru import logger

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from src.loader import dp
from src.filters import IsSubscribed
from src.logic import ask_gpt, exit_keyboard


class GPTState(StatesGroup):
    chatting = State()


@dp.callback_query(F.data == 'chat_GPT', IsSubscribed())
async def start_chatting(callback_query, state: FSMContext):
    logger.info(
        f"User {callback_query.message.from_user.id}/{callback_query.message.from_user.username} chatting CPT")
    await state.set_state(GPTState.chatting)
    markup = exit_keyboard()
    await callback_query.message.answer('Напишите запрос чату GPT:', reply_markup=markup)


@dp.message(GPTState.chatting, IsSubscribed())
async def chatting(message: Message):
    logger.info(
        f"User {message.from_user.id}/{message.from_user.username} chatting with GPT with following text:\n{message.text}")
    answer = await ask_gpt(message.text)
    await message.answer(answer)
