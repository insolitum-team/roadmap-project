#!/bin/bash
set -e
if poetry run alembic history --verbose | grep "downgrade" > /dev/null; then
  poetry run alembic upgrade head
else
  echo "Database is up to date"
fi
