#(1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#(2) Entradas de dados
data = [2, 3, 4, 5, 5, 5, 5, 6, 7, 8,
        8, 8, 9, 10, 10, 12, 12, 14, 14, 14,
        16, 20, 23, 25, 25, 28, 30, 32, 35, 38]

#(3) Processamento de dados
lenght = len(data)

# Determinação do numero de bins
k = 1 + 3.32 * np.log10(lenght)
k_final = np.round(k)

# Calculo do tamanho de cada classe
t = max(data) - min(data)
x = t/k_final

# Define o histograma
tabela = np.histogram(data, bins=int(k_final))
plt.hist(data, bins=int(k_final))

#(4) Resultados e visualizações
print(f"Quantidade de amostras: {lenght}\n"
      f"Numero de classes: {k}\n"
      f"Numero de classes (arredondado): {k_final}\n"
      f"Tamanho das classes: {x}")

print(tabela)
plt.title("Histograma do tempo de banho")
plt.ylabel("Qtd de pessoas")
plt.xlabel("Classe de tempo de banho")
plt.show()
