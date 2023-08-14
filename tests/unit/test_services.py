from app.services.nimble_service import NimbleService
from tests.conftest import MOCK_RESPONSE


def test_get_nimble_contacts(mock_requests):
    mock_requests.get("https://api.nimble.com/api/v1/contacts", json=MOCK_RESPONSE)

    nimble_service = NimbleService(api_key="")
    contacts = nimble_service.get_contacts()

    assert len(contacts) == 1
    assert contacts[0].first_name == "Jon1"
    assert contacts[0].last_name == "Ferrara"
    assert contacts[0].email == "care@nimble.com"
