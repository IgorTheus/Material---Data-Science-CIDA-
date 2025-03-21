#(1) Carregamento das bibliotecas
import numpy as np
import scipy as sp

#(2) Entradas de dados
seguros = [33.6, 14.0, 12.9, 12.2, 5.5, 5.3, 3.1, 2.9, 1.7, 1.0, 0.9]

#(3) Processamento de dados
media = np.mean(seguros)
mediana = np.median(seguros)
variancia = np.var(seguros)
moda = sp.stats.mode(seguros)[0]

#Arrendodamento dos valores
media = np.round(media, decimals=2)
variancia = np.round(variancia, decimals=2)


#(4) Resultados e visualizações
print(f"A media dos dados de seguros é: {media}\n"
      f"A medianada dos dados de seguros é: {mediana}\n"
      f"A moda dos dados de seguros é: {moda}, aparecendo {sp.stats.mode(seguros)[1]} vezes\n"
      f"A variancia dos dados e seguros é: {variancia}\n")
