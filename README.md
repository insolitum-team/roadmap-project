# 🎓 Insolitum Learn

## Backend logic implementation for <https://learn.insolitum.team/> with FastAPI

## 📍 Local development deeds

### ▶️ Running the server

To run the server use the command:

> `uvicorn api.main:app --reload`

### ➡️ Alembic migrations

After creating new models you need to import them into `common.db.models.init`

Then:

- make migrations with

> `alembic revision --autogenerate`

- migrate with

> `alembic upgrade head`
