# start file contacts/app/services/contact_service.py
from app.dal.contact_dal import ContactDAL
from app.serializers.contactserializer import ContactSerializer
from app.services.nimble_service import NimbleService


def update_database_from_nimble(api_key: str):
    nimble_service = NimbleService(api_key)
    nimble_contacts = nimble_service.get_contacts()

    person_contacts = [
        contact for contact in nimble_contacts if contact.get("record_type") == "person"
    ]

    contact_dal = ContactDAL()

    for contact_data in person_contacts:
        first_name = contact_data["fields"].get("first name", [{}])[0].get("value")
        last_name = contact_data["fields"].get("last name", [{}])[0].get("value")
        email = contact_data["fields"].get("email", [{}])[0].get("value")

        if first_name and last_name:
            contact = contact_dal.create_contact(
                id=contact_data["id"],
                first_name=first_name,
                last_name=last_name,
                email=email,
            )

            existing_contact = contact_dal.get_contact_by_id(contact_data["id"])

            if existing_contact:
                # Check for differences before updating
                if (
                    existing_contact.first_name != contact.first_name
                    or existing_contact.last_name != contact.last_name
                    or existing_contact.email != contact.email
                ):
                    # Update the existing_contact
                    contact_dal.update_contact(
                        contact,
                        first_name=contact.first_name,
                        last_name=contact.last_name,
                        email=contact.email,
                    )

    contact_dal.close()
    print("checking updates completed")

# end file contacts/app/services/contact_service.py
