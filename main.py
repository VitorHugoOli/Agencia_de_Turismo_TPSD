from flask import Flask, request, redirect, url_for, render_template

from sockets.client import EasySocketClient

app = Flask(__name__)
# aeroporto
aeroporto = {}

dados = []

dados_aero = {}

# hotel
hotel = {}
diaEntrada = []
numero = []
qtdQuartos = []
qtdCamas = []
valor = []
nome = []
endereco = []
cidade = []
cafeDaManha = []

serverAero = EasySocketClient(5050)
serverHotel = EasySocketClient(5051)


# serverPasseio = EasySocketClient(5052)


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

        aeroporto = serverAero.send({'action': 'passagem', **data})

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
            "numeeroDePessoas": npessoas,
            "dataIda": dataidahotel,
            "dataVolta": datavoltahotel,
        }

        hotel = serverHotel.send({'action': 'hospedar', **data})

        print(f"Resposta {data}")

        return redirect('/showHotel')
    return render_template('hotel.html')


@app.route('/showHotel')
def showHoteis():
    if request.method == 'POST':
        return redirect('/passeio')
    return render_template('showHotel.html', len=len(hotel), diaEntrada=diaEntrada, numero=numero,
                           qtdQuartos=qtdQuartos, qtdCamas=qtdCamas, valor=valor, nome=nome, endereco=endereco,
                           cidade=cidade, cafeDaManha=cafeDaManha)


@app.route('/passeio', methods=['POST', 'GET'])
def selectPasseio():
    if request.method == 'POST':
        cidadePasseio = request.form['cidadePasseio']
        dataidaPasseio = request.form['dataidaPasseio']

        data = {
            "cidade": cidadePasseio,
            "dataIda": dataidaPasseio
        }

        # data = serverPasseio.send({**data})

        print(f"Resposta {data}")

        return redirect('/showPasseio')
    return render_template('passeio.html')


@app.route('/showPasseio')
def showPasseio():
    return render_template('showPasseio.html')


if __name__ == "__main__":
    app.run()
