def fatorial(numero):
    fatorial = 1
    for i in range(1,numero+1):
        fatorial *= i
    return fatorial


while True:
    try:
        a,b = map(int, input().split())
        fat1 = fatorial(a)
        fat2 = fatorial(b)
        soma = fat1+fat2
        print(soma)
        
    except EOFError:
        break