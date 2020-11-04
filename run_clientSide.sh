#!/bin/bash
trap ctrl_c INT

function ctrl_c() {
  fuser -k 5000/tcp
  fuser -k 5001/tcp
  echo "$(tput setaf 5)$(tput bold)I catch U!!!$(tput sgr0)"
}

source venv/bin/activate

python3 main.py -p 5000 &
python3 main.py -p 5001