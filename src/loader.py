import os

import openai

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PAYMASTER_TOKEN = os.getenv("PAYMASTER_TOKEN")

if not BOT_TOKEN or not PAYMASTER_TOKEN:
    raise Exception("No token provided")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

GPT_TOKEN = os.getenv('GPT_TOKEN')
openai.api_key = GPT_TOKEN
