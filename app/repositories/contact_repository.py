# file app/repositories/contact_repository.py
from app.models.contacts import ContactModel
from app.repositories.base import BaseRepository


class PersonRepository(BaseRepository):
    model = ContactModel


# end of file app/repositories/contact_repository.py
