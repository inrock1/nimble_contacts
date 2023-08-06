import os
from dotenv import load_dotenv

load_dotenv()

NIMBLE_API_KEY = os.getenv("NIMBLE_API_KEY")
print("NIMBLE_API_KEY = ", NIMBLE_API_KEY)

DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL = ", DATABASE_URL)
