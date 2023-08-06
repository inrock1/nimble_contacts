# contacts/app/api/search.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.contact import Contact

router = APIRouter()


@router.get("/search/", response_model=List[Contact])
def search_contacts(
    query: str = Query(..., min_length=1, max_length=100),
    db: Session = Depends(SessionLocal),
):
    search_query = f"%{query}%"
    contacts = (
        db.query(Contact)
        .filter(
            (Contact.first_name.ilike(search_query))
            | (Contact.last_name.ilike(search_query))
            | (Contact.email.ilike(search_query))
        )
        .all()
    )
    return contacts


# end of file contacts/app/api/contacts.py
