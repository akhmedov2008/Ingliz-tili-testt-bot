from aiogram import types
from filters import IsPrivate, IsGroup
from loader import dp
import wikipedia


wikipedia.set_lang('uz')

# Wiki bot
@dp.message_handler(IsPrivate())
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

@dp.message_handler(IsGroup())
async def sendSalom(message: types.Message):
    respond = message.from_user.text
    if respond in ['Salom','Qalesiz','Tuzimisilar']:
        await message.answer("Assalomu aleykum nima qilyapsiz, Tuzimisiz")
