#------------------------------------------------#
while True:
    total = 0
    num, num2 = map(int, input().split())
    if num <= 0 or num2 <= 0:
        break
    if num < num2:
        for i in range(num,num2+1):
#            print("%d"%i,end=" ")
            total += i
    elif num2 < num:
        for i in range(num2,num+1):
#            print("%d"%i, end=" ")
            total += i
    else:
        total = num
    print("Sum=%d"%total)

#------------------------------------------------#
while True:
    try:
        m,n = list(map(int,input().split()))
        if(m < 1 or n < 1 ):
            break
        tmp = 0

        if(m > n):
            tmp = m
            m = n
            n = tmp
        soma = 0
        resultado = ''
        while(m <= n):
            resultado += str(m) + ' '
            soma += m
            m += 1
        resultado += 'Sum=%d'
        print(resultado %soma)
    except:
        break
#------------------------------------------------#