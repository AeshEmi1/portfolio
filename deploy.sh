#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# 1. Shut down the stack and DELETE the static volume
echo "Clearing static_files volume..."
podman-compose down --volumes

# 2. Pulling latest containers
podman-compose pull

# 3. Bring the stack back up
echo "Starting containers..."
podman-compose up -d