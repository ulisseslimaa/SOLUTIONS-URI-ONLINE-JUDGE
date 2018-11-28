matriz = []
l = int(input())
op = input()
for i in range(12):
    linha = []
    for p in range(12):
        a = float(input())
        linha.append(a)
    matriz.append(linha)
soma = 0
for i in matriz[l]:
    soma+=i

if op == "M":
    soma = soma/12
print("{:.1f}".format(soma))