while (True):
    l = []
    x = int(input())
    if(x == 0):
        break
    else:
        for i in range(1,x+1):
            l.append(i)
        print(" ".join(map(str, l)))