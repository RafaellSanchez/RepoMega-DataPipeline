import sqlite3
import pandas as pd

#arquivo para ser ingerido na tabela
file = "/workspaces/RepoMega-DataPipeline/data/files/full-data-megaMEGA SENA.txt"
separator = ';'

df = pd.read_csv(file, sep=separator)


# Conectar ao banco de dados SQLite (se não existir, será criado automaticamente)
conexao_sqlite = sqlite3.connect('db_mega.db')

# Salvar o DataFrame no banco de dados SQLite
nome_tabela = 'tb_mega'
df.to_sql(nome_tabela, conexao_sqlite, if_exists='replace', index=False)

# Executar uma consulta para visualizar os dados na tabela que você salvou
nome_tabela = 'tb_mega'
consulta = f"SELECT * FROM {nome_tabela};"
cursor = conexao_sqlite.cursor()

resultados = cursor.fetchall()


for linha in resultados:
    print(linha)

cursor.execute(consulta)



# Fechar a conexão com o banco de dados SQLite
cursor.close()
conexao_sqlite.close()


