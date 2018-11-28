qtd = int(input())
for i in range(qtd):
    bonus = int(input())
    ataque1,defesa1,level1 = map(int,input().split())
    ataque2,defesa2,level2 = map(int,input().split())
    if level1 % 2 == 0:
        valorGolpe1 = ((ataque1 + defesa1)/2) + bonus
    else:
        valorGolpe1 = (ataque1 + defesa1)/2
    if level2 % 2 == 0:
        valorGolpe2 = ((ataque2 + defesa2)/2) + bonus
    else:
        valorGolpe2 = (ataque2 + defesa2)/2
    if valorGolpe1 > valorGolpe2:
        print("Dabriel")
    elif valorGolpe2 > valorGolpe1:
        print('Guarte')
    else:
        print('Empate')