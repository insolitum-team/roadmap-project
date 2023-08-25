FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /usr/src/api

COPY poetry.lock pyproject.toml ./

RUN pip3 install poetry && \
    poetry install --no-root

COPY . ./

RUN chmod +x ./scripts/entrypoint.sh && \
    chmod +x ./scripts/check-migrations.sh

ENTRYPOINT ["./scripts/entrypoint.sh"]
