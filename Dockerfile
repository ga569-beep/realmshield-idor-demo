FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    patch \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY tests ./tests
COPY pytest.ini .
COPY prompt.txt .
COPY artifacts ./artifacts

RUN touch app/__init__.py app/routes/__init__.py

CMD ["pytest", "-q"]
