#!/bin/bash
set -e

echo "Starting Uvicorn server..."
poetry run uvicorn src.app.main:app --host 0.0.0.0 --port 8002 --workers 4
