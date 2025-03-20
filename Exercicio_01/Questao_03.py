#(1) Carregamento das bibliotecas
import numpy as np

#(2) Entradas de dados
dureza = [83.3, 80.7, 86.4, 88.3, 84.7, 85.2, 82.8, 87.8, 86.9, 86.2, 83.5, 84.4, 87.2, 85.5, 86.3]

#(3) Processamento de dados
mean = np.mean(dureza)
median = np.median(dureza)
std = np.std(dureza)

#(4) Resultados e visualizações
print(f"A media da dureza é: {mean}\n"
      f"A mediana da dureza é: {median}\n"
      f"O desvio-padrão da dureza é: {std.round(decimals=2)}")