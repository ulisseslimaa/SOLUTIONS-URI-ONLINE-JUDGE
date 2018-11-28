n,c,i,g,grenais,empate = 0,0,0,0,1,0


while(n!=2):
    inter, gremi = map(int, input().split())
    if inter < gremi:
        g+=1
        c = True
    elif(gremi < inter):
        i+=1
        c = True
    else:
        empate+=1
        c = True
    while(c):
        print("Novo grenal (1-sim 2-nao)")
        n = int(input())
        if n == 1:
            c = False
            grenais+=1
        else:
            break



print("{} grenais".format(grenais))
print("Inter:{}".format(i))
print("Gremio:{}".format(g))
print("Empates:{}".format(empate))
if g < i:
    print("Inter venceu mais")
elif i < g:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")