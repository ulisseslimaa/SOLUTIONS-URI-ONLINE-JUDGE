j1,r1 = map(int, input().split())
listaJogadas = [int(a) for a in input().split(" ")]



jogadores = []
for a in range(j1):
    jogadores.append([])
contador = 0

for i in listaJogadas:
    jogadores[contador].append(i)
    contador+=1
    if(contador == j1):
        contador = 0
somas = []

for i in jogadores:
    somaJogadas = 0
    for j in i:
        somaJogadas+=j
    somas.append(somaJogadas)
maior = max(somas)

jogaCont = 1
listaMaioresJogadas = []
for i in somas:
    if i == maior:
        listaMaioresJogadas.append(jogaCont)
    jogaCont+=1
    
print(listaMaioresJogadas[-1])



