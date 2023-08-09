import os

from dotenv import load_dotenv

load_dotenv()


NIMBLE_API_KEY = os.getenv("NIMBLE_API_KEY")

def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "")
    server = os.getenv("POSTGRES_SERVER", "db")
    db = os.getenv("POSTGRES_DB", "app")
    return f"postgresql://{user}:{password}@{server}/{db}"

DATABASE_URL = get_url()

TEST_DATABASE_URL = "sqlite:///./test.db"

