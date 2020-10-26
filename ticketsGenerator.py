# coding=UTF-8
import random as rd
import json
import os

tickets = []
passeios = []
hosp = []
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

cidades = [
    {'hospedagens': [{'nome': 'Amazon Xingu Hotel', 'endereco': 'Av. Djalma Dutra, 2081 - Centro, Altamira - PA'}, {'nome': 'Xingu Praia Hotel', 'endereco': 'R. Cel. José Porfírio, 3001 - Esplanada do Xingu, Altamira - PA'}, ],
        'cidade': 'Altamira (PA)', 'passeios': [{'endereco': 'Altamira - PA', 'local': 'Cachoeira do Rio Curuá'}, {
            'endereco': 'R. Monte Sião - Brasília, Altamira - PA', 'local': 'Praça do Mirante'}]},

    {'hospedagens': [{'nome': 'Hotel Dunamys Curitiba', 'endereco': 'Rod. BR-116, Km 93 3750 - Bairro Alto, Curitiba - PR'}, {'nome': 'Three Little Birds Hospedagem', 'endereco': 'R. José Mario de Oliveira, 177 - Bacacheri, Curitiba - PR'}, ],
        'cidade': 'Bacacheri (PR)', 'passeios': [{'endereco': 'Av. Nossa Senhora da Luz, Curitiba - PR', 'local': 'Jardim  Social'}, {
            'endereco': 'Av. República Argentina, Bacacheri - PR', 'local': 'Novo Mundo'}]},

    {'hospedagens': [{'nome': 'Dallé Hotel', 'endereco': 'Av. Santa Tecla, 451 - Getúlio Vargas, Bagé - RS'}, {'nome': 'Fenícia Hotel', 'endereco': 'R. Juvêncio Lemos, 45 - Centro, Bagé - RS'}, ],
        'cidade': 'Bagé (RS)', 'passeios': [{'endereco': ' R. Gen. Neto, 16 - Centro, Bagé - RS', 'local': 'Casa de Cultura Pedro Wayne'}, {
            'endereco': 'Av. Visc. Ribeiro de Magalhães, Bagé - RS', 'local': 'Centro Histórico Vila de Santa Thereza'}]},
    
    {'hospedagens': [{'nome': 'Hotel Ajuricaba', 'endereco': 'R. Ajuricaba, 179 - Centro, Boa Vista - RR'}, {'nome': 'Ferrari Palace Hotel', 'endereco': 'Av. Benjamin Constant, 2011 - Centro, Boa Vista - RR'}, ],
        'cidade': 'Boa Vista (RR)', 'passeios': [{'endereco': 'Centro, Boa Vista - RR', 'local': 'Praça das Águas'}, {
            'endereco': 'R. Floriano Peixoto - Centro, Boa Vista - RR', 'local': 'Orla Taumanan'}]},

    {'hospedagens': [{'nome': 'Bahamas Suíte Hotel', 'endereco': 'R. José Antônio, 1117 - Centro, Campo Grande - MS'}, {'nome': 'Hotel Mohave', 'endereco': 'Av. Afonso Pena, 602 - Amambai, Campo Grande - MS'}, ],
        'cidade': 'Campo Grande (MS)', 'passeios': [{'endereco': 'Rua 14 de Julho - Centro, Campo Grande - MS', 'local': 'Praça Ary Coelho'}, {
            'endereco': 'Av. Afonso Pena, s/n - Centro, Campo Grande - MS', 'local': 'Parque das Nações Indígenas'}]},

    {'hospedagens': [{'nome': 'Hotel Mandari', 'endereco': 'Av. Rodrigues Alves, 433 - Centro, Cruzeiro do Sul - AC'}, {'nome': 'Hotel Juruá', 'endereco': 'R. Alfredo Téles, 532 - João Alves, Cruzeiro do Sul - AC'}, ],
        'cidade': 'Cruzeiro do Sul (AC)', 'passeios': [{'endereco': 'Cruzeiro do Sul - AC', 'local': 'Rio Croa'}, {
            'endereco': 'R. Rui Barbosa - Centro, Cruzeiro do Sul - AC', 'local': 'Catedral de Cruzeiro do Sul'}]},

    {'hospedagens': [{'nome': 'Oft San Conrado hotel', 'endereco': 'R. 3, 652 - St. Central, Goiânia - GO'}, {'nome': 'Pousada Ana Poipa', 'endereco': 'R. 14, 291 - Aeroviario, Goiânia - GO'}, ],
        'cidade': 'Goiânia (GO)', 'passeios': [{'endereco': 'Av. T-10, s/n - St. Bueno, Goiânia - GO', 'local': 'Parque Vaca Brava'}, {
            'endereco': 'Av. Assis Chateaubriand - St. Oeste, Goiânia - GO', 'local': 'Bosque dos Buritis'}]},

    {'hospedagens': [{'nome': 'Imperial Hotel', 'endereco': 'Rod, BR-010, 100 - Jardim Sao Luis, Imperatriz - MA'}, {'nome': 'Posseidon Hotel', 'endereco': 'Centro, Imperatriz - MA'}, ],
        'cidade': 'Imperatriz (MA)', 'passeios': [{'endereco': 'KM 69,5 ZONA RURAL, BR-010, Carolina - MA',
                                                   'local': 'Cachoeira da Pedra Caída'}, {'endereco': 'Centro, Imperatriz - MA', 'local': 'Praça de Fátima'}]},

    {'hospedagens': [{'nome': 'Hotel Slim Joinville', 'endereco': 'R. Sete de Setembro, 40 - Centro, Joinville - SC'}, {'nome': 'Hotel Tannenhof', 'endereco': 'R. Visc. de Taunay, 340 - Atiradores, Joinville - SC'}, ],
        'cidade': 'Joinville (SC)', 'passeios': [{'endereco': 'Pirabeiraba, Joinville - SC', 'local': 'Mirante da Serra Dona Francisca'}, {
            'endereco': 'R. Pastor Guilherme Ráu, 462 - Saguaçu, Joinville - SC', 'local': 'Zoobotânico Joinville'}]},

    {'hospedagens': [{'nome': 'Hotel JK', 'endereco': 'R. Tiradentes, 1273 - Central, Macapá - AP'}, {'nome': 'Amazon Plaza Hotel', 'endereco': 'R. Beira Rio, 208 - Santa Ines, Macapá - AP'}, ],
        'cidade': 'Macapá (AP)', 'passeios': [{'endereco': 'Praça Floriano Peixoto : Macapá, AP', 'local': 'Praça Floriano Peixoto'}, {
            'endereco': 'Av. Felíciano Coelho, 1509 - Trem, Macapá - AP', 'local': 'Museu Sacaca'}]},

    {'hospedagens': [{'nome': 'Céu Palmas Hotel', 'endereco': 'Quadra 201 Sul, Av. Joaquim Teotônio Segurado, 201 - Plano Diretor Expansão Sul, Palmas - TO'}, {'nome': 'Italian Palace Hotel', 'endereco': 'Avenida Joaquim Teotônio Segurado, Q. 1201 Sul Avenida Joaquim Teotônio Segurado, Conjunto 01, Lote 19 - Plano Diretor Sul, Palmas - TO'}, ],
        'cidade': 'Palmas (TO)', 'passeios': [{'endereco': 'Ilha Canela s/n Lago de, Palmas - TO', 'local': 'Ilha Canela Beach'}, {
            'endereco': 'Av. Joaquim Teotônio Segurado, s/n - Plano Diretor Sul, Palmas - TO', 'local': 'Praça dos Girassóis'}]},
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
    write_file('passeios.txt', passeios)
    write_file('hospedagens.txt', hosp)


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

    # passeios
    for city in cidades:
        for passeio in city['passeios']:
            hr1, hr2 = getHours()
            isFree = rd.randint(0, 1)
            passeioPrice = isFree * rd.randint(10, 100)
            passeios.append({
                'horario': '{}:00h'.format(hr1),
                'valor': '{},00R$'.format(passeioPrice),
                'dia': '{}/{}/{}'.format(formatHour(d), formatHour(m), y),
                'local': passeio['local'],
                'endereco': passeio['endereco'],
                'cidade': city['cidade'],
            })

    # hospedagem
    for city in cidades:
        for h in city['hospedagens']:
            cafe = rd.randint(0, 1)
            nightPrice = rd.randint(100, 1000)
            numero = rd.randint(1, 100)
            qtdQuartos = rd.randint(1, 5)
            qtdCamas = qtdQuartos * rd.randint(1, 3)
            hosp.append({
                'diaEntrada': '{}/{}/{}'.format(formatHour(d), formatHour(m), y),
                'numero': numero,
                'qtdQuartos': qtdQuartos,
                'qtdCamas': qtdCamas,
                'valor': '{},00R$'.format(nightPrice),
                'nome': h['nome'],
                'endereco': h['endereco'],
                'cidade': city['cidade'],
                'cafeDaManha': (cafe == 0)
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
    f = open(name, "w+", -1, "utf-8")
    f.write(json.dumps(content, indent=4))
    f.close()


ticketGen()
