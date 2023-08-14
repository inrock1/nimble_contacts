import csv
import os
from contextlib import contextmanager

from app.core.database import SessionLocal, get_db
from app.models.contacts import ContactModel


def read_csv_file(filename):
    with open(filename, newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            yield row


def contact_exists(session, email):
    return session.query(ContactModel).filter_by(email=email).first() is not None


def insert_contacts_to_db(db):
    try:
        script_dir = os.path.dirname(__file__)
        csv_file_path = os.path.join(script_dir, "Nimble_Contacts.csv")
        for row in read_csv_file(csv_file_path):
            email = row["Email"]
            if not contact_exists(db, email):
                contact = ContactModel(
                    first_name=row["first name"],
                    last_name=row["last name"],
                    email=email,
                )
                db.add(contact)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e


def init_db_from_csv():
    with contextmanager(get_db)() as session:
        insert_contacts_to_db(session)


