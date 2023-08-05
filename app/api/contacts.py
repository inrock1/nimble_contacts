# contacts/app/api/contacts.py

from fastapi import APIRouter, Depends, HTTPException
from ..models.contact import Contact
from ..services.nimble_service import NimbleService

router = APIRouter()

class ContactAPI:
    def __init__(self, nimble_service: NimbleService = Depends()):
        self.nimble_service = nimble_service

    @router.get("/contacts")
    def search_contacts(self, query: str):
        contacts = self.nimble_service.get_contacts()
        filtered_contacts = [
            Contact(contact["id"], contact["fields"]["company name"][0]["value"])
            for contact in contacts
            if query.lower() in contact["fields"]["company name"][0]["value"].lower()
        ]
        return filtered_contacts
