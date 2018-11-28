vetor = []
cont = 0
for i in range(20):
    x = int(input())
    vetor.insert(0, x)
for j in vetor:
    print("N[{}] = {}".format(cont,j))
    cont+=1