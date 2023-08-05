# start of file contacts/app/celery_config.py
from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0', include=["app.tasks"])

# Celery beat scheduler configuration
celery_app.conf.beat_schedule = {
    "fetch-nimble-contacts": {
        "task": "app.tasks.tasks.fetch_nimble_contacts",
        "schedule": 60,  # 600 seconds (10 minutes)
    },
}

# end of file contacts/app/celery_config.py