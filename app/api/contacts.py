# file contacts/app/api/contacts.py
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db

from ..models.contacts import ContactModel
from ..repositories.contact_repository import ContactRepository
from ..serializers.contact_serializer import ContactSchema

router = APIRouter()


@router.get("/search/", response_model=list[ContactSchema])
def search_contacts(
    query: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    contact_repo = ContactRepository(db)
    contacts = contact_repo.search_contacts(query)
    return contacts


# end of file contacts/app/api/contacts.py
