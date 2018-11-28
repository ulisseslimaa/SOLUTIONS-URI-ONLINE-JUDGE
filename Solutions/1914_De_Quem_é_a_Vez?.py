escolha = int(input())
for quant in range(escolha):
    a,a1,b,b1=input().split()
    num1,num2 = map(int, input().split())
    if (num1+num2)%2==0:
        ganho = "PAR"
    else:
        ganho = "IMPAR"
    if a1 == ganho:
        print(a)
    elif b1 == ganho:
        print(b)