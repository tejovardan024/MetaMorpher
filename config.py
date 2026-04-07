#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "16995961")
API_HASH = os.environ.get("API_HASH", "8817a7d4293049593e60999359970ddd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8639333344:AAGO2Dl9Xrw2XIoc9WIWthH6h_TiDI-gUWQ")
ADMIN = int(os.environ.get("ADMIN", '7364106679'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "Anime_Encodes_Telugu")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "animeencodestelugusupport")
DATABASE_URI = os.environ.get("DATABASE_URI","mongodb+srv://nothingboy024:nothingboy024@cluster0.5hzyn3i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/bd91761f6e938e2e6d23a.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '7364106679'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8081"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002457918476)
