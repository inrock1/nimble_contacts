# start file contacts/app/helpers.py
from app.database import ContactModel, SessionLocal
from app.models.contact import Contact
from app.services.nimble_service import NimbleService


def update_database_from_nimble(api_key: str):
    nimble_service = NimbleService(api_key)
    nimble_contacts = nimble_service.get_contacts()

    person_contacts = [
        contact for contact in nimble_contacts if contact.get("record_type") == "person"
    ]

    with SessionLocal() as db:
        for contact_data in person_contacts:
            first_name = contact_data["fields"].get("first name", [{}])[0].get("value")
            last_name = contact_data["fields"].get("last name", [{}])[0].get("value")
            email = contact_data["fields"].get("email", [{}])[0].get("value")
            # print(
            #     "first_name: ", first_name, "last_name: ", last_name, "email: ", email
            # )
            if first_name and last_name:
                nimble_contact = Contact(
                    id=contact_data["id"],
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )

                existing_contact = (
                    db.query(ContactModel).filter_by(id=nimble_contact.id).first()
                )

                if existing_contact:
                    # Check for differences before updating
                    if (
                        existing_contact.first_name != nimble_contact.first_name
                        or existing_contact.last_name != nimble_contact.last_name
                        or existing_contact.email != nimble_contact.email
                    ):
                        # Update the existing_contact
                        existing_contact.first_name = nimble_contact.first_name
                        existing_contact.last_name = nimble_contact.last_name
                        existing_contact.email = nimble_contact.email
                        db.commit()
                else:
                    # Contact does not exist, perform insertion
                    contact_model = ContactModel(
                        id=nimble_contact.id,
                        first_name=nimble_contact.first_name,
                        last_name=nimble_contact.last_name,
                        email=nimble_contact.email,
                    )
                    db.add(contact_model)
                    db.commit()
        print("checking updates completed")


# end file contacts/app/helpers.py
