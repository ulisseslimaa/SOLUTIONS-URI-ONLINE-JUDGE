a, b, c, d = map(int, input().split())

ini = a * 60 + b
fin = c * 60 + d
duracao = 0

if a <= c:
    duracao = fin - ini
    if duracao == 0:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%((duracao - duracao%60)/60, duracao%60))
else:
    duracao = (24 * 60 - ini) + fin
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%((duracao - duracao%60)/60, duracao%60))
    
