#  start file contacts/app/serializers/contact_serializer.py
from typing import Optional

from pydantic import BaseModel


class ContactSchema(BaseModel):
    id_nimble: Optional[str] = None
    first_name: str
    last_name: str
    email: Optional[str] = None


#  end file contacts/app/serializers/contact_serializer.py
