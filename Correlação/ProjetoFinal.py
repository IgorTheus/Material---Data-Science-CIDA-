# (1) carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbs

# (2) Entrada de dados
arquivo = "dados_brutos.csv"
dados_df = pd.read_csv(arquivo, header=0, delimiter=';')
dados = dados_df.to_dict('list')    # carrega os dados na forma de DICT

# (3) Processamento de dados
# Criação dos dados intermediários do projeto
# Criação das listas vazias
area = []
volume = []
densidade = []
tensao = []

tamanho  = len(dados["ID"])     # Numero de amostras
contador = range(tamanho)       # Cria um contador de 0 a 69 (no. de amostras)

for i in contador:
    raio = dados["Diâmetro (mm)"][i] / 2
    a = np.pi * (raio ** 2)
    area.append(a)

    vol = dados["Altura (mm)"][i] * a
    volume.append(vol)

    den = dados["Massa (g)"][i] / vol
    densidade.append(den)

    ten = dados["Resistência (kgf)"][i] / a
    tensao.append(ten)

tensao_media = np.mean(tensao)
tensao_desvio = np.std(tensao)

ID_ruins = []
for i in contador:
    valor = tensao[i]
    if valor < 2.67:
        id = dados["ID"][i]
        ID_ruins.append(id)


# Determinar importancia de cada variavel atraves do metodo de Pearson
matriz_Pearson = [dados["Resistência (kgf)"],
                  dados["Massa (g)"],
                  densidade,
                  dados["Diâmetro (mm)"],
                  area,
                  dados["Altura (mm)"]]
# Texto nos graficos
rotulos = ["Resist.", "Massa", "Densidade", "Diâmetro", "Área", "Altura"]

correlacao = np.corrcoef(matriz_Pearson) # Aplica a correlção de Pearson

# (4) Apresentação dos resultados
print("Dados carregados: ", dados)
print("Área: ", area)
print("Volume: ", volume)
print("Densidade: ", densidade)
print("Tensão: ", tensao)
print("Tensão média: ", tensao_media)
print("Desvio-padrão da tensão: ", tensao_desvio)

# plt.boxplot(dados["Massa (g)"])
# plt.title("Boxplot da massa")
# plt.show()
#
# plt.boxplot(dados["Resistência (kgf)"])
# plt.title("Boxplot da resistencia")
# plt.show()
#
# plt.boxplot(densidade)
# plt.title("Boxplot da densidade")
# plt.show()
#
# plt.boxplot(tensao)
# plt.title("Boxplot da tensão")
# plt.show()

print("IDs outliers: ", ID_ruins)
print(correlacao)

a=sbs.heatmap(correlacao, annot=True, xticklabels=rotulos, yticklabels=rotulos)
plt.show()

plt.scatter(dados["Diâmetro (mm)"], dados["Resistência (kgf)"], s=10)
plt.show()