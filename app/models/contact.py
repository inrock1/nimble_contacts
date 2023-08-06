#  start file contacts/app/models/contact.py
from typing import Optional

from pydantic import BaseModel


class Contact(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: Optional[str] = None

#  end file contacts/app/models/contact.py
