#!/usr/bin/env bash

if [ "$1" == "--test" ] || [ "$1" == "--t" ] || [ "$1" == "-t" ] || [ "$1" == "-test" ]
then
    echo "Running tests using pytest..."
    source venv/bin/activate
    pytest
    exit
elif [ "$1" == "--help" ] || [ "$1" == "--h" ] || [ "$1" == "-h" ] || [ "$1" == "-help" ]
then
    cat ./src/tic_tac_toe/docs/help.hlp
    exit
elif [ "$1" == "--about" ] || [ "$1" == "--a" ] || [ "$1" == "-a" ] || [ "$1" == "-about" ]
then
    cat ./src/tic_tac_toe/docs/about.hlp
elif [ "$1" == "--stats" ] || [ "$1" == "--s" ] || [ "$1" == "-s" ] || [ "$1" == "-stats" ]
then
    cat ./data/computer.json
    cat ./data/multiplayer.json
else
    source venv/bin/activate
    python3 ./src/tic_tac_toe/main.py
    exit
fi
