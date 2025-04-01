import pandas as pd
from flask import jsonify
from app import df_operadoras, remover_acentos
import numpy as np 

def buscar_operadoras(termo_busca):
    termo_busca_sem_acentos = remover_acentos(termo_busca)

    df_operadoras['Razao_Social_Sem_Acentos'] = df_operadoras['Razao_Social'].apply(remover_acentos)

    resultados = df_operadoras[
        df_operadoras['Razao_Social_Sem_Acentos'].str.contains(termo_busca_sem_acentos, case=False, na=False)
    ].copy()

    resultados['Relevancia'] = resultados['Razao_Social_Sem_Acentos'].apply(lambda x: x.lower().count(termo_busca_sem_acentos))
    resultados = resultados.sort_values(by='Relevancia', ascending=False)
    resultados = resultados.head(5)

    resultados.drop(columns=['Razao_Social_Sem_Acentos'], inplace=True)

    # Substitua NaN por None
    resultados = resultados.replace({np.nan: None})

    if resultados.empty:
        return jsonify({"mensagem": "Nenhuma operadora encontrada."}), 404

    return jsonify(resultados.to_dict(orient='records'))

def buscar_por_registro(registro):
    if not registro:
        return jsonify({"mensagem": "Por favor, forneça um número de registro válido."}), 400

    resultados = df_operadoras[df_operadoras['Registro_ANS'] == int(registro)]
    resultados = resultados.head(1)

    resultados = resultados.replace({np.nan: None})

    if resultados.empty:
        return jsonify({"mensagem": "Nenhuma operadora encontrada."}), 404

    return jsonify(resultados.to_dict(orient='records'))

def buscar_por_cnpj(cnpj):
    if not cnpj:
        return jsonify({"mensagem": "Por favor, forneça um número de CNPJ válido."}), 400

    resultados = df_operadoras[df_operadoras['CNPJ'] == int(cnpj)]
    resultados = resultados.head(1)

    resultados = resultados.replace({np.nan: None})

    if resultados.empty:
        return jsonify({"mensagem": "Nenhuma operadora encontrada."}), 404

    return jsonify(resultados.to_dict(orient='records'))

def buscar_por_modalidade(modalidade):
    if not modalidade:
        return jsonify({"mensagem": "Por favor, forneça uma modalidade válida."}), 400

    modalidade_sem_acentos = remover_acentos(modalidade.lower())

    df_operadoras['Modalidade_Sem_Acentos'] = df_operadoras['Modalidade'].apply(remover_acentos)
    resultados = df_operadoras[
        df_operadoras['Modalidade_Sem_Acentos'].str.contains(modalidade_sem_acentos, case=False, na=False)
    ]
    df_operadoras.drop(columns=['Modalidade_Sem_Acentos'], inplace=True)

    resultados = resultados.head(5)

    resultados = resultados.replace({np.nan: None})

    if resultados.empty:
        return jsonify({"mensagem": "Nenhuma operadora encontrada."}), 404

    return jsonify(resultados.to_dict(orient='records'))