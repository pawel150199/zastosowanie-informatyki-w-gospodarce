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
python ./initial_data.py
log_info "Initial data has been succesfully created!" 
