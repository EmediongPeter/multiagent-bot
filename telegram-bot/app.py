from email.mime import message
import logging
from urllib import response
from openai import OpenAI
import sys
import asyncio
from os import getenv, environ
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters import Command

from google import genai
from google.genai import types as genai_types

# client = OpenAI(
#     # This is the default and can be omitted
#     api_key= environ.get("OPENAI_API_KEY"),
# )
load_dotenv()
TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = getenv("GEMINI_API_KEY")

# gemini-2.0-flash gemini-1.5-flash gemini-2.5-flash
GEMINI_MODEL_NAME = "gemini-2.0-flash-001"

client = genai.Client(api_key=GEMINI_API_KEY)


class ChatMemory:
    def __init__(self, max_len=6):
        self.history = []  # list of {"role": ..., "content": ...}
        self.max_len = max_len

    def add(self, role: str, content: str):
        self.history.append({"role": role, "content": content})
        # trim to keep only last max_len rounds (each round = user + assistant)
        if len(self.history) > self.max_len * 2:
            self.history = self.history[- (self.max_len * 2):]

    def clear(self):
        self.history = []


memory = ChatMemory()

model_name = "gpt-3.5-turbo"

dispatcher = Dispatcher()


@dispatcher.message(Command('clear'))
async def clear(message: Message):
    """A handler to clear the previous conversations and context"""

    memory.clear()
    await message.answer("🗑️ Chat history cleared.")


@dispatcher.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.from_user is not None:
        await message.answer(f"Hello! I'm a bot created with aiogram.\n\n It's nice meeting you {html.bold(message.from_user.first_name)}!")


@dispatcher.message()
async def chat_with_assistant(message: Message):
    """A handler to process the user's inputs and produce an agentic workflow or generative one if it's a simple questions"""

    if message.text is None:
        return
    user_msg = message.text.strip()

    memory.add("user", user_msg)
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL_NAME,
            contents=[
                *[
                    genai_types.Content(role=msg["role"], parts=[
                        genai_types.Part.from_text(text=msg["content"])])
                    for msg in memory.history
                ]
            ],
            config=genai_types.GenerateContentConfig(
                system_instruction="You are a helpful telegram bot assistant that helps the user to accomplish tasks. If the user asks you a question, provide a concise and accurate answer. And BE AS CONCISE AS POSSIBLE",
                max_output_tokens=256,
            )
        )
    # response = client.chat.completions.create(
    #         model=model_name,
    #         messages=[
    #             {"role": "assistant", "content": memory_context.reference},
    #             {"role": "user", "content": message.text}
    #         ]
    #     )

        print("Response received from Gemini API:")
        print(response.text)

        if response.text is not None:
            ai_text = response.text.strip()
            memory.add("user", ai_text)
            await message.answer(ai_text)

    except Exception as e:
        logging.error("Error when calling Gemini API: %s", e)
        await message.answer("⚠️ Sorry, I couldn’t process that right now.")


async def main() -> None:
    if TELEGRAM_BOT_TOKEN is None:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set.")

    bot = Bot(token=TELEGRAM_BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
