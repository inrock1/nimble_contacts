# contacts/app/main.py
import os

from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.contacts import router as contact_router

from app.tasks.tasks import fetch_nimble_contacts

app = FastAPI()
app.include_router(contact_router, prefix="/api")

load_dotenv()
NIMBLE_API_KEY = os.getenv("NIMBLE_API_KEY")


@app.on_event("startup")
def startup():
    fetch_nimble_contacts.delay(NIMBLE_API_KEY)
    # update_database_from_nimble(NIMBLE_API_KEY)


@app.get("/")
async def root():
    return {"message": "Root page"}


# end of file contacts/app/main.py