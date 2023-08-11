# file tests/integration/test_database.py
from app.services.contact_service import ContactService
from app.repositories.contact_repository import PersonRepository
from tests.conftest import test_db, mock_requests
from tests.conftest import MOCK_RESPONSE


def test_fetch_nimble_contacts_mocked_api(mock_requests, test_db):
    mock_requests.get("https://api.nimble.com/api/v1/contacts", json=MOCK_RESPONSE)

    with test_db as session:
        contact_repo = PersonRepository(session)
        service = ContactService(contact_repo)
        service.check()

    db_contact = contact_repo.get_contact_by_id("64ca0fa4d1d39db980b9d42c")
    assert db_contact is not None
    assert db_contact.first_name == "Jon1"
    assert db_contact.last_name == "Ferrara"
    assert db_contact.email == "care@nimble.com"


# end of file tests/integration/test_database.py