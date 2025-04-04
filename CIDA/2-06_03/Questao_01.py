#(1) Carregamento das bibliotecas
import numpy as np

#(2) Entradas de dados
resistencia = [348.5, 340.1, 360.8, 353.2, 357.6]
dmed = []

#(3) Processamento de dados
mean = np.mean(resistencia)
dpad = np.std(resistencia)

#Calcular desvio medio
for i in resistencia:
    dmed.append(abs(i - mean))

desvio_med = np.mean(dmed)

#Arredondamento de valores
mean = np.round(mean, decimals = 2)
dpad = np.round(dpad, decimals = 2)
desvio_med = np.round(desvio_med, decimals = 2)

#(4) Resultados e visualizações
print(f"A tensão media do material é: {mean}\n"
      f"O desvio-padrão é: {dpad}\n"
      f"O desvio-medio é: {desvio_med}")
