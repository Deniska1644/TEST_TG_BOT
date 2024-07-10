import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOCKEN")
YANDEX_MAP_KEY = os.environ.get("YANDEX_MAP_KEY")
YOU_MONEY_TOCKEN = os.environ.get("YOU_MONEY_TOCKEN")
GOOGLE_TABLE_LINK = os.environ.get('GOOGLE_TABLE_LINK')
GOOGLE_FILE_NAME_JSON = os.environ.get('GOOGLE_FILE_NAME_JSON')