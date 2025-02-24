FROM python:3.9-slim

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt



RUN mkdir -p /app/results

CMD ["python", "Cryptopricefetch.py"]