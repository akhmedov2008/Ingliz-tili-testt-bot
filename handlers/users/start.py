import sqlite3
import logging
from filters import IsGroup, IsPrivate
from aiogram import types
from data.config import CHANNELS
from keyboards.inline.subscription import check_button
from loader import bot, dp
from utils.misc import subscription
from aiogram.dispatcher.filters.builtin import Command

@dp.message_handler(IsGroup(),Command('start'))
async def bot_start_group(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!, Siz guruhdasiz")
foydalanuvchi = []

@dp.message_handler(Command('Foydalanuvchilar'))
async def Foydalanuvchilar(message: types.Message):
    await message.reply(f"Foydalanuvchilar: {foydalanuvchi}")
@dp.message_handler(IsPrivate(), Command('start'))
async def show_channels(message: types.Message):
    # name = message.from_user.full_name
    # # Foydalanuvchini bazaga qo'shamiz
    # try:
    #     db.add_user(id=message.from_user.id,
    #                 name=name)
    # except sqlite3.IntegrityError as err:
    #     await bot.send_message(chat_id=ADMINS[0], text=err)

    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)
    # Adminga xabar beramiz
    # count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {message.from_user.first_name} ta foydalanuvchi kirdi."
    foydalanuvchi.append(message.from_user.id)
    await bot.send_message(chat_id=ADMINS[0], text=msg)


@dp.callback_query_handler(IsGroup(),text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz! ✅\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. ❌ "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)
