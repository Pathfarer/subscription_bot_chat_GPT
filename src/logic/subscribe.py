import calendar
from datetime import datetime, timedelta

from src.database import User


def subscribe(user_id):
    user = User.get(id=user_id)
    now = datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    user.subscription_until = now + timedelta(days=days_in_month)
    user.save()
