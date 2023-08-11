# file tests/conftest.py
import pytest
import requests_mock
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from app.config import TEST_DATABASE_URL
from app.models.contacts import Base


test_engine = create_engine(TEST_DATABASE_URL, echo=True)
SessionLocalTest = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
Base.metadata.create_all(bind=test_engine)


@pytest.fixture
def test_db():
    db = SessionLocalTest()
    try:
        yield db
    finally:
        db.close()

def clear_contacts_table(db: Session):
    delete_query = text("DELETE FROM contacts")
    db.execute(delete_query)
    db.commit()


@pytest.fixture
def mock_requests():
    with requests_mock.Mocker() as m:
        yield m


MOCK_RESPONSE = {
    "resources": [
        {
            "id": "64ca0fa4d1d39db980b9d42c",
            "record_type": "person",
            "fields": {
                "first name": [{"value": "Jon1"}],
                "last name": [{"value": "Ferrara"}],
                "email": [{"value": "care@nimble.com"}]
            }
        }
    ]
}

# end of file tests/conftest.py