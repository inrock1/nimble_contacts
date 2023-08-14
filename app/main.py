# contacts/app/main.py
import uvicorn
from fastapi import FastAPI

from app.api.contacts import router as contact_router
from app.celery_tasks.tasks import fetch_nimble_contacts
from app.utils.csv_to_db import init_db_from_csv

app = FastAPI(title="simplified contact search service")
app.include_router(contact_router, prefix="/api")


@app.on_event("startup")
def startup():
    init_db_from_csv()
    fetch_nimble_contacts.delay()


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)

# end of file contacts/app/main.py
