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


def get_test_url():
    user = os.getenv("TEST_POSTGRES_USER", "postgres")
    password = os.getenv("TEST_POSTGRES_PASSWORD", "")
    server = os.getenv("TEST_POSTGRES_SERVER", "db")
    db = os.getenv("TEST_POSTGRES_DB", "app")
    return f"postgresql://{user}:{password}@{server}/{db}"


TEST_DATABASE_URL = get_test_url()
