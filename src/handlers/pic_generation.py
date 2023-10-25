from aiogram import F

from loguru import logger

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, URLInputFile, InputMediaPhoto, ReplyKeyboardMarkup, KeyboardButton

from src.loader import dp
from src.filters import IsSubscribed
from src.logic import get_image_url, exit_keyboard


class PICgeneration(StatesGroup):
    generation = State()


@dp.callback_query(F.data == 'pic_generation', IsSubscribed())
async def start_pic_generation(callback_query, state: FSMContext):
    logger.info(f"User {callback_query.message.from_user.id}/{callback_query.message.from_user.username} generating images")
    await state.set_state(PICgeneration.generation)
    markup = exit_keyboard()
    await callback_query.message.answer('Напишите описание:', reply_markup=markup)


@dp.message(PICgeneration.generation, IsSubscribed())
async def pic_generation(message: Message):
    logger.info(
        f"User {message.from_user.id}/{message.from_user.username} generating images with following text:\n{message.text}")
    picture_urls = await get_image_url(message.text, number=4)

    media_group = []
    for picture_url in picture_urls:
        photo_file = URLInputFile(picture_url)
        input_photo = InputMediaPhoto(media=photo_file)
        media_group.append(input_photo)

    await message.answer_media_group(media=media_group)
