# from environs import Env
#
# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
#
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
#
# CHANNELS = ["-1001798490099", "-1001691825311"]

import os

# .env faylini ichidan quyidegilRNI O'QIYMIZ
BOT_TOKEN = str(os.environ.get("BOT_TOKEN")) #BOT TOKEN
ADMINS = list(os.environ.get("ADMINS")) #ADMINLAR ROYHATI
# IP = str(os.environ.get("ip")) #Xosting ip manzil
IP = str("localhost")
CHANNELS = list(os.environ.get("CHANNELS"))
