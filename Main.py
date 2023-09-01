import pandas as pd
import json
import os



#EXTRAIR
with open('Transform_json_to_Excel\db.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(data, record_path=['books'], meta=['books', ['books', 'author', 'first_name'], ['books', 'author', 'last_name'], ['books', 'publisher', 'name'], ['books', 'publisher', 'location']])



# dados = pd.json_normalize(data,record_path=['livros'], meta=['livros', ['livros','titulo']])

# print(dados)



#TRANSFORM



#LOADING

