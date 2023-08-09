# file app/repositories/base.py
from typing import Any

from sqlalchemy.orm import Session

from app.serializers.contact_serializer import ContactSchema


class BaseRepository:
    model: Any = None

    def __init__(self, db: Session):
        self.db = db

    def create_contact(self, nimble_contact: ContactSchema):
        contact = self.model(
            id_nimble=nimble_contact.id_nimble,
            first_name=nimble_contact.first_name,
            last_name=nimble_contact.last_name,
            email=nimble_contact.email,
        )
        self.db.add(contact)
        self.db.commit()
        return contact

    def update_contact(self, nimble_contact: ContactSchema):
        contact = self.get_contact_by_id(nimble_contact.id_nimble)
        if contact:
            contact.first_name = nimble_contact.first_name
            contact.last_name = nimble_contact.last_name
            contact.email = nimble_contact.email
            self.db.commit()
            return contact
        return None

    def get_contact_by_id(self, id_nimble: str):
        return (
            self.db.query(self.model).filter(self.model.id_nimble == id_nimble).first()
        )

    def close(self):
        self.db.close()


# end of file app/repositories/base.py