#!/usr/bin/env bash
set -e

# Always run from the directory where the script is located
cd "$(dirname "$0")"

echo "Starting Playwright Desktop Environment..."
echo " -> WebVNC URL: http://localhost:6080/vnc.html?autoconnect=true&resize=scale"
echo " -> Press Ctrl + C ONCE to stop immediately."

docker compose down --remove-orphans 2>/dev/null || true
trap 'echo "Stopping..."; docker compose down --remove-orphans; exit 0' INT TERM
docker compose up --build