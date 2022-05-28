from os import getenv
import logging
from consts import *
from user import *
from utils import MyStates
from keyboards import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="test")
async def test(message: types.Message):
    await message.answer("test!!!")

@dp.message_handler(commands="flag_for")
async def flag_for(message: types.Message):
    argument = message.get_args()
    path = f"images/{argument.lower()}.png"
    try:
        await bot.send_photo(message.from_user.id, open(path, "rb"))
    except FileNotFoundError:
        await message.answer("Такой страны я не знаю.")

@dp.message_handler(commands="one_question")
async def one_question(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(MyStates.WAITING_NUMBER[0])


# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!", reply_markup=greet_kb)

#
# @dp.message_handler(commands="cat")
# async def cat(message: types.Message):
#     path = "images/" + images['cat']
#     await bot.send_photo(message.from_user.id, open(path, "rb"))
#
# @dp.message_handler(commands="dog")
# async def dog(message: types.Message):
#
#     url = "https://avatars.mds.yandex.net/get-altay/2056672/2a0000016e40a5d1a1a6b2f40f7683e6d03d/XXL"
#     await bot.send_photo(message.from_user.id, url)
#
# @dp.message_handler(commands="giraffe")
# async def giraffe(message: types.Message):
#     path = "images/" + images['giraffe']
#     await bot.send_photo(message.from_user.id, open(path, "rb"))
#
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)