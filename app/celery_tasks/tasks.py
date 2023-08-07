# contacts/app/tasks/tasks.py
from celery import Celery

from app.config import NIMBLE_API_KEY
from app.services.contact_service import update_database_from_nimble

celery_app = Celery(
    "tasks", backend="redis://localhost:6379/1", broker="redis://localhost:6379/0"
)


# Celery beat scheduler configuration
celery_app.conf.beat_schedule = {
    "run-fetch-nimble": {
        "task": "app.celery_tasks.tasks.fetch_nimble_contacts",
        "schedule": 86400,  # seconds
    },
}


@celery_app.task
def fetch_nimble_contacts():
    update_database_from_nimble(NIMBLE_API_KEY)


# end of file contacts/app/tasks/tasks.py
