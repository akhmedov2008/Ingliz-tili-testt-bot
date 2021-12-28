from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import *
from filters import IsPrivate, IsGroup

@dp.message_handler(IsPrivate(), Command('translator'))
async def Translator(message: types.Message):
    textt = ("So'zlarni tarjima qilish UCHUN Botlar :",
             "👉 @lang_translate_bot",
             "👉 @tarjimon_eng_bot")
    await message.reply("\n".join(textt))

@dp.message_handler(IsGroup(), Command('translator'))
async def Translator(message: types.Message):
    textt = ("Bu buyruqni bajarish uchun\n Iltimos <a href='https://t.me/ingliz_tili_testt_bot/'>Botga</a> o'ting:\n 👉 @ingliz_tili_testt_bot")
    await message.reply("\n".join(textt))