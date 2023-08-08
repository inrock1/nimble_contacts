from sqlalchemy.orm import Session

from app.database import ContactModel, SessionLocal


class ContactDAL:
    def __init__(self):
        self.db = SessionLocal()

    def create_contact(self, id: str, first_name: str, last_name: str, email: str):
        contact = ContactModel(id=id, first_name=first_name, last_name=last_name, email=email)
        self.db.add(contact)
        self.db.commit()
        self.db.refresh(contact)
        return contact

    def update_contact(self, contact: ContactModel, first_name: str, last_name: str, email: str):
        contact.first_name = first_name
        contact.last_name = last_name
        contact.email = email
        self.db.commit()
        self.db.refresh(contact)
        return contact

    def get_contact_by_id(self, contact_id: str):
        return self.db.query(ContactModel).filter_by(id=contact_id).first()

    def close(self):
        self.db.close()
