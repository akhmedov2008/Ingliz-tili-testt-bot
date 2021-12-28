from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("yangi_post", "Kanallarga reklama yoki post joylash"),
            types.BotCommand("translator", "Tarjimon"),
            # types.BotCommand("email", "Emailingizni bazaga qo'shish."),
        ]
    )
