from loader import dp
from aiogram import types
from filters import IsGroup, IsPrivate

@dp.message_handler(commands=['admins','programmers'])
async def Adminc(message: types.Message):
    await message.answer(f"Assalomu aleykum {message.from_user.username}\n Siz Dasturchi va Adminlar haqida bilmoqchi bo'lsangiz\n\n Adminlar: @Mx_2589, @ahmedov_2008\n Dasturchi: Muhammadamin Ahmedov\n\n ")
    await message.reply(f"{message.from_user.first_name} {message.from_user.last_name}\n Bu bot Mysterious programmer tomonidan yaratilgan\n Dasturchining ismi: Muhammadamin\n Dasturchining Familiyasi: Ahmedov\n")

