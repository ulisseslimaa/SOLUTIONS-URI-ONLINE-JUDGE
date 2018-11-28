n = int(input())
vetor = []
cont = 0
while cont!=1000:
    valor = 0
    for j in range(n):
        vetor.append(valor)
        print("N[{}] = {}".format(cont,valor))
        valor+=1
        cont+=1
        if cont == 1000:
            break