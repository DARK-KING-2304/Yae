#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6223743220:AAHtxvOnwjJYi_sxpPYEQGx7K0Ofz2lokEM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16102521"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3b87f55691dbc7eea5768cc3a8498895")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001863828346"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5109376623"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://asta:asta123@cluster0.ir8xzna.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001853425881"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_IMG = os.environ.get("START_IMAGE", "https://graph.org//file/e54e0fad1b478e43c84a4.jpg") 

#start message
START_MSG = os.environ.get("START_MESSAGE", "• 𝗞𝗼𝗻𝗻𝗶𝗰𝗵𝗶𝘄𝗮 {first} 💫\n\n• 𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗷𝗼𝗶𝗻 𝗼𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 [ 𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝗷𝗼𝗶𝗻 ] 𝘁𝗵𝗲𝗻\n\n• 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗯𝘆 𝘁𝗮𝗽𝗽𝗶𝗻𝗴 𝗼𝗻 📥 𝗥𝗲𝗹𝗼𝗮𝗱 📥 𝗞𝗲𝗲𝗽 𝗦𝘂𝗽𝗽𝗼𝗿𝘁𝗶𝗻𝗴 😊\n\n</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5850249548 1730665149").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "• 𝗞𝗼𝗻𝗻𝗶𝗰𝗵𝗶𝘄𝗮 {first} 💫\n\n• 𝗬𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗷𝗼𝗶𝗻 𝗼𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 [ 𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝗷𝗼𝗶𝗻 ] 𝘁𝗵𝗲𝗻\n\n• 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗯𝘆 𝘁𝗮𝗽𝗽𝗶𝗻𝗴 𝗼𝗻 📥 𝗥𝗲𝗹𝗼𝗮𝗱 📥 𝗞𝗲𝗲𝗽 𝗦𝘂𝗽𝗽𝗼𝗿𝘁𝗶𝗻𝗴 😊\n\n</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1243568995)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
