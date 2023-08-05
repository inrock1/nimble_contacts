# contacts/app/tasks/celery_config.py
from celery import Celery

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",  # Replace with your Redis URL if different
    include=["app.tasks"],
)

# Optional configuration settings for Celery
# app.conf.update(
#     result_backend="db+sqlite:///results.db",
#     task_serializer="json",
#     result_serializer="json",
#     accept_content=["json"],
#     timezone="Europe/Oslo",
#     enable_utc=True,
# )

# end of file contacts/app/tasks/celery_config.py