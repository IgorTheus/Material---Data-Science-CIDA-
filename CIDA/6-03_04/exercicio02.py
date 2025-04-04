#(1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#(2) Entradas de dados
dcit_vazio = {}
data = {
    "nomes" : ["João", "Jose", "Maria"],
    "idades" : [25, 29, 15],
    "notas" : [50, 20, 86]
}

#(3) Processamento de dados

# A)
data["nomes"].append("Carlos")
data["idades"].append(29)
data["notas"].append(90)

# B)
media_maria = data["notas"][2]

# C)
data["notas"][0] = 60

# D)
data["faltas"] = []
data["faltas"].append(10)
data["faltas"].append(5)
data["faltas"].append(7)
data["faltas"].append(2)

# E)
mean_notas = data["notas"]
media_geral = np.mean(mean_notas)

#(4) Resultados e visualizações
print(f"{data}\n"
      f"Nota da Maria: {media_maria}\n"
      f"Listas de medias: {mean_notas}\n"
      f"Media da turma: {media_geral}")



