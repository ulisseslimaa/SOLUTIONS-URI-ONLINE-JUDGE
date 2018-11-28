n = int(input())
val = list(map(int, input().split()))

menor = min(val)
indice = val.index(menor)

print("Menor valor: %d"%menor)
print("Posicao: %d"%indice)