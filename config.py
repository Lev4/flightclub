import os
from dotenv import load_dotenv

load_dotenv()

TEQUILA_API_KEY = str(os.getenv("TEQUILA_API_KEY"))
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMIN_ID = int(os.getenv("ADMIN_ID"))
DATAFILE_PATH = os.path.join('FlightDeals.xlsx')



