x,y = map(int, input().split())
linhas = 0
soma = ""
numero = 1
while numero < y:
    while linhas < x:
        soma = soma + str(numero) + " "
        numero+=1
        linhas+=1
    linhas = 0
    print(soma[0:-1])
    soma= ""