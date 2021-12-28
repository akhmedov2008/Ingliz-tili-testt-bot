import io

from aiogram import types
from aiogram.dispatcher.filters import Command
from data.config import ADMINS
from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!#$"),AdminFilter(),user_id=ADMINS)
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    #1-usul
    try:
        await message.chat.set_photo(photo=input_file)
    except:
        print("Xatolik")

@dp.message_handler(IsGroup(), Command("set_title", prefixes="!#$"), AdminFilter(),user_id=ADMINS)
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    #2-usul
    try:
        await bot.set_chat_title(message.chat.id, title=title)
    except:
        print("Xatolik")


@dp.message_handler(IsGroup(), Command("set_description", prefixes="!#$"), AdminFilter(),user_id=ADMINS)
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    # 1-usul
    # await bot.set_chat_description(message.chat.id, description=description)
    # 2-usul
    try:
        await message.chat.set_description(description=description)
    except:
        print("Xatolik")