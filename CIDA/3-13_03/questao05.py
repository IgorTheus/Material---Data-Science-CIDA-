#(1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#(2) Entradas de dados
median = 15
Q1 = 10
Q3 = 40
DQ = Q3 - Q1

Min = max(10, Q1 - 1.5 * DQ)
Max = min(20, Q3 + 1.5 * DQ)

#(3) Processamento de dados
data = [Min, Q1, median, Q3, Max]

#(4) Resultados e visualizações

grafico = plt.boxplot(data)
plt.title('Dados')
plt.show()

