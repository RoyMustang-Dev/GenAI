import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Configure Logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This is the handler that receives messages with '/start' or '/help' commands
    """
    await message.answer("Hello! I am Enigma.\nPowered by aiogram, developed by Aditya.\nType '/help' for a list of available commands.")

@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return EchoResponse
    """
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)