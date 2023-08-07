# contacts/app/main.py
from fastapi import FastAPI

from app.api.contacts import router as contact_router
from app.celery_tasks.tasks import fetch_nimble_contacts


app = FastAPI()
app.include_router(contact_router, prefix="/api")


@app.on_event("startup")
def startup():
    fetch_nimble_contacts.delay()


@app.get("/")
async def root():
    return {"message": "Root page"}


# end of file contacts/app/main.py
