#(1) Carregamento das bibliotecas
import numpy as np                      #Biblioteca para calculos
import matplotlib.pyplot as plt         #Biblioteca para graficos

#(2) Entradas de dados
dados = [52, 56, 62, 54, 52, 51, 60, 61,
         56, 55, 56, 54, 57, 67, 61, 49]

#(3) Processamento de dados
media = np.mean(dados)
mediana = np.median(dados)
sigma = np.std(dados)
org = sorted(dados)

# Arredondamento do dados
media = np.round(media, decimals=2)
sigma = np.round(sigma, decimals=2)

# Calculos para o boxplot
Q1 = np.percentile(dados, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(dados, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(dados, 75, method="averaged_inverted_cdf")

dq = Q3 - Q1
vmin = min(dados)
vmax = max(dados)

LI = max(vmin, Q1 - 1.5*dq)
LS = min(vmax, Q3 + 1.5*dq)

#(4) Resultados e visualizações
print(f"A media dos dados é {media}\n"
      f"A mediana dos dados é {mediana}\n"
      f"O desvio padrão dos dados é {sigma}\n"
      f"Dados em ordem crescente: {org}\n"
      f"\n"
      f"|Q1 = {Q1}\n"
      f"|Q2 = {Q2}\n"
      f"|Q3 = {Q3}\n"
      f"|LI = {LI}\n"
      f"|LS = {LS}")

grafico = plt.boxplot(dados)
plt.title ("Boxplot dos pesos dos valores")
plt.ylabel ("Peso (KG)")
plt.xlabel ("Alunos")

plt.show()
