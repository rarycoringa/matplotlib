## Visualização e Manipulação de Dados com Python
# Aula 02 - Legenda em Gráficos

import matplotlib.pyplot as plt

x = [1, 2, 5, 8, 10]
y = [2, 3, 7, 8, 13]

# Título
plt.title('Meu primeiro gráfico com Python')

# Legenda dos Eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Gerando o Gráfico de Linha
plt.plot(x, y)

# Visualizar o gráfico gerado
plt.show()
