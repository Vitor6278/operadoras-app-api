from flask import Flask
from flask_cors import CORS  
import pandas as pd

app = Flask(__name__)

CORS(app)

df_operadoras = pd.read_csv('data/operadoras.csv', delimiter=';')

def remover_acentos(texto):
    from unidecode import unidecode
    return unidecode(texto)

from app import routes