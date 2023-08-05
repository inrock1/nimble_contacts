#  start file contacts/app/models/contact.py
from pydantic import BaseModel

class Contact(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str

#  end file contacts/app/models/contact.py