quant = int(input())
for i in range(quant):
    a,b = map(int, input().split())
    a,b = str(a),str(b)
    c = len(a)-len(b)
    if a[c:len(a)] == b:
        print('encaixa')
    else:
        print('nao encaixa')