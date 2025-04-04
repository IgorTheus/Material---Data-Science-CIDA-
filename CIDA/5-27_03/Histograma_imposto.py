#(1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#(2) Entradas de dados
data = [36.9, 28.4, 25.7, 65.4, 46.7, 3.4, 15.8, 20.6, 14.2, 9.0,
        15.1, 1.8, 1.9, 32.7, 17.6, 3.8, 4.5, 37.5, 14.3, 20.3, 
        7.7, 46.5, 12.1, 12.7, 4.8, 3.1, 10.1, 17.8, 28.9, 7.8,
        18.9, 11.0, 11.1, 56.1, 27.0, 2.4, 5.2, 26.0, 8.0, 22.9, 
        30.0, 13.9, 8.0, 3.4, 13.3, 10.2, 14.2, 9.1, 4.8, 29.4]

#(3) Processamento de dados
lenght = len(data)

# Determinação do numero de bins
k = 1 + 3.32 * np.log10(lenght)
k_final = int(np.round(k))

# Extração dos dados de distribuição
tabela = np.histogram(data, bins=int(k_final))
abst = tabela[0]
classes = tabela[1]
class_inicio = classes[0]
class_final = classes[1]


for i in abst:
      rlt = (i / lenght) * 100
      print(f'Classe: {i} - Porcentagem: {rlt}%')

data.sort()
data_filter1 = []
data_filter2 = []
counter = range(len(data))
for i in counter:
      valor = data[i]
      if (valor > 25.0):
            data_filter1.append(data[i])
      elif (valor >= 10.0 and valor <= 20.0):
            data_filter2.append(data[i])

#(4) Resultados e visualizações
print(f"Quantidade de amostras: {lenght}\n"
      f"{tabela}\n"
      f"{classes}\n"
      f"A aliquota mais comum é: {class_inicio} - {class_final}\n"
      f"\nLista ordenada em ordem crescente:\n {data}\n"
      f"\nValores maiores que 25:\n {data_filter1}\n"
      f"\nValores entre 10 e 20:\n {data_filter2}")

plt.hist(data, bins=(k_final))
plt.title("Histograma das classes de Imposto")
plt.ylabel("Quantidade de empresas")
plt.xlabel("Porcentual de imposto(%)")
#plt.show()



