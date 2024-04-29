#!/bin/bash

# Check if the required command-line argument is provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide a command-line argument."
    exit 1
fi

# Attempt to read from a non-existent file
if [ ! -f "$1" ]; then
    echo "Error: File $1 does not exist."
    exit 1
fi

echo "Success: File $1 exists and can be read."
