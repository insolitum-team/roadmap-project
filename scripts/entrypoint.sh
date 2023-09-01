#!/bin/bash
set -e
bash -c ./scripts/check-migrations.sh
poetry run uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
exec "$@"