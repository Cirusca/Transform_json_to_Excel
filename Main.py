import pandas as pd
import json



#EXTRAIR
with open('db.json', 'r') as f:
    data = json.loads(f.read())
#TRANSFORM
    dados = pd.json_normalize(data=data['livros'])
#TODO - Fazer um filtro de colunas

dados = dados.rename(columns={
    'descricao': 'Descrição',
    'titulo': 'Titulo',
    'categoria': 'Categoria',
    'paginas': 'Paginas',
    'estoque': 'Estoque',
    'autores.autor1': 'Autor',
    'preco': 'Preço'
})
#LOADING
dados.to_excel('data.xlsx')