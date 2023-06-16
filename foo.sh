#!/bin/bash
echo 'Running Script'
# exec "ls"

# Check if at least one argument is provided
if [ $# -eq 0 ]; then
    echo "At least one argument is required."
    exit 1
fi

python3 main.py "$1" "$2" "$3"


echo $command

# read
# r
# query, as a string. if empty, read today

# write
# w
# type
# in quotes, the thing

# python3 main.py

