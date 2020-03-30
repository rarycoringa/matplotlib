## Visualização e Manipulação de Dados com Python
# Aula 04 - Scatterplot: Gráfico de Dispersão

import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]


titulo = 'Scatterplot: Gráfico de Dispersão'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Título
plt.title(titulo)

# Legenda dos Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Gerando um Gráfico Scatterplot
plt.scatter(x, y, label='Meus pontos', color='green') # Pontos
plt.plot(x, y) # Linhas

# Gerando a legenda do gráfico (label)
plt.legend()

# Visualizar o gráfico gerado
plt.show()
