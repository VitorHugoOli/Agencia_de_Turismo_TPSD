#!/bin/bash
trap ctrl_c INT

function ctrl_c() {
  fuser -k 5050/tcp
  fuser -k 5051/tcp
  fuser -k 5052/tcp
  fuser -k 5000/tcp
  fuser -k 5001/tcp
  echo "$(tput setaf 5)$(tput bold)I catch U!!!$(tput sgr0)"
}

if [ ! -f tickets/passeios.json ] || [ ! -f tickets/aeroportos.json ] || [ ! -f tickets/hospedagens.json ]; then
  echo "$(tput setaf 3)$(tput bold)Gerando mocks$(tput sgr0)"
  cd tickets &&
  python3 ticketsGenerator.py
  cd ..
fi

if [ ! -f venv ];then
  echo "$(tput setaf 3)$(tput bold)Criando venv$(tput sgr0)"
  python3 -m venv venv
  source venv/bin/activate
  pip3 install flask
fi

source venv/bin/activate

#Verificar se há python 3.7
python3.7 ticketServer.py &
python3.7 hospServer.py &
python3.7 passeioServer.py &
python3 main.py -p 5000 &
python3 main.py -p 5001

