FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY config.ini .
COPY scripts .

ENTRYPOINT ["python", "app.py"]