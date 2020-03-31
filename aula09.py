## Visualização e Manipulação de Dados com Python
# Aula 09 - Boxplot: Diagrama de Caixa

import matplotlib.pyplot as plt
import random # Biblioteca de valores aleatórios

vetor = []

for i in range(100):
    numero_aleatorio = random.randint(0, 50)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title('Boxplot')
plt.show()
