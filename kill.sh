#!/bin/bash
cd /root/task || exit 0
echo "[INFO] Stopping and cleaning up containers..."
docker-compose down --volumes --remove-orphans
IMAGES=$(docker images -q 'task*')
if [ ! -z "$IMAGES" ]; then
  docker rmi $IMAGES 2>/dev/null || true
fi
docker system prune -a --volumes -f
rm -rf /root/task
echo "[INFO] Cleanup complete."
