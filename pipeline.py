import sys
from pathlib import Path
import pandas as pd

# verifica se o usuário passou um arquivo de entrada como argumento
if len(sys.argv) < 2:
    print("Uso: python script.py <arquivo1.csv> <arquivo2.csv> ...")
    sys.exit(1)

# captura o nome dos arquivos passados pela linha de comando
arquivos_entrada = sys.argv[1:]

# colunas do dataframe
colunas = [
    'medição', 'unidade de medida', 'evento', 'stddev',
    'time counter active', '% time counter active', 'extra_1', 'extra_2'
]

# para cada arquivo de entrada passado
for caminho_entrada in arquivos_entrada:
    caminho = Path(caminho_entrada)

    # verifica se o arquivo existe e avisa se não existir e pula pra o próximo arquivo
    if not caminho.exists():
        print(f"Aviso: Arquivo {caminho} não encontrado. Pulando...")
        continue

    # leia o CSV, usando ';' como separador e sem cabeçalho e como string
    df = pd.read_csv(caminho_entrada, sep=';', names=colunas, header=None, dtype=str)

    # se o dataframe estiver vazio, continue para o próximo arquivo
    if df.empty:
        continue

    # remove espaços em branco no início e no fim da coluna 'evento'
    df['evento'] = df['evento'].str.strip()
    # troque as vírgulas por pontos e converta a coluna 'medição' para float
    df['medição'] = df['medição'].str.replace(',', '.').astype(float)
    # adiciona uma coluna 'run_id' para identificar cada execução do experimento
    df['run_id'] = (df['evento'] == df['evento'].iloc[0]).cumsum()

    # pivota o dataframe para ter uma linha por rodada do experimento utilizando 
    # a coluna 'run_id' como índice, e as colunas serão os eventos, com os valores 
    # sendo as medições obtidas
    new_df = df.pivot(index='run_id', columns='evento', values='medição').reset_index(drop=True)

    # captura o número da entrada do experimento a partir do nome do arquivo de entrada
    entrada_xp = "".join(filter(str.isdigit, caminho_entrada))

    # adiciona uma coluna com o número da entrada do experimento
    new_df['entrada do experimento'] = entrada_xp

    # itera sobre os eventos de tempo e converte os valores de nanosegundos para segundos
    for col_tempo in ['system_time', 'user_time', 'duration_time']:
        if col_tempo in new_df.columns:
            new_df[col_tempo] = new_df[col_tempo] / 1e9

    # calcula a potência consumida com base na coluna de energia e na coluna de tempo,
    # se ambas existirem
    if 'power/energy-pkg/' in new_df.columns and 'duration_time' in new_df.columns:
        new_df['potência'] = new_df['power/energy-pkg/'] / new_df['duration_time']

    # define o caminho de saída para o CSV tratado, baseado no número da entrada do experimento
    # Salva na MESMA pasta onde o arquivo original está
    saida = caminho.parent / f'resultado-tratado-entrada-{entrada_xp}.csv'

    # salva o dataframe tratado em um novo arquivo CSV, sem o índice e usando ';' como separador
    new_df.to_csv(saida, index=False, sep=';')