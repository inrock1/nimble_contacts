# contacts/app/helpers.py
from app.database import insert_contact_to_db
from app.models.contact import Contact
from app.services.nimble_service import NimbleService


def update_database_from_nimble(api_key: str):
    nimble_service = NimbleService(api_key)
    nimble_contacts = nimble_service.get_contacts()
    print("nimble_contacts: ", nimble_contacts)

    person_contacts = [contact for contact in nimble_contacts if contact.get("record_type") == "person"]

    for contact_data in person_contacts:
        nimble_contact = Contact(
            id=contact_data["id"],
            first_name=contact_data["fields"]["first name"][0]["value"],
            last_name=contact_data["fields"]["last name"][0]["value"],
            email=contact_data["fields"]["email"][0]["value"],
        )

        if nimble_contact.first_name and nimble_contact.last_name and nimble_contact.email:
            insert_contact_to_db(
                id=nimble_contact.id,
                first_name=nimble_contact.first_name,
                last_name=nimble_contact.last_name,
                email=nimble_contact.email,
            )
