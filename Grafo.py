#(1) Carregamento das bibliotecas

import matplotlib.pyplot as plt      # Biblioteca para gráficos
import networkx as nx                # Biblioteca para grafos

#(2) Entradas de dados

amizades = [("Hero", "Dunn"),
            ("Hero", "Sue"),
            ("Dunn", "Sue"),
            ("Dunn", "Chi"),
            ("Sue", "Chi"),
            ("Chi", "Thor"),
            ("Thor", "Clive"),
            ("Clive", "Hicks"),
            ("Clive", "Devin"),
            ("Hicks", "Kate"),
            ("Devin", "Kate"),
            ("Kate", "Klein")]

#(3) Processamento de dados

grafo = nx.Graph()                    # Cria um grafo chamado grafo
grafo.add_edges_from(amizades)

# Contagem de amigos
for pessoa in grafo.nodes():
    vizinhos = list(nx.all_neighbors(grafo, pessoa))
    if len(list(vizinhos)) == 3:
        print(f"O {pessoa} tem 3 amigos, seus vizinhos são: {vizinhos}")

#(4) Resultados e visualizações

nx.draw(grafo, with_labels=True, node_size=1500, font_color="cyan", node_color="gray", font_weight="bold") # Desenha o grafo
plt.show()                            # Mostra o grafo
