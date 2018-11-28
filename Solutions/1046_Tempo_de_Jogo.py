a, b = map(int, input().split())

if a >= b:
    print("O JOGO DUROU %d HORA(S)"% ((24 - a) + b))
else:
    print("O JOGO DUROU %d HORA(S)"% (b - a))
