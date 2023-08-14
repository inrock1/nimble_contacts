# Contact Management Service

A service with a contact database that is populated from a CSV file and an external API, which updates contacts in the database once a day. An API has been implemented with a single method that accepts a text query, enabling full-text search based on the provided input.

### API Documentation:
- Endpoint: http://localhost:8000/api/search/?query=<your_query>    
- Method: POST   
- Request Body: Text query for full-text search   
- Response: List of contacts matching the search query   

### Technologies:
- Python  
- FastApi   
- PostgreSQL   
- SQLAlchemy   
- Celery   
- Redis   
- Requests   
- Pytest   

### How to Run with docker:
```python
# Rename .env.sample to .env and put your credentials 
# (you can write only NIMBLE_API_KEY).
docker-compose build 
docker-compose up
```
### How to run tests with docker:
```python
# create test user and test DB
docker exec -it <CONTAINER_DB_ID_OR_NAME> bash
psql -U postgres
create database test_db;
CREATE USER test_user WITH PASSWORD 'test_password';
ALTER DATABASE test_db OWNER TO test_user;
GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;
\q
exit

# run tests
docker exec -it <CONTAINER_APP_ID_OR_NAME> bash
alembic -x alembic_test.ini upgrade head
pytest tests
```


### How to Run without docker:

Install the required dependencies mentioned in the requirements.txt file.   
/* if you run it in windows, please change in requirements.txt  
psycopg2-binary to psycopg2   
psycopg-binary to psycopg   
Rename .env.sample to .env and put your credentials (you can write only NIMBLE_API_KEY).   
Set up your PostgreSQL database and configure the connection.
```python
# start celery worker (for windows):   
celery -A app.celery_tasks.tasks worker --loglevel=info --pool=solo -E
# start celery worker (for unix):   
celery -A app.celery_tasks.tasks worker --loglevel=info -E
# start celery beat:   
celery -A app.celery_tasks.tasks beat --loglevel=info


```
Start the FastApi service 
```python
python.exe -m uvicorn app.main:app --reload 
```
API contact search will be able at: 
http://localhost:8000/api/search/?query=ххххх  
write your request instead of xxxхх   
Or use documentation at 
http://127.0.0.1:8000/docs    
