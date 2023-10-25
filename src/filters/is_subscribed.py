from datetime import datetime

from aiogram.types import Message
from aiogram.filters import Filter

from src.database import User


class IsSubscribed(Filter):
    async def __call__(self, message: Message, event_from_user: User):
        now = datetime.now()
        user = message.from_user

        user_from_db = User.get_or_create(id=user.id, username=user.username)[0]
        subscription_until = user_from_db.subscription_until

        return subscription_until > now if subscription_until else False
