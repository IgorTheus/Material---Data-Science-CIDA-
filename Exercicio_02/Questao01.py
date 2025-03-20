#(1) Carregamento das bibliotecas
import numpy as np

#(2) Entradas de dados
dados = [7, 5, 4, 5, 6, 3, 8, 4, 5, 4, 6, 4, 5, 6, 4, 6, 6, 3, 8, 4, 5, 4, 5, 5, 6]

#(3) Processamento de dados
media = np.mean(dados)
mediana = np.median(dados)


# Arredondamento do dados
media = np.round(media, decimals=2)
mediana = np.round(mediana, decimals=2)

# Calculos para o boxplot
Q1 = np.percentile(dados, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(dados, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(dados, 75, method="averaged_inverted_cdf")

aprovados = []
reprovados = []

for i in dados:
    if dados[i] >= 5:
        aprovados.append(dados[i])
        i += 1
    else:
        reprovados.append(dados[i])
        i += 1

varr = np.var(reprovados)
vara = np.var(aprovados)

#(4) Resultados e visualizações
print(f"A media das notas dos alunos é: {media}\n"
      f"A mediana das notas é: {mediana}\n"
      f"\n"
      f"|Q1 = {Q1}\n"
      f"|Q2 = {Q2}\n"
      f"|Q3 = {Q3}\n"
      f"\n"
      f"Foram {len(aprovados)} aprovados, com as notas: {aprovados}\n"
      f"Com variancia de {vara}\n"
      f"Foram {len(reprovados)} reprovados, com as notas: {reprovados}\n"
      f"Com variancia de {varr}\n"
      f"\n"
      f"Existem mais alunos aprovados do que reprovados, com a variancia dos aprovados sendo maior que a dos aprovados")


