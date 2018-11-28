while True:
    x1,y1,x2,y2 = map(int, input().split())
    jogadas = 0
    if(x1 == 0 and x2 == 0 and y1 == 0 and y2==0):
        break
    if (x1 == x2 and y1 == y2):
        jogadas = 0
    else:
        if (x1 == x2):
            jogadas = 1

        elif(y1 == y2):
            jogadas = 1

        elif (abs(x1-x2) == abs(y1-y2)):
            jogadas = 1

        else:
            jogadas = 2

    print(jogadas)