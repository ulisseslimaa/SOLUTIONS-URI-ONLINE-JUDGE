vetor = []
cont = 0
vetor_impar = []
vetor_par = []
resto = []
for i in range(15):
    
    a = int(input())
    vetor.append(a)


for i in vetor:
    if i%2==0:
        vetor_par.append(i)
    else:
        vetor_impar.append(i)
    if len(vetor_par) == 5:
        for a in vetor_par:
            print("par[{}] = {}".format(cont,a))
            cont+=1
        cont = 0
        vetor_par = []
    if len(vetor_impar) == 5:
        pos = 0
        for p in vetor_impar:
            print("impar[{}] = {}".format(cont,p))
            cont+=1
        cont = 0
        vetor_impar = []

if len(vetor_impar) > 0:
    for i in vetor_impar:
        print("impar[{}] = {}".format(cont,i))
        cont+=1
    cont = 0

        
       
if len(vetor_par) > 0:
    for i in vetor_par:
        print("par[{}] = {}".format(cont,i))
        cont+=1
    cont = 0