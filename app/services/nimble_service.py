# contacts/app/services/nimble_service.py

import requests

class NimbleService:
    def __init__(self, api_key: str, requests_session: requests.Session = None):
        self.api_key = api_key
        self.requests_session = requests_session or requests.Session()

    def get_contacts(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = self.requests_session.get(
            "https://api.nimble.com/api/v1/contacts", headers=headers
        )
        if response.status_code == 200:
            return response.json().get("resources", [])
        response.raise_for_status()

# end file contacts/app/services/nimble_service.py
