# contacts/app/tasks/tasks.py
from contextlib import contextmanager

from celery import Celery

from app.core.database import get_db
from app.repositories.contact_repository import PersonRepository
from app.services.contact_service import ContactService

celery_app = Celery(
    "tasks", backend="redis://redis:6379/1", broker="redis://redis:6379/0"
)


celery_app.conf.beat_schedule = {
    "run-fetch-nimble": {
        "task": "app.celery_tasks.tasks.fetch_nimble_contacts",
        "schedule": 86400,  # seconds
    },
}


@celery_app.task
def fetch_nimble_contacts():
    with contextmanager(get_db)() as session:
        contact_repo = PersonRepository(session)
        service = ContactService(contact_repo)
        service.check()


# end of file contacts/app/tasks/tasks.py
