from flask import Flask, redirect, url_for
from flask import render_template
from flask import request

from sockets.client import EasySocketClient

app = Flask(__name__)

aeroporto = {}

client = EasySocketClient()


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

        data = client.send({'action': 'passagem', **data})

        print(f"Resposta {data}")

        return redirect(url_for('selectHotel'))

    return render_template('index.html')


@app.route('/aero')
def showAero():
    return render_template('showAeros.html')


@app.route('/hotel', methods=['POST', 'GET'])
def selectHotel():
    if request.method == 'POST':
        cidades = request.form['cidades']
        dataidahotel = request.form['dataidahotel']
        datavoltahotel = request.form['datavoltahotel']
        npessoas = request.form['npessoas']

        data = {
            "cidade": cidades,
            "numeeroDePessoas": npessoas,
            "dataIda": dataidahotel,
            "dataVolta": datavoltahotel,
        }

        data = client.send({**data})

        print(f"Resposta {data}")

        return redirect(url_for('selectPasseio'))
    return render_template('hotel.html')


@app.route('/showHotel')
def showHoteis():
    return render_template('showHoteis.html')


@app.route('/passeio', methods=['POST', 'GET'])
def selectPasseio():
    if request.method == 'POST':
        cidadePasseio = request.form['cidadePasseio']
        dataidaPasseio = request.form['dataidaPasseio']

        data = {
            "cidade": cidadePasseio,
            "dataIda": dataidaPasseio
        }

        data = client.send({**data})

        print(f"Resposta {data}")

        return redirect(url_for(''))
    return render_template('passeio.html')


@app.route('/showPasseio')
def showPasseio():
    return render_template('showPasseio.html')


if __name__ == "__main__":
    app.run()
