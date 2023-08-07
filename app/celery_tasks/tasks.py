# contacts/app/tasks/tasks.py
from celery import Celery

from app.config import NIMBLE_API_KEY
from app.helpers import update_database_from_nimble


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


# run worker:   celery -A app.celery_tasks.tasks worker --loglevel=info --pool=solo -E
# run beat:     celery -A app.celery_tasks.tasks beat --loglevel=info
# run flower:   celery -A app.celery_tasks.tasks flower

# end of file contacts/app/tasks/tasks.py
