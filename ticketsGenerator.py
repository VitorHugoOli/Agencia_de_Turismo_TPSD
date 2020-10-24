import random as rd
import json
import os

tickets = []
airports = [
    'Aeroporto de Altamira - Altamira (PA)',
    'Aeroporto do Paraná - Bacacheri (PR)',
    'Aeroporto Internacional de Bagé Comandante Gustavo Kraemer - Bagé (RS)',
    'Aeroporto Internacional de Boa vista Atlas Brasil Cantanhede - Boa Vista (RR)',
    'Aeroporto Internacional de Campo Grande - Campo Grande (MS)',
    'Aeroporto Internacional Cruzeiro do Sul - Cruzeiro do Sul (AC)',
    'Aeroporto de Goiânia Santa Genoveva - Goiânia (GO)',
    'Aeroporto de Imperatriz Prefeito Renato Moreira - Imperatriz (MA)',
    'Aeroporto de Joinville Lauro Carneiro de Loyola - Joinville (SC)',
    'Aeroporto Internacional de Macapá Alberto Alcolumbre - Macapá (AP)',
    'Aeroporto de Palmas Brigadeiro Lysias Rodrigues - Palmas (TO)',
]


def ticketGen(initd=1, initm=1, inity=2020, finald=30, finalm=12, finaly=2021):
    for i in range(inity, finaly):
        if(i == inity):
            monthGen(initm, finalm, initd, finald, i)
        elif (i == finaly):
            monthGen(1, 12, 1, finald, i)
        else:
            monthGen(1, 12, 1, 31, i)
    write_file('aeroportos.txt', tickets)


def formatHour(hr):
    if (hr > 0 and hr < 10):
        return "0{}".format(hr)
    return "{}".format(hr)


def getHours():
    hr = rd.randint(0, 22)
    plus = rd.randint(1, 10)
    hr2 = hr + plus
    if(hr2 > 23):
        hr2 = 23
    return (formatHour(hr), formatHour(hr2))


def createTicket(d, m, y):

    for airport in airports:
        for i in range(5):
            hr1, hr2 = getHours()
            price = rd.randint(400, 10000)
            # ida
            tickets.append({
                'horarioIda': '14:00h',
                'chegadaIda': '18:00h',
                'valor': '{},00R$'.format(price),
                'diaIda': '{}/{}/{}'.format(formatHour(d), formatHour(m), y),
                'diaChegada': '{}/{}/{}'.format(formatHour(d), formatHour(m), y),
                'deAeroporto': 'Aeroporto Internacional de Confins - Tancredo Neves',
                'paraAeroporto': airport,
            })
            # volta
            hr1, hr2 = getHours()
            price = rd.randint(400, 10000)
            tickets.append({
                'horarioIda': '{}:00h'.format(hr1),
                'chegadaIda': '{}:00h'.format(hr2),
                'valor': '{},00R$'.format(price),
                'diaIda': '{}/{}/{}'.format(formatHour(d), formatHour(m), y),
                'diaChegada': '{}/{}/{}'.format(formatHour(d), formatHour(m), y),
                'deAeroporto': airport,
                'paraAeroporto': 'Aeroporto Internacional de Confins - Tancredo Neves',
            })


def getRealFinal(final, month, year):
    if(month == 4 or month == 6 or month == 9 or month == 11):
        if(final > 30):
            return 30

    if(month == 2 and final > 28):
        if(year % 400 == 0):
            return 28
        elif (year % 100 != 0 and year % 4 == 0):
            return 28
        if(final >= 29):
            return 29
    if(final > 31):
        return 31
    return final


def dayGen(init, final, month, year):
    
    final = getRealFinal(final, month, year)
    print(final)
    for i in range(init, final):
        createTicket(i, month, year)


def monthGen(init, final, initd, finald, year):
    for i in range(init, final):
        if(i == init):
            dayGen(initd, 31, i, year)
        elif (i == final):
            dayGen(1, finald, i, year)
        else:
            dayGen(1, 31, i, year)


def write_file(name, content):
    f = open(name, "w+")
    f.write(json.dumps(content, indent=4))
    f.close()


ticketGen()
