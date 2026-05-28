#!/bin/bash
cd /root/task || exit 1
echo "[INFO] Starting docker-compose build and deployment..."
docker-compose up -d --build
COUNT=0
while [ $COUNT -lt 10 ]; do
  sleep 3
  if curl -sf http://localhost:8000/healthz > /dev/null; then
    echo "[SUCCESS] Service healthy and responding."
    exit 0
  fi
  COUNT=$((COUNT + 1))
  echo "[INFO] Waiting for service to become healthy... ($COUNT)"
done
echo "[ERROR] Service did not become healthy after 30 seconds."
docker-compose logs notes_api
exit 1
