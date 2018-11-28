n = int(input())
somas = []
for i in range(n):
    impares = 0
    cont = 0
    x,y = map(int, input().split())
    inicio = x
    if x%2==0:
        inicio = inicio + 1
    while(cont < y):
        impares += inicio
        cont += 1
        inicio+=2
    somas.append(impares)
    
    
print("\n".join(map(str, somas)))