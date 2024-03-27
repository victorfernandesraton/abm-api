FROM python:3.11-slim-bookworm

WORKDIR /app
ENV POETRY_VIRTUALENVS_CREATE=false
RUN python -m pip install --upgrade pip
RUN pip install poetry 
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-interaction --no-cache --only=main 

COPY . .

EXPOSE 8080
CMD ["bash", "entrypoint.sh"]

