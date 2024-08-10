#!/bin/bash

# Check if Docker is installed
if ! [ -x "$(command -v docker)" ]; then
  echo 'Error: Docker is not installed.' >&2
  exit 1
fi

# Build the Docker image
echo "Building the Docker image..."
docker build -t my-python-app .

# Run the Docker container
echo "Running the Docker container..."

# Cross-platform volume mount
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  # Windows (Git Bash, WSL, etc.)
  winpty docker run --rm -v "/$(pwd)":/app my-python-app
else
  # Linux and MacOS
  docker run --rm -v "$(pwd):/app" my-python-app
fi

echo "Script executed successfully."
