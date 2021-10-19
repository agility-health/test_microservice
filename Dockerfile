FROM python:3.8
ENV PYTHONBUFFERED 1
ENV FLASK_APP service.py
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . /app

CMD poetry run flask run --host 0.0.0.0
