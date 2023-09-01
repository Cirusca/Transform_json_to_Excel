import pandas as pd
import xlsxwriter
import json
import os


#EXTRAIR
df_json = pd.read_json('db.json')

dados = pd.json_normalize(df_json,record_path=['livros'], meta=['descricao'] )
print(dados)
keyss = df_json['livros']

print(keyss)


#TRANSFORM


#LOADING
