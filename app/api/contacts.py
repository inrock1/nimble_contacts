# file contacts/app/api/contacts.py
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..database import ContactModel, get_db
from ..models.contact import Contact

router = APIRouter()


@router.get("/search/", response_model=list[Contact])
def search_contacts(query: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    search_query = f"%{query}%"
    contacts = (
        db.query(ContactModel)
        .filter(
            (ContactModel.first_name.ilike(search_query))
            | (ContactModel.last_name.ilike(search_query))
            | (ContactModel.email.ilike(search_query))
        )
        .all()
    )

    return contacts


# end of file contacts/app/api/contacts.py
