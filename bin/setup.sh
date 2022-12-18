#!/usr/bin/env bash

echo "Thank you for installing Prateek Khindri's TicTacToe terminal application." 
sleep 1
if ! [[ -x "$(command -v python3)" ]]
then
  echo "Error : 
    Prateek Khindri's Tic Tac Toe terminal application requires Python 3 to run, but it looks like Python 3 is not installed.
    To install Python 3, please head to https://www.python.org/downloads/" >&2
  exit 1
fi

if command -v python3 &> /dev/null
  then
    echo "Creating the virtual environment..."
    python3 -m venv venv
    sleep 1
    echo "Activating the virtual environment..."
    source venv/bin/activate
    sleep 1
    echo "Installing dependencies required to run Tic Tac Toe..."
    pip3 install -r requirements.txt
    sleep 1
    echo "All dependencies have been installed. Please run the application using the following command:..."
    echo "./bin/tic_tac_toe.sh"
    sleep 1
    exit
fi

if command -v python &> /dev/null
  then
    echo "Creating the virtual environment..."
    python -m venv venv
    sleep 1
    echo "Activating the virtual environment..."
    source venv/bin/activate
    sleep 1
    echo "Installing dependencies required to run Tic Tac Toe..."
    pip install -r requirements.txt
    sleep 1
    echo "All dependencies have been installed. Please run the application using the following command:..."
    echo "./bin/tic_tac_toe.sh"
    sleep 1
    exit
fi