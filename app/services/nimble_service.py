# contacts/app/services/nimble_service.py
import requests

from app.serializers.contact_serializer import ContactSchema


class NimbleService:
    def __init__(self, api_key: str, requests_session: requests.Session = None):
        self.api_key = api_key
        self.requests_session = requests_session or requests.Session()

    def get_json(self) -> list[dict]:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = self.requests_session.get(
            "https://api.nimble.com/api/v1/contacts", headers=headers
        )
        if response.status_code != 200:
            response.raise_for_status()
        return response.json().get("resources", [])

    def get_contacts(self) -> list[ContactSchema]:
        resources = self.get_json()
        contacts_schema = []
        person_contacts = [
            contact for contact in resources if contact.get("record_type") == "person"
        ]

        for contact_data in person_contacts:
            id_nimble = contact_data["id"]
            first_name = contact_data["fields"].get("first name", [{}])[0].get("value")
            last_name = contact_data["fields"].get("last name", [{}])[0].get("value")
            email = contact_data["fields"].get("email", [{}])[0].get("value")

            if first_name and last_name:
                contacts_schema.append(
                    ContactSchema(
                        id_nimble=id_nimble,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                    )
                )
        return contacts_schema


# end file contacts/app/services/nimble_service.py
