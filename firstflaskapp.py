from flask import Flask 
from flask import render_template
from flask import request
import json 
from client import main
from server import mainServer

app = Flask(__name__)

aeroporto={}

@app.route('/') #home.html

def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])

def getdata():
    aeroporto = request.form['aeroporto']
    dataida = request.form['dataida']
    datavolta = request.form['datavolta']
    passagens = request.form['npassagens']
    cidades = request.form['cidades']
    dataidahotel = request.form['dataidahotel']
    datavoltahotel = request.form['datavoltahotel']
    npessoas = request.form['npessoas']
    cidadePasseio = request.form['cidadePasseio']
    dataidaPasseio = request.form['dataidaPasseio']

    aeroporto = {
        "aeroporto":aeroporto,
        "dataIda": dataida,
        "dataVolta":datavolta,
        "numeroPassagens":passagens
    }

   

    hotel = {
        "cidade":cidades,
        "dataIda":dataidahotel,
        "dataVolta":datavoltahotel,
        "numeroPessoas":npessoas
    }
    

    passeio = {
        "cidade":cidadePasseio,
        "dataIda":dataidaPasseio
    }
   
    print(aeroporto)
    print(hotel)
    print(passeio)


    return "Enviado com sucesso!!"


if __name__ == "__main__":
    app.run()    

main(aeroporto)
mainServer()