import csv
from app.database import SessionLocal, ContactModel, create_tables


create_tables()
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

# insert_contacts_to_db()
