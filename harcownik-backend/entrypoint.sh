#! /usr/bin/env bash
set -e

log_info() {
    echo "[INFO] [$(date)] $*"
}

log_error() {
    echo "[ERROR] [$(date)] $*"
}

# Let the DB start
#python3 ./backend_test_connection.py
#log_info "Database is running!"

# Run migrations
alembic upgrade head
log_info "Migration has been succesfully run!"

# Create initial data in DB
if python ./initial_data.py 2>/dev/null; then
    log_info "Initial data has been succesfully created!"
else
    log_info "Initial data exists!"
fi

# Entrypoint
uvicorn src.main:app --host 0.0.0.0 --port 8000
