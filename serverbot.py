## realizar flask server telegram to github...
import flask
import requests
import threading
import json
import socket


app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return '<h1>Hola Nanae hortensia !</h1><br/>' \
           'Felipe Huerta esta corriendo un servidor'

@app.route('/recepcion_accion_bot', methods=['POST'])
def recepcion_accion_bot():
    pass
    #estructura de ifs para elegir que post mandar a api github


    #data obtenida :flask.request.json
    #flask.request.headers
    #return "Echo: {}".format(json.dumps(flask.request.json)) 

@app.route('/recepcion_notificacion_github', methods=['POST'])
def recepcion_notificacion_github():
    pass
    #data obtenida :flask.request.json
    #return "Echo: {}".format(json.dumps(flask.request.json))



def mandar_accion_github(data):
    url = ''
    #realizar accion con data y crear msg
    req = requests.post(url,msg)


def mandar_accion_telegram(data):
    url = ''
    #realizar accion con data y crear msg
    req = requests.post(url,msg)

    
if __name__ == '__main__':
    app.run(port=8080)
    