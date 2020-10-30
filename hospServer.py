import asyncio
import datetime
import json

from sockets.server import EasySocketServer


def getHosps(hosps, ida, cidade, pessoas):
    rListHosp = []
    for h in hosps:
        if (h['cidade'] == cidade):
            if ((datetime.datetime.strptime(h['diaEntrada'], "%d/%m/%Y") == datetime.datetime.strptime(ida,
                                                                                                       '%Y-%m-%d')) & (
                    h['qtdCamas'] >= pessoas)):
                rListHosp.append(h)

    return {'hospedagens': rListHosp}


async def handleData(data, sock,hosps):
    print(f"Recive data {data}")
    try:
        if data['action'] == 'hospedar':
            sock.send(getHosps(hosps, data['diaIda'], data['cidade'], data['numeroDePessoas']))
        if data['action'] == 'reservar':
            sock.send(data)
    except Exception as ex:
        print(ex)
        sock.send(False)


async def main():
    sock = EasySocketServer(5050)
    with open('tickets/hospedagens.json') as json_file:
        hosps = json.load(json_file)
    while True:
        data = await sock.listen()
        await handleData(data, sock,hosps)


asyncio.run(main())
