#(1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#(2) Entradas de dados
data_raw = {
    "Automovel" : 33.6,
    "Saude" : 14.0,
    "Incendio" : 12.9,
    "Vida" : 12.2,
    "Riscos Diversos" : 5.5,
    "Habitação" : 5.3,
    "Transporte" : 3.1,
    "Acidentes Pessoais" : 2.9,
    "Obrigatorios Veiculos" : 1.7,
    "Riscos de engenharia" : 1.0,
    "Responsabilidade civil" : 0.9
}

#(3) Processamento de dados
data_f = []
data_f2 = []
data_p = []
for i in data_raw:
    data_p.append(data_raw[i])
    if (data_raw[i] > 10):
        data_f.append(i)

    else:
        data_f2.append(i)

Q1 = np.percentile(data_p, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(data_p, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(data_p, 75, method="averaged_inverted_cdf")

dq = Q3 - Q1
vmin = min(data_p)
vmax = max(data_p)

LI = max(vmin, Q1 - 1.5*dq)
LS = min(vmax, Q3 + 1.5*dq)


#(4) Resultados e visualizações
print(f"Ramos com mais de 10%:\n {data_f}\n"
      f"Ramos com menos de 10%:\n {data_f2}\n"
      f"\nO ramo de Automoveis é o outlier")

grafico = plt.boxplot(data_p)
plt.show()



