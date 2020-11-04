#!/bin/bash
trap ctrl_c INT

function ctrl_c() {
  fuser -k 5050/tcp
  fuser -k 5051/tcp
  fuser -k 5052/tcp
  echo "$(tput setaf 5)$(tput bold)I catch U!!!$(tput sgr0)"
}

source venv/bin/activate

python3.7 ticketServer.py &
python3.7 hospServer.py &
python3.7 passeioServer.py