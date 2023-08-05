# start file contacts/app/services/nimble_service.py

import requests

class NimbleService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_contacts(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get("https://api.nimble.com/api/v1/contacts", headers=headers)
        if response.status_code == 200:
            return response.json().get("resources", [])
        return []

# end file contacts/app/services/nimble_service.py