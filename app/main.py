# contacts/app/main.py
import os

from fastapi import FastAPI
from app.api.contacts import router as contact_router
from app.database import SessionLocal, ContactModel, create_tables
import csv
from dotenv import load_dotenv

from app.helpers import update_database_from_nimble
from app.tasks import fetch_nimble_contacts

app = FastAPI()

app.include_router(contact_router, prefix="/api")

load_dotenv()
NIMBLE_API_KEY = os.getenv("NIMBLE_API_KEY")


@app.on_event("startup")
def startup():
    create_tables()
    # fetch_nimble_contacts.delay(NIMBLE_API_KEY)
    update_database_from_nimble(NIMBLE_API_KEY)


@app.get("/")
async def root():
    return {"message": "Root page"}

def read_csv_file(filename):
    with open(filename, newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            yield row

def insert_contacts_to_db():
    db = SessionLocal()
    try:
        for row in read_csv_file("Nimble_Contacts.csv"):
            contact = ContactModel(
                id=row["Email"],
                first_name=row["first name"],
                last_name=row["last name"],
                email=row["Email"]
            )
            db.add(contact)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Celery configuration
app.config_from_object("app.tasks.celery_config")

# insert_contacts_to_db()

# end of file contacts/app/main.py