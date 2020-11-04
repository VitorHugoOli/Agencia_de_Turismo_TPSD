import getopt
import sys
import timeit

import werkzeug
from flask import Flask, request, redirect, render_template

from sockets.client import EasySocketClient

app = Flask(__name__)
# aeroporto
aeroporto = {}
dados_aero = {}

# hotel

hotel = {}
dados_hotel = {}

passeio = {}
dados_passeio = {}

serverAero = EasySocketClient(5050)
serverHotel = EasySocketClient(5051)
serverPasseio = EasySocketClient(5052)


@app.route('/', methods=['POST', 'GET'])  # home.html
def index():
    if request.method == 'POST':
        aero = request.form['aeroporto']
        data_ida = request.form['dataida']
        data_volta = request.form['datavolta']
        passagens = request.form['npassagens']

        data = {
            "paraAeroporto": aero,
            "dataIda": data_ida,
            "dataVolta": data_volta,
            "numeroPassagens": passagens
        }

        start = timeit.timeit()
        aeroporto = serverAero.send({'action': 'passagem', **data})
        end = timeit.timeit()
        print(f"Tempo Server Aero: {end - start}")
        dados_aero['aero_ida'] = aeroporto['ida']
        dados_aero['aero_volta'] = aeroporto['volta']

        return redirect('/aero')

    return render_template('index.html')


@app.route('/aero', methods=['POST', 'GET'])
def showAero():
    if request.method == 'POST':
        return redirect('/hotel')
    return render_template('showAero.html', aero_ida=dados_aero['aero_ida'], aero_volta=dados_aero['aero_volta'])


@app.route('/hotel', methods=['POST', 'GET'])
def selectHotel():
    if request.method == 'POST':
        cidades = request.form['cidades']
        dataidahotel = request.form['dataidahotel']
        datavoltahotel = request.form['datavoltahotel']
        npessoas = request.form['npessoas']

        data = {
            "cidade": cidades,
            "numeroDePessoas": npessoas,
            "dataIda": dataidahotel,
            "dataVolta": datavoltahotel,
        }

        start = timeit.timeit()
        hotel = serverHotel.send({'action': 'hospedar', **data})
        end = timeit.timeit()
        print(f"Tempo Server Hotel: {end - start}")

        dados_hotel['hosp'] = hotel['hospedagens']

        return redirect('/showHotel')
    return render_template('hotel.html')


@app.route('/showHotel', methods=['POST', 'GET'])
def showHoteis():
    if request.method == 'POST':
        return redirect('/passeio')
    return render_template('showHotel.html', hosp=dados_hotel['hosp'])


@app.route('/passeio', methods=['POST', 'GET'])
def selectPasseio():
    if request.method == 'POST':
        print(request.form)
        cidadePasseio = request.form['cidade']
        dataidaPasseio = request.form['dataidaPasseio']

        data = {
            "cidade": cidadePasseio,
            "dataIda": dataidaPasseio
        }

        start = timeit.timeit()
        passeio = serverPasseio.send({**data})
        end = timeit.timeit()
        print(f"Tempo Server Passeio: {end - start}")

        dados_passeio['passeio'] = passeio['passeio']

        return redirect('/showPasseio')
    return render_template('passeio.html')


@app.route('/showPasseio')
def showPasseio():
    return render_template('showPasseio.html', passeio=dados_passeio['passeio'])


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return render_template('Block.html', error=500)


# or, without the decorator
app.register_error_handler(500, handle_bad_request)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "p", ["port="])
    except getopt.GetoptError:
        print('Entre com alguma porta!!!')
        sys.exit(2)
    app.run(host='0.0.0.0', port=args[0])


if __name__ == "__main__":
    main(sys.argv[1:])
