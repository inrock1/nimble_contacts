#  start file contacts/app/serializers/contact.py
from typing import Optional

from pydantic import BaseModel


class ContactSerializer(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: Optional[str] = None


#  end file contacts/app/serializers/contact.py
