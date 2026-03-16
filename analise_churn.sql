#Etapa 1
#IMPORTES E MONTAGEM DO DRIVE
import pandas as pd
import sqlite3
import os
from google.colab import drive

# Monta o Google Drive
drive.mount('/content/drive')

# 1. DEFINIÇÃO DE CAMINHOS (ADAPTE O NOME DA PASTA SE NECESSÁRIO)
# consultas avulsas com SQL - (Esse Script pode ser apagado)

# "Qual a média salarial e a idade média dos funcionários que saíram
# (Attrition = 'Yes') vs. os que ficaram?"

# conectando para validar os dados
conn = sqlite3.connect(db_name)

# Query de negocio: comparativo de quem saiu(yes) vs quem ficou(no)

query = """
select
  attrition,
  count (*) as total_funci,
  round (avg(age), 2) as idade_media,
  round (avg(monthlyincome), 2) as salario_medio
from funcionarios
group by attrition;
"""

# Executando e exibindo o resultado

df_validacao = pd.read_sql_query(query, conn)
conn.close()

print('Relatório de Diagnostico Inicial:')
print(df_validacao)