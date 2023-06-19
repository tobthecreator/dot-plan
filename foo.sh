#!/bin/bash
echo 'Running Script'

# Check if at least one argument is provided
if [ $# -eq 0 ]; then
    echo "At least one argument is required."
    exit 1
fi

# TODO for multiple args, we're gonna need an array
# very easy to handle on the python side

python3 main.py "$@"

# read
# r
# query, as a string. if empty, read today

# write
# w
# type
# in quotes, the thing

# python3 main.py

