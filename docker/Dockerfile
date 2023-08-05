# contacts/docker/Dockerfile

# Взять базовый образ с Python
FROM python:3.9

# Установить рабочую директорию
WORKDIR /app

# Установить зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копировать код приложения
COPY app/ app/

# Запустить приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
