FROM python:3.8

ENV PYTHONBUFFERED=1
ENV FLASK_APP=service.py

WORKDIR /app

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . .

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]