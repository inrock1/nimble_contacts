# contacts/app/tasks.py
import os

import requests
from celery import Celery
from app.helpers import update_database_from_nimble

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def fetch_nimble_contacts(api_key: str):
    update_database_from_nimble(api_key)
