## Visualização e Manipulação de Dados com Python
# Aula 10 - Estudo de Caso: Bioinformática - Comparando Genomas

entrada = open('bacteria.fasta').read()
saida = open('bacteria.html','w')

# Criando um dicionário
cont = {}

# Incrementando o dicionário com todos os pares
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace('\n','')

# Realizando a contagem dos pares
for k in range(len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1

# Gerando o HTML
i = 1

for k in cont:
    transparencia = cont[k]/max(cont.values())
    saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+")'>"+k+"</div>")

    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")

    i+=1

saida.close()
