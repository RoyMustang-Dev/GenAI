import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import openai
import sys

# Step 1: Load the Keys and Tokens
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Step 2: Initialize the Class instance
class Reference:
    '''
    A class to store the previous response
    '''
    def __init__(self) -> None:
        self.reference = ""
        self.response = ""


reference = Reference()
model_name = "gpt-3.5-turbo"

# Step 3: Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

# Step 4: Define the function to handle the /start command
@dispatcher.message_handler(commands=['start'])
async def command_start_handler(message: types.Message):
    """
    This is the handler that receives messages with '/start'
    """
    await message.answer("Hello! I am Enigma.\nPowered by aiogram, developed by Aditya.\nHow can I help you?")

# Step 5: Define the function to handle the /help command
@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    This is the handler that receives messages with '/help'
    """
    help_command = """
        Hi there, I'm Enigma. I can help you with the following commands:\n/start - to start the conversation\n/clear - to clear the past conversations\n/help - to get this help menu
                """
    await message.reply(help_command)
    await message.answer("You can also ask me questions, provide references, or generate answers based on the provided context. Type /start to begin.")

# Step 6: Define the function to clear the previous responses and context

# Clear Previous Response
def clear_response():
    """
    A function to clear the previous response and context
    """
    reference.response = ""


@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    This is the handler that receives messages with '/clear'
    """
    clear_response()
    await message.reply("Previous responses and context have been cleared.")

# Step 7: Define the function to handle the Users inputs and generate responses
@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """
    This is the handler that processes the User's Input & Generate a response using the chatGPT API.
    """
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = model_name,
        messages = [
            {"role": "assistant", "content": reference.response},
            {"role": "user", "content": message.text}
        ]
    )
    reference.response = response.choices[0].message.content
    print(f"<<< Enigma: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)

# Step 8: Call the Executor
if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False)