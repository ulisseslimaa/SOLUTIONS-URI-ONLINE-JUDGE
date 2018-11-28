try:
    while True:
        tamanho = int(input())
        soma = 0
        km = map(int, input().split())
        km = list(km)
        maior = max(km)
        if maior < 10:
            print(1)
        elif maior>=10 and maior<20:
            print(2)
        else:
            print(3)

except EOFError:
    pass