n = int(input())
for i in range(n):
    primo = int(input())
    ativador = 0
    if(primo==0 or primo==1):
        print("{} nao eh primo".format(primo))
    else:
        
        for numero in range(1,primo+1):
            if(primo%numero==0):
                ativador+=1
        if(ativador>2):
            print("{} nao eh primo".format(primo))
        else:
            print("{} eh primo".format(primo))