#!/bin/bash

set -e

if [ ! -d "ollama" ]; then
    echo "updating system packages..."
    yes "" | pkg update -y

    echo "installing Go, Git, and CMake..."
    pkg install golang git cmake -y

    echo "cloning ollama repository..."
    git clone https://github.com/ollama/ollama
fi

cd ollama

if [ ! -f "ollama" ]; then
    echo "building ollama..."
    go generate ./...
    go build .
    echo "build completed!"

    echo "creating symbolic link to $PREFIX/bin/ollama"
    ln -sf $(pwd)/ollama $PREFIX/bin/ollama
fi

echo "starting ollama service in the background..."
nohup ./ollama serve &
echo "ollama service has started."

echo "ollama service pid is $!"
