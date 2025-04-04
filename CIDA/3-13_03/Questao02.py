#(1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#(2) Entradas de dados
mediani = 82
dpi = 10.5
mini = 62
maxi = 90
Q1i = 70
Q3i = 85

medianf = 70
dpf = 9.6

Q1f = 63
Q3f = 77
DQ = Q3f - Q1f

minf = max(58, Q1f - 1.5*DQ)
maxf = min(92, Q3f + 1.5*DQ)

#(3) Processamento de dados
data = [
    [mini, Q1i, mediani, Q3i, maxi],
    [minf, Q1f, medianf, Q3f, maxf]
]

#(4) Resultados e visualizações
# Criando o boxplot
boxplot = plt.boxplot(data, tick_labels=["Intensa", "Fraco"] )

# Adicionando títulos ao gráfico

plt.title('Intenso e Fraco')
plt.ylabel('Valores')

print(f"50% da pulsação de atividade  fisica intensa: {mediani}\n"
      f"50% da pulsação de atividade fisica fraca: {medianf}\n"
      f"A proporção de ambas  é a mesma\n"
      f"A atividade fisica influenciou na media de pulsações\n"
      f"Mais da metade não tem pulsação maior que 82, ja que a mediana é 82, ou seja, a exata metade")

plt.show()

