import pandas as pd
from flask import Flask, jsonify

server = Flask(__name__)

@server.route('/')
def home():
    return 'Bem-vindo'

@server.route('/get-vendas')
def get_vendas():
    tabela = pd.read_csv("dados.csv")
    total_vendas = tabela['Vendas'].sum()
    result = {'total_vendas': total_vendas}
    return jsonify(result)


server.run()
