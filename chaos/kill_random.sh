#!/usr/bin/env bash
# Randomly kills one of the service containers to simulate failure
set -euo pipefail
candidates=("auth-service" "video-service" "recommendation-service")
choice=${candidates[$RANDOM % ${#candidates[@]}]}
echo "Killing $choice"
docker kill $choice || true
