a = int(input())
string = 'Feliz natl!'
lista = []
for i in string:
    lista.append(i)
for i in range(a):
    lista.insert(9,'a')
print("".join(lista))