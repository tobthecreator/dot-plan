#!/bin/bash

if [ $# -eq 0 ]; then
    echo "At least one argument is required."
    exit 1
fi

python3 ~/bin/dot-plan/main.py "$@"
