#!/bin/bash
trap ctrl_c INT

function ctrl_c() {
  fuser -k 5050/tcp
  fuser -k 5051/tcp
  fuser -k 5052/tcp
  echo "I catch U!!!"
}

if [ ! -f tickets/passeios.json ] || [ ! -f tickets/aeroportos.json ] || [ ! -f tickets/hospedagens.json ]; then
  echo "Gerando mocks"
  cd tickets &&
  python3 ticketsGenerator.py
  cd ..
fi

#Verificar se venv existe
source venv/bin/activate
pip3 install flask

#Verificar se há python 3.7
python3.7 ticketServer.py &
python3.7 hospServer.py &
python3.7 passeioServer.py &

#Criar 2 instancias em diferentes portas
python3 main.py