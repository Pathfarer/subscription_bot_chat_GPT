from peewee import *

db = SqliteDatabase('database.db')


class User(Model):
    username = CharField()
    subscription_until = DateTimeField(null=True)

    class Meta:
        database = db


db.connect()
db.create_tables([User])
