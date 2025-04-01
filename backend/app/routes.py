from flask import request
from app import app
from app.operadora_services import buscar_operadoras, buscar_por_registro, buscar_por_cnpj, buscar_por_modalidade

@app.route('/operadoras/busca', methods=['GET'])
def rota_buscar_operadoras():
    termo_busca = request.args.get('termo', '').lower()
    return buscar_operadoras(termo_busca)

@app.route('/operadoras/registro', methods=['GET'])
def rota_buscar_por_registro():
    registro = request.args.get('registro', None)
    return buscar_por_registro(registro)

@app.route('/operadoras/cnpj', methods=['GET'])
def rota_buscar_por_cnpj():
    cnpj = request.args.get('cnpj', None)
    return buscar_por_cnpj(cnpj)

@app.route('/operadoras/modalidade', methods=['GET'])
def rota_buscar_por_modalidade():
    modalidade = request.args.get('modalidade', None)
    return buscar_por_modalidade(modalidade)
