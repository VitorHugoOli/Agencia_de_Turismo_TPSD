import asyncio
import datetime
import json

from sockets.server import EasySocketServer


def getPasseio(passeio, ida, cidade):
    rListPass = []
    a:str = ''
    for p in passeio:
        if p['cidade'] in cidade or p['endereco'] in cidade:
            if datetime.datetime.strptime(p['dia'], "%d/%m/%Y") == datetime.datetime.strptime(ida, '%Y-%m-%d'):
                rListPass.append(p)
    return {'passeio': rListPass}


async def handleData(data, sock, passeio):
    print(f"Recive data {data}")
    try:
        sock.send(getPasseio(passeio, data['dataIda'], data['cidade']))
    except Exception as ex:
        print(ex)
        sock.send(False)


async def main():
    sock = EasySocketServer(5052)
    with open('tickets/passeios.json') as json_file:
        passeio = json.load(json_file)
    while True:
        data = await sock.listen()
        await handleData(data, sock, passeio)


asyncio.run(main())
