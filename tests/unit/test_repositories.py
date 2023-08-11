from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.repositories.contact_repository import PersonRepository
from app.serializers.contact_serializer import ContactSchema
from tests.conftest import test_db, clear_contacts_table

NEW_CONTACT = ContactSchema(
    id_nimble="some_id",
    first_name="John",
    last_name="Doe",
    email="john@example.com"
)

def test_create_contact(test_db: Session):
    contact_repo = PersonRepository(test_db)
    created_contact = contact_repo.create_contact(NEW_CONTACT.dict())

    assert created_contact.id_nimble == "some_id"
    assert created_contact.first_name == "John"
    assert created_contact.last_name == "Doe"
    assert created_contact.email == "john@example.com"


def test_update_contact(test_db: Session):
    contact_repo = PersonRepository(test_db)
    contact_repo.create_contact(NEW_CONTACT.dict())
    updated_contact = ContactSchema(
        id_nimble="some_id",
        first_name="Updated John",
        last_name="Updated Doe",
        email="updated_john@example.com"
    )

    updated_contact = contact_repo.update_contact(updated_contact.dict())
    assert updated_contact.first_name == "Updated John"
    assert updated_contact.last_name == "Updated Doe"
    assert updated_contact.email == "updated_john@example.com"


def test_get_contact_by_id(test_db: Session):
    contact_repo = PersonRepository(test_db)
    contact_repo.create_contact(NEW_CONTACT.dict())
    retrieved_contact = contact_repo.get_contact_by_id("some_id")

    assert retrieved_contact is not None
    assert retrieved_contact.first_name == "John"
    assert retrieved_contact.last_name == "Doe"
    assert retrieved_contact.email == "john@example.com"


def test_duplicate_id_nimble(test_db: Session):
    contact_repo = PersonRepository(test_db)
    contact_repo.create_contact(NEW_CONTACT.dict())

    try:
        contact_repo.create_contact(NEW_CONTACT.dict())
        assert False, "Expected IntegrityError"
    except IntegrityError:
        test_db.rollback()
        assert True


def test_nonexistent_contact(test_db: Session):
    contact_repo = PersonRepository(test_db)

    retrieved_contact = contact_repo.get_contact_by_id("nonexistent_id")
    assert retrieved_contact is None


