fibonaci = [0,1]
a = 0
b = 1

for i in range(60):
    c = b + a
    fibonaci.append(c)
    a = b
    b = c
u = int(input())

for i in range(u):
    n = int(input())
    print('Fib(%d) = %d'%(n, fibonaci[n]))
