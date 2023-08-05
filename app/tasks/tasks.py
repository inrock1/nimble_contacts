# contacts/app/tasks/tasks.py
from celery import Celery
from app.helpers import update_database_from_nimble
from app.tasks.celery_config import celery_app

@celery_app.task
def fetch_nimble_contacts(api_key: str):
    update_database_from_nimble(api_key)

# end of file contacts/app/tasks/tasks.py