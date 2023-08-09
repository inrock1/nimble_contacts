# start file contacts/app/services/contact_service.py
from app.config import NIMBLE_API_KEY
from app.repositories.contact_repository import ContactRepository
from app.services.nimble_service import NimbleService


class ContactService:
    def __init__(self, contact_repo: ContactRepository):
        self.repo = contact_repo

    def check(self):
        nimble_service = NimbleService(NIMBLE_API_KEY)
        nimble_contacts = nimble_service.get_contacts()

        for nimble_contact in nimble_contacts:
            db_contact = self.repo.get_contact_by_id(nimble_contact.id_nimble)

            if not db_contact:
                self.repo.create_contact(nimble_contact)
            else:
                # Check for differences before updating
                if (
                    db_contact.first_name != nimble_contact.first_name
                    or db_contact.last_name != nimble_contact.last_name
                    or db_contact.email != nimble_contact.email
                ):
                    # Update the contact
                    self.repo.update_contact(nimble_contact)

        self.repo.close()
        print("checking updates completed")


# end file contacts/app/services/contact_service.py
