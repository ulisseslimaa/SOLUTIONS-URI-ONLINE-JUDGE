p1, n1, v1 = input().split()
p2, n2, v2 = input().split()
n1 = int(n1)
v1 = float(v1)
n2 = int(n2)
v2 = float(v2)
total = (n1*v1) + (n2*v2)
print('VALOR A PAGAR: R$ %.2f' %total)
