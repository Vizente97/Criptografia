from flask import Flask, render_template, request, jsonify
import pandas as pd 
from io import StringIO, BytesIO
import numpy as np
import matplotlib.pyplot as plt
plt.matplotlib.use('agg')
from base64 import b64encode

#####Programas
from Programas.RSAOAEP import rsa

app = Flask("Criptografía")

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/404.html')
def error404():
    return render_template('404.html')

@app.route('/Cifrado_action.html')
def Cifrado_action():
    return render_template('Cifrado_action.html')

@app.route('/Descifrado_action.html')
def Descifrado_action():
    return render_template('Descifrado_action.html')

@app.route('/Firmas_action.html')
def Firmas_action():
    return render_template('Firmas_action.html')

@app.route('/llaves_action.html')
def llaves_action():
    return render_template('404.html')

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')

##########################################################################################

@app.route("/cifrado")
def cifrado():
    rsa.cadenas()
    tiempos_cifrado = rsa.time_cifrar()
    print(tiempos_cifrado) 
    return jsonify(True)

##########################################################################################

if __name__ == '__main__':
    app.run()