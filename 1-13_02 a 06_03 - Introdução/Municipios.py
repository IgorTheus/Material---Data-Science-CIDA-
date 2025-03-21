#(1) Carregamento das bibliotecas
import numpy as np                      #Biblioteca para calculos
import matplotlib.pyplot as plt         #Biblioteca para graficos

#(2) Entradas de dados
dados = [988.8, 556.9, 224.6, 210.9, 201.5, 187.7, 151.6, 135.8, 129.8, 119.4, 116.0, 102.3, 101.8, 92.4, 84.7,
         83.9, 80.2, 74.7, 72.7, 68.4, 66.8, 66.8, 63.7, 62.8, 61.9, 56.2, 54.1, 50.3, 49.7, 46.3]

pop_sudeste = [988.8, 101.8, 92.4, 63.7, 62.8, 68.4, 49.7, 46.3,
               556.9, 84.7, 83.9, 72.7,
               210.9, 50.3]

#(3) Processamento de dados
info_boxplots =  [dados, pop_sudeste]
boxplot_brasil = plt.boxplot(info_boxplots, tick_labels = ["Brasil" , "Sudeste"])


#(4) Resultados e visualizações
print(f"A quantidade de dados é: {len(dados)}\n"
      f"Visualização da variavel dupla {info_boxplots}")

plt.title("Boxplot das populações do Brasil")
plt.ylabel("Quantidades de habitantes")
plt.show()


