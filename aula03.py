## Visualização e Manipulação de Dados com Python
# Aula 03 - Gráfico de Barras

import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = 'Meu gráfico em barras com Python'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Título
plt.title(titulo)

# Legenda dos Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Gerando um Gráfico duplo em Barras
plt.bar(x1, y1, label = 'Grupo 1')
plt.bar(x2, y2, label = 'Grupo 2')

# Gerando a legenda do gráfico (label)
plt.legend()

# Visualizar o gráfico gerado
plt.show()
