from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.repositories.contact_repository import ContactRepository
from app.models.contacts import ContactModel
from app.services.contact_service import ContactService
from app.serializers.contact_serializer import ContactSchema
from tests.conftest import test_db


def test_create_contact(test_db: Session):
    contact_repo = ContactRepository(test_db)

    new_contact = ContactSchema(
        id_nimble="some_id",
        first_name="John",
        last_name="Doe",
        email="john@example.com"
    )

    created_contact = contact_repo.create_contact(new_contact)
    print("=====================created_contact", created_contact)
    print("=====================type created_contact", type(created_contact))

    assert created_contact.id_nimble == "some_id"
    assert created_contact.first_name == "John"
    assert created_contact.last_name == "Doe"
    assert created_contact.email == "john@example.com"


def test_update_contact(test_db: Session):
    contact_repo = ContactRepository(test_db)

    updated_contact = ContactSchema(
        id_nimble="some_id",
        first_name="Updated John",
        last_name="Updated Doe",
        email="updated_john@example.com"
    )

    updated_contact = contact_repo.update_contact(updated_contact)
    assert updated_contact.first_name == "Updated John"
    assert updated_contact.last_name == "Updated Doe"
    assert updated_contact.email == "updated_john@example.com"


def test_get_contact_by_id(test_db: Session):
    contact_repo = ContactRepository(test_db)

    retrieved_contact = contact_repo.get_contact_by_id("some_id")
    assert retrieved_contact is not None
    assert retrieved_contact.first_name == "Updated John"
    assert retrieved_contact.last_name == "Updated Doe"
    assert retrieved_contact.email == "updated_john@example.com"


def test_duplicate_id_nimble(test_db: Session):
    contact_repo = ContactRepository(test_db)

    duplicate_contact = ContactSchema(
        id_nimble="some_id",
        first_name="Duplicate John",
        last_name="Duplicate Doe",
        email="duplicate_john@example.com"
    )

    try:
        contact_repo.create_contact(duplicate_contact)
        assert False, "Expected IntegrityError"
    except IntegrityError:
        test_db.rollback()
        assert True


def test_nonexistent_contact(test_db: Session):
    contact_repo = ContactRepository(test_db)

    retrieved_contact = contact_repo.get_contact_by_id("nonexistent_id")
    assert retrieved_contact is None