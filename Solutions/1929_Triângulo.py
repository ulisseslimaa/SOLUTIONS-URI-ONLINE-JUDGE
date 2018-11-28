a,b,c,d = map(int, input().split())

lista = [a,b,c,d]
lista.sort()

if lista[0] + lista[1] > lista[2] or lista[1] + lista[2] > lista[3]:
    print("S")
else:
    print("N")