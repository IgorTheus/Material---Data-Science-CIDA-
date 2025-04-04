#(1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import histogram

#(2) Entradas de dados
data = [45, 56, -89.0, 23.4, 1.5, 2.5, 5.5, 10.0, -50.0, 1.0]

data.append(-12.5)

#(3) Processamento de dados

# Calculos para o boxplot
Q1 = np.percentile(data, 25, method="averaged_inverted_cdf")
Q3 = np.percentile(data, 75, method="averaged_inverted_cdf")

dq = Q3 - Q1
vmin = min(data)
vmax = max(data)

LI = max(vmin, Q1 - 1.5 * dq)
LS = min(vmax, Q3 + 1.5 * dq)

counter = range(len(data))
data_filter = []

for i in counter:
      valor = data[i]
      if (valor < LS and valor > LI):
            data_filter.append(data[i])

total_data = [data, data_filter]

lenght = len(data_filter)

# Determinação do numero de bins
k = 1 + 3.32 * np.log10(lenght)
k_final = int(np.round(k))

# Construção do histrograma
tabela = np.histogram(data_filter, k_final)

abst = tabela[0]
classes = tabela[1]
class_inicio = classes[0]
class_final = classes[1]
rlt = (abst / lenght) * 100

#(4) Resultados e visualizações
print(f"LI: {LI}\n"
      f"LS: {LS}")

boxplot = plt.boxplot(total_data, tick_labels=["Dados originais", "Dados filtrados"])
plt.title("Numeros orginais")
plt.show()

print(rlt)

plt.hist(classes[:-1], int(k), weights=rlt)
plt.title("Histograma dos dados filtrados")

plt.show()



