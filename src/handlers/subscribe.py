import calendar
from datetime import datetime, timedelta

from aiogram import F
from aiogram.types import PreCheckoutQuery, ShippingQuery, Message

from loguru import logger

from src.filters import IsSubscribed
from src.handlers import bot_start_subscribed
from src.loader import dp, bot, PAYMASTER_TOKEN
from src.database import User
from src.logic import subscribe


@dp.callback_query(F.data == 'subscribe', ~IsSubscribed())
async def check_feature_not_subbed(callback_query):
    logger.info(
        f"User {callback_query.from_user.id}/{callback_query.from_user.username} subscribing.")

    await bot.send_invoice(chat_id=callback_query.from_user.id,
                           title='Подписка на бота',
                           description='Подписка на бота',
                           payload='123',
                           provider_token=PAYMASTER_TOKEN,
                           currency='RUB',
                           prices=[{
                               'label': 'Подписка на бота',
                               'amount': 100_00
                           }]
                           )


@dp.shipping_query()
async def shipping(shipping_query: ShippingQuery):
    await bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=[])


@dp.pre_checkout_query()
async def pre_checkout(pre_checkout_query: PreCheckoutQuery):
    user_id = pre_checkout_query.from_user.id
    user_from_db = User.get(User.id == user_id)
    if user_from_db.subscription_until and user_from_db.subscription_until > datetime.now():
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=False, error_message=f'Подписка оформеленна до {user_from_db.subscription_until}')
        return

    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message(F.successful_payment)
async def successful_payment(message: Message):
    await message.answer('Спасибо за подписку!')
    subscribe(message.from_user.id)
    await bot_start_subscribed(message)
