#(1) Carregamento das bibliotecas
import numpy as np

#(2) Entradas de dados
marca_a = [153, 173, 134, 157, 149, 171, 162]
marca_b = [172, 163, 151, 146, 146]

#(3) Processamento de dados
mean_a = np.mean(marca_a)
mean_b = np.mean(marca_b)

dpad_a = np.std(marca_a)
dpad_b = np.std(marca_b)

#(4) Resultados e visualizações
print(f"A)\n"
      f"A media da marca A é: {mean_a}\n"
      f"O desvio-padrao da marca A é: {dpad_a.round(decimals=2)}\n"
      f"A media da marca B é: {mean_b}\n"
      f"O desvio-padrão da marca B é: {dpad_b.round(decimals=2)}")

print(f"===========================================\n"
      f"B)\n"
      f"A marca B, pois ela possuiu uma consistencia e uma previsibilidade de uso maior que a da marca A")

print(f"===========================================\n"
      f"C)\n"
      f"A marca B tambem, pelo fato dela não ter uma variação tão grande")