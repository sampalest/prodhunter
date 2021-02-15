#!/bin/bash
# strict mode
set -e
set -u
set -o pipefail

export PYTHONPATH=/app

APP_DIR=app
VERSION=$(cat VERSION)

echo "Starting Scheduler VERSION=${VERSION}"
python $APP_DIR/main.py "$@"
