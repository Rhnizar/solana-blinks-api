FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 8000

# Run Django server on 0.0.0.0:8000 to allow external connections
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]