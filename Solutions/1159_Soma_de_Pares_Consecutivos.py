while(True):
    x = int(input())
    if x == 0:
        break
    if x%2!=0:
        x+=1
    soma = 0
    for i in range(x,x+10):
        if i%2==0:
            soma+=i
    print(soma)