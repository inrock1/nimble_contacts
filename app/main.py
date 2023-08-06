# contacts/app/main.py
import os

from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.search import router as contact_router
from app.celery_tasks.tasks import fetch_nimble_contacts


load_dotenv()
NIMBLE_API_KEY = os.getenv("NIMBLE_API_KEY")

app = FastAPI()
app.include_router(contact_router, prefix="/api")


@app.on_event("startup")
def startup():
    fetch_nimble_contacts.delay()
    # update_database_from_nimble(NIMBLE_API_KEY)


@app.get("/")
async def root():
    return {"message": "Root page"}


# end of file contacts/app/main.py
