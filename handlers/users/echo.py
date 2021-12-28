from aiogram import types
from filters import IsPrivate
from loader import dp
import wikipedia


wikipedia.set_lang('uz')

# Wiki bot
@dp.message_handler(IsPrivate())
async def sendWiki(message: types.Message):
    print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")