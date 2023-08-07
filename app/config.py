# contacts/app/config.py
import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
NIMBLE_API_KEY = os.getenv("NIMBLE_API_KEY")

# end of file contacts/app/config.py
