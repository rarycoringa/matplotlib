## Visualização e Manipulação de Dados com Python
# Aula 07 - Salvando Figuras

import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 300, 700, 100, 10]

titulo = 'Scatterplot: Gráfico de Dispersão'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Título
plt.title(titulo)

# Legenda dos Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Gerando um Gráfico Scatterplot
plt.scatter(x, y, label='Meus pontos', color='g', marker='h', s=z) # Pontos
plt.plot(x, y, color='k', linestyle='--') # Linhas

# Gerando a legenda do gráfico (label)
plt.legend()

# Salvando a imagem no diretório atual
plt.savefig('figura1.png', dpi=500)

# Visualizar o gráfico gerado
plt.show()

'''
Documentação oficial do Matplotlib
Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

Cores (color):
'b'	blue
'g'	green
'r'	red
'c'	cyan
'm'	magenta
'y'	yellow
'k'	black
'w'	white

Marcadores (marker):
'.'	point marker
','	pixel marker
'o'	circle marker
'v'	triangle_down marker
'^'	triangle_up marker
'<'	triangle_left marker
'>'	triangle_right marker
'1'	tri_down marker
'2'	tri_up marker
'3'	tri_left marker
'4'	tri_right marker
's'	square marker
'p'	pentagon marker
'*'	star marker
'h'	hexagon1 marker
'H'	hexagon2 marker
'+'	plus marker
'x'	x marker
'D'	diamond marker
'd'	thin_diamond marker
'|'	vline marker
'_'	hline marker

Tipos de linha (linestyle):
'-'	solid line style
'--'	dashed line style
'-.'	dash-dot line style
':'	dotted line style
'''
