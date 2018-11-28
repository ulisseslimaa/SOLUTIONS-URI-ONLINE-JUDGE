a = int(input())
b = int(input())
lista = []
for i in range(a):
    entrada = int(input())
    lista.append(entrada)
cont = 0
lista.sort()
while cont<b:
    maior = lista[-1]
    contador = lista.count(maior)
    cont+=contador
    for p in range(contador):
        lista.remove(maior)
print(cont)