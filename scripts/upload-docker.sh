#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath="phamanhtuan221995/ml-classification"


# Step 2:
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
# docker login --username phamanhtuan221995
docker image tag ml-classification $dockerpath

# Step 3:
# Push image to a docker repository
docker push $dockerpath
