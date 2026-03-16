#Etapa 1
#IMPORTES E MONTAGEM DO DRIVE
import pandas as pd
import sqlite3
import os
from google.colab import drive

# Monta o Google Drive
drive.mount('/content/drive')

# 1. DEFINIÇÃO DE CAMINHOS (ADAPTE O NOME DA PASTA SE NECESSÁRIO)
# Certifique-se de que a pasta 'Projeto_Consultoria_RH' existe no seu Drive
folder_path = '/content/drive/MyDrive/Projetos_Tecnologicos/Data_Projects/Projeto_Consultoria_RH/'
csv_file = folder_path + 'WA_Fn-UseC_-HR-Employee-Attrition.csv'
db_name = folder_path + 'consultoria_rh.db'

def atualizar_sistema():
    print("🚀 Iniciando automação de dados...")

    # 2. VERIFICAÇÃO E LIMPEZA (PYTHON)
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)

        # Limpeza Profissional: Minúsculas e Underline
        # Por que? Facilita escrever SQL sem precisar de aspas
        df.columns = [c.lower().replace(' ', '_').replace('.', '_') for c in df.columns]

        # 3. BANCO DE DADOS (SQLite): Persistência no Drive
        # O SQLite criará o arquivo .db dentro da sua pasta no Drive
        conn = sqlite3.connect(db_name)

        # 'replace' substitui a tabela toda, garantindo dados novos a cada rodada
        df.to_sql('funcionarios', conn, if_exists='replace', index=False)
        conn.close()

        print(f"✅ Sucesso! {len(df)} registros processados e salvos no Drive.")
        print(f"📂 Local: {db_name}")
    else:
        print(f"❌ Erro: Arquivo CSV não encontrado no caminho: {csv_file}")

if __name__ == "__main__":
    atualizar_sistema()
