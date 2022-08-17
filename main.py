import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from config import token
from aiogram.dispatcher import FSMContext

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=token, parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    button = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    button.add(
        types.KeyboardButton(text="O'zbek"),
        types.KeyboardButton(text="Ruscha"),
        types.KeyboardButton(text="English"),
    )

    await message.answer(
        text=f"Xush kelibsiz{message.from_user.full_name}",
        reply_markup=button
    )
# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def choice_lang(message:types.Messae):
#     language = message.text.title()
#     if language == "O'zbek":
#         msg ="Siz o'zbek tilini tanladingiz"
#     elif language =="Rus tili":
#         msg ="Siz rus tilini tanladingiz"
#     elif language == "English":
#         msg = "you selected english"
#     await message.answer(
#         text=msg
#     )

# @dp.message_handler(commands=["help"])
# async def help_command(message: types.Message):
#     await message.answer(
#         text="Bizning botda hali kamandalar mavjud emas"
#     )


@dp.message_handler(commands=['click'])
async def cmd_start(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:  # proxy = FSMContextProxy(state); await proxy.load()
        proxy.setdefault('counter', 0)
        proxy['counter'] += 1
        return await message.reply(f"Counter: {proxy['counter']}")


@dp.message_handler(commands=["dice"])
async def get_dice(message: types.Message):
    await message.answer_dice(
        emoji="🎲"
    )
# @dp.message_handler(commands=["video"])
# async def get_video(message: types.Message):
#     await message.answer_video("https://www.youtube.com/watch?v=i5v0avsuAgI")



@dp.message_handler(commands=["photo"])
async def get_photo1(message: types.Message):
    await message.answer_photo("https://www.pocket-lint.com/laptops/reviews/apple/161591-apple-macbook-pro-m2-2022-review")

@dp.message_handler(commands=["video"])
async def get_photo1(message: types.Message):
    video = open("200w.webp", "rb")
    await message.answer_video(
        video
    )

# @dp.errors_handler(exception='BotBlocked')
# async def handle_error(update: types.Update, exception: Exception):
#     print("Bot blocked")
#     return True
#
#
# @dp.errors_handler(commands=["help"])
# async def help_error(message: types.Message):
#     await asyncio.sleep(20)
#     await message.answer(
#         text=f"how can i help you"
#     )

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)