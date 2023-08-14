# file app/repositories/base.py
from typing import Any, Dict, List

from sqlalchemy.orm import Session

from app.models.contacts import ContactModel
from app.serializers.contact_serializer import ContactSchema


class BaseRepository:
    model: Any = None

    def __init__(self, db: Session):
        self.db = db

    def create_contact(self, data: Dict[str, Any]):
        contact = self.model(**data)
        self.db.add(contact)
        self.db.commit()
        return contact

    def update_contact(self, data: dict):
        contact = self.get_contact_by_id(data["id_nimble"])
        if contact:
            for key, value in data.items():
                setattr(contact, key, value)
            self.db.commit()
            return contact
        return None

    def get_contact_by_id(self, id_nimble: str):
        return (
            self.db.query(self.model).filter(self.model.id_nimble == id_nimble).first()
        )

    def search_contacts(self, query: str) -> List[ContactModel]:
        search_query = f"%{query}%"
        contacts = (
            self.db.query(ContactModel)
            .filter(
                (ContactModel.first_name.ilike(search_query))
                | (ContactModel.last_name.ilike(search_query))
                | (ContactModel.email.ilike(search_query))
            )
            .all()
        )
        return contacts

    def close(self):
        self.db.close()


# end of file app/repositories/base.py
