import asyncio
import datetime
import json

from sockets.server import EasySocketServer


def getTickets(tickets, ida, volta, aeroporto):
    rListIda = []
    rListVolta = []
    for t in tickets:

        if t['paraAeroporto'] == aeroporto and datetime.datetime.strptime(t['diaIda'],
                                                                          "%d/%m/%Y") == datetime.datetime.strptime(ida,
                                                                                                                    '%Y-%m-%d'):
            rListIda.append(t)

        elif t['deAeroporto'] == aeroporto and datetime.datetime.strptime(t['diaIda'],
                                                                          "%d/%m/%Y") == datetime.datetime.strptime(
            volta, '%Y-%m-%d'):
            rListVolta.append(t)

    return {'ida': rListIda, 'volta': rListVolta}


async def main():
    sock = EasySocketServer()
    with open('aeroportos.json') as json_file:
        tickets = json.load(json_file)
    while True:
        data = await sock.listen()
        print(f"Recive data {data}")
        try:
            if data['action'] == 'passagem':
                sock.send(getTickets(tickets, data['dataIda'], data['dataVolta'], data['paraAeroporto']))
            if data['action'] == 'reservar':
                sock.send(data)
        except Exception as ex:
            print(ex)
            sock.send(False)
            continue


asyncio.run(main())
